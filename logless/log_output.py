# from fpdf import FPDF
from logless.event import Event
from conf.config import MODE_CONFIG, INFO, ERROR
from logless.logger import logger


class LogGenerator:
    def __init__(self, mode=None):
        self.events = []
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
        self.mode = mode
        self.mode_config = self.get_mode_config()
        self.logger = logger

    def wrap_color(self, text, color):
        return f'{self.color_map[color]}{text}\u001b[0m'

    def with_colors(self, event):
        event_type = self.wrap_color(event.event_type, "blue")
        assign_type = self.wrap_color(event.assign_type, "yellow")
        var_name = self.wrap_color(event.var_name, "magenta")
        var_value = self.wrap_color(event.var_value, "green")

        event_str = f'{event_type} {assign_type} {var_name}'

        if self.mode_config.get("LOG_VALUES"):
            event_str += f' with value = {var_value}'
        return event_str

    def without_colors(self, event):
        event_str = f'{event.event_type} {event.assign_type} {event.var_name}'

        if self.mode_config.get("LOG_VALUES"):
            event_str += f' with value = {event.var_value}'

        return event_str

    def add_event(self, event: Event):
        self.events.append(event)

    def print_to_terminal(self):
        for event in self.events:
            print(self.with_colors(event))

    def print_to_txt(self):
        with open('logless.txt', 'a') as f:
            for event in self.events:
                f.write(f'{self.without_colors(event)}\n')

    def log(self):
        for event in self.events:
            if event.level in self.mode_config.get("SUPPORTED_LOG_LEVELS"):
                if event.level == INFO:
                    self.logger.info(self.with_colors(event))
                elif event.level == ERROR:
                    self.logger.error(self.without_colors(event))

    # still in progress
    # def print_to_pdf(self):
    #     pdf = FPDF()
    #     pdf.add_page()
    #     pdf.set_font("Arial", size=20)
    #     pdf.cell(200, 10, txt="LogLess", ln=1, align='C')
    #     pdf.output("logless.pdf")

    def get_mode_config(self):
        """
        Utility function to get environment mode configurations based on environment setting
        """
        # extract environment mode configurations
        # mode_config = MODE_CONFIG.get(os.getenv("LOGGING_MODE"))
        mode_config = MODE_CONFIG.get(self.mode)
        if not mode_config:
            # if env var not set correctly, set safe mode as the default
            mode_config = MODE_CONFIG.get("SAFE")
        # print("Mode config selected: ", mode_config)
        return mode_config
