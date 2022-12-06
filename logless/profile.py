

class Profile:
    def __init__(self, event_type, assign_type, var_name, var_value, level):
        self.event_type = event_type
        self.assign_type = assign_type
        self.var_name = var_name
        self.var_value = var_value
        self.level = level
        self.color_map = {'black': "\u001b[30m",
                          'red': "\u001b[31m",
                          'green': "\u001b[32m",
                          'yellow': "\u001b[33m",
                          'blue': "\u001b[34m",
                          'magenta': "\u001b[35m",
                          'cyan': "\u001b[36m",
                          'white': "\u001b[37m",
                          'none': ''
                          }

    def wrap_color(self, text, color):
        return f'{self.color_map[color]}{text}\u001b[0m'

    def with_colors(self, log_values):
        event_type = self.wrap_color(self.event_type, "blue")
        assign_type = self.wrap_color(self.assign_type, "yellow")
        var_name = self.wrap_color(self.var_name, "magenta")
        var_value = self.wrap_color(self.var_value, "green")

        event_str = f'{event_type} {assign_type} {var_name}'

        if log_values:
            event_str += f' with value = {var_value}'
        return event_str

    def without_colors(self, log_values):
        event_str = f'{self.event_type} {self.assign_type} {self.var_name}'

        if log_values:
            event_str += f' with value = {self.var_value}'

        return event_str




