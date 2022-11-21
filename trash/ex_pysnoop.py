def trace(self, frame, event, arg):

    ### Checking whether we should trace this line: #######################
    #                                                                     #
    # We should trace this line either if it's in the decorated function,
    # or the user asked to go a few levels deeper and we're within that
    # number of levels deeper.

    if not (frame.f_code in self.target_codes or frame in self.target_frames):
        if self.depth == 1:
            # We did the most common and quickest check above, because the
            # trace function runs so incredibly often, therefore it's
            # crucial to hyper-optimize it for the common case.
            return None
        elif self._is_internal_frame(frame):
            return None
        else:
            _frame_candidate = frame
            for i in range(1, self.depth):
                _frame_candidate = _frame_candidate.f_back
                if _frame_candidate is None:
                    return None
                elif _frame_candidate.f_code in self.target_codes or _frame_candidate in self.target_frames:
                    break
            else:
                return None

    #                                                                     #
    ### Finished checking whether we should trace this line. ##############

    if event == 'call':
        thread_global.depth += 1
    indent = ' ' * 4 * thread_global.depth

    _FOREGROUND_BLUE = self._FOREGROUND_BLUE
    _FOREGROUND_CYAN = self._FOREGROUND_CYAN
    _FOREGROUND_GREEN = self._FOREGROUND_GREEN
    _FOREGROUND_MAGENTA = self._FOREGROUND_MAGENTA
    _FOREGROUND_RED = self._FOREGROUND_RED
    _FOREGROUND_RESET = self._FOREGROUND_RESET
    _FOREGROUND_YELLOW = self._FOREGROUND_YELLOW
    _STYLE_BRIGHT = self._STYLE_BRIGHT
    _STYLE_DIM = self._STYLE_DIM
    _STYLE_NORMAL = self._STYLE_NORMAL
    _STYLE_RESET_ALL = self._STYLE_RESET_ALL

    ### Making timestamp: #################################################
    #                                                                     #
    if self.normalize:
        timestamp = ' ' * 15
    elif self.relative_time:
        try:
            start_time = self.start_times[frame]
        except KeyError:
            start_time = self.start_times[frame] = \
                datetime_module.datetime.now()
        duration = datetime_module.datetime.now() - start_time
        timestamp = pycompat.timedelta_format(duration)
    else:
        timestamp = pycompat.time_isoformat(
            datetime_module.datetime.now().time(),
            timespec='microseconds'
        )
    #                                                                     #
    ### Finished making timestamp. ########################################

    line_no = frame.f_lineno
    source_path, source = get_path_and_source_from_frame(frame)
    source_path = source_path if not self.normalize else os.path.basename(source_path)
    if self.last_source_path != source_path:
        self.write(u'{_FOREGROUND_YELLOW}{_STYLE_DIM}{indent}Source path:... '
                   u'{_STYLE_NORMAL}{source_path}'
                   u'{_STYLE_RESET_ALL}'.format(**locals()))
        self.last_source_path = source_path
    source_line = source[line_no - 1]
    thread_info = ""
    if self.thread_info:
        if self.normalize:
            raise NotImplementedError("normalize is not supported with "
                                      "thread_info")
        current_thread = threading.current_thread()
        thread_info = "{ident}-{name} ".format(
            ident=current_thread.ident, name=current_thread.getName())
    thread_info = self.set_thread_info_padding(thread_info)

    ### Reporting newish and modified variables: ##########################
    #                                                                     #
    old_local_reprs = self.frame_to_local_reprs.get(frame, {})
    self.frame_to_local_reprs[frame] = local_reprs = \
        get_local_reprs(frame,
                        watch=self.watch, custom_repr=self.custom_repr,
                        max_length=self.max_variable_length,
                        normalize=self.normalize,
                        )

    newish_string = ('Starting var:.. ' if event == 'call' else
                     'New var:....... ')

    for name, value_repr in local_reprs.items():
        if name not in old_local_reprs:
            self.write('{indent}{_FOREGROUND_GREEN}{_STYLE_DIM}'
                       '{newish_string}{_STYLE_NORMAL}{name} = '
                       '{value_repr}{_STYLE_RESET_ALL}'.format(**locals()))
        elif old_local_reprs[name] != value_repr:
            self.write('{indent}{_FOREGROUND_GREEN}{_STYLE_DIM}'
                       'Modified var:.. {_STYLE_NORMAL}{name} = '
                       '{value_repr}{_STYLE_RESET_ALL}'.format(**locals()))

    #                                                                     #
    ### Finished newish and modified variables. ###########################


    ### Dealing with misplaced function definition: #######################
    #                                                                     #
    if event == 'call' and source_line.lstrip().startswith('@'):
        # If a function decorator is found, skip lines until an actual
        # function definition is found.
        for candidate_line_no in itertools.count(line_no):
            try:
                candidate_source_line = source[candidate_line_no - 1]
            except IndexError:
                # End of source file reached without finding a function
                # definition. Fall back to original source line.
                break

            if candidate_source_line.lstrip().startswith('def'):
                # Found the def line!
                line_no = candidate_line_no
                source_line = candidate_source_line
                break
    #                                                                     #
    ### Finished dealing with misplaced function definition. ##############

    # If a call ends due to an exception, we still get a 'return' event
    # with arg = None. This seems to be the only way to tell the difference
    # https://stackoverflow.com/a/12800909/2482744
    code_byte = frame.f_code.co_code[frame.f_lasti]
    if not isinstance(code_byte, int):
        code_byte = ord(code_byte)
    ended_by_exception = (
            event == 'return'
            and arg is None
            and (opcode.opname[code_byte]
                 not in ('RETURN_VALUE', 'YIELD_VALUE'))
    )

    if ended_by_exception:
        self.write('{_FOREGROUND_RED}{indent}Call ended by exception{_STYLE_RESET_ALL}'.
                   format(**locals()))
    else:
        self.write(u'{indent}{_STYLE_DIM}{timestamp} {thread_info}{event:9} '
                   u'{line_no:4}{_STYLE_RESET_ALL} {source_line}'.format(**locals()))

    if event == 'return':
        self.frame_to_local_reprs.pop(frame, None)
        self.start_times.pop(frame, None)
        thread_global.depth -= 1

        if not ended_by_exception:
            return_value_repr = utils.get_shortish_repr(arg,
                                                        custom_repr=self.custom_repr,
                                                        max_length=self.max_variable_length,
                                                        normalize=self.normalize,
                                                        )
            self.write('{indent}{_FOREGROUND_CYAN}{_STYLE_DIM}'
                       'Return value:.. {_STYLE_NORMAL}{return_value_repr}'
                       '{_STYLE_RESET_ALL}'.
                       format(**locals()))

    if event == 'exception':
        exception = '\n'.join(traceback.format_exception_only(*arg[:2])).strip()
        if self.max_variable_length:
            exception = utils.truncate(exception, self.max_variable_length)
        self.write('{indent}{_FOREGROUND_RED}Exception:..... '
                   '{_STYLE_BRIGHT}{exception}'
                   '{_STYLE_RESET_ALL}'.format(**locals()))

    return self.trace