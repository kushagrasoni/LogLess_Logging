# from fpdf import FPDF
from logless.profile import Profile
from conf.config import MODE_CONFIG, INFO, ERROR
from logless import logger


class Generator:
    def __init__(self, mode=None, file_type=None):
        self.profiles = []
        self.logger = logger
        self.mode = mode
        self.file_type = file_type
        self.mode_config = self.get_mode_config()

    def add_profile(self, profile: Profile):
        self.profiles.append(profile)

    def print_to_terminal(self):
        for profile in self.profiles:
            print(profile.with_colors(self.mode_config.get("LOG_VALUES")))

    def print_to_txt(self, filename):
        with open(filename, 'a') as f:
            for profile in self.profiles:
                f.write(f'{profile.without_colors(self.mode_config.get("LOG_VALUES"))}\n')

    def log(self):
        for profile in self.profiles:
            if profile.level in self.mode_config.get("SUPPORTED_LOG_LEVELS"):
                if profile.level == INFO:
                    self.logger.info(profile.with_colors(self.mode_config.get("LOG_VALUES")))
                elif profile.level == ERROR:
                    self.logger.error(profile.without_colors(self.mode_config.get("LOG_VALUES")))

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
