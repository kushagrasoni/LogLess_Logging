from logless.event import Event


class TestLogOutput:

    def test_add_event_method(self, log_generator):
        """
        Tests to add Events to the logs
        """
        event1 = Event('line', 'Initializing Variable', 'var', 'ABC', 'INFO')
        event2 = Event('call', 'Starting Variable', 'start', '123', 'INFO')
        event3 = Event('line', 'Updated Variable', 'var', 'XYZ', 'INFO')

        expected_events_list = [event1, event2, event3]

        log_generator.add_event(event1)
        log_generator.add_event(event2)
        log_generator.add_event(event3)

        assert expected_events_list == log_generator.events
