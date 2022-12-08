from fpdf import FPDF
from logless.profile import Profile
from conf.config import MODE_CONFIG, INFO, ERROR
import json
from logless import logger


class Generator:
    def __init__(self, mode=None, file_type=None):
        self.profiles = []
        self.logger = logger
        self.mode = mode
        self.file_type = file_type
        self.mode_config = self.get_mode_config()
        self.low_frequency = ["exception", "line"]
        self.medium_frequency = ["exception", "line", "return"]
        self.high_frequency = ["exception", "line", "return", "call"]

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
            if profile.level in self.mode_config.get("SUPPORTED_LOG_LEVELS") and self.allow_event_by_frequency(profile.event_type):
                if profile.level == INFO:
                    self.logger.info(profile.with_colors(self.mode_config.get("LOG_VALUES")))
                elif profile.level == ERROR:
                    self.logger.error(profile.without_colors(self.mode_config.get("LOG_VALUES")))


    def print_to_pdf(self):
        # open temporary file in append mode to store this session's logs
        with open("logless.txt","a") as session_state:
            for profile in self.profiles:
                if profile.level in self.mode_config.get("SUPPORTED_LOG_LEVELS") and self.allow_event_by_frequency(profile.event_type):
                    profile_dict = profile.profile_to_dict(self.mode_config.get("LOG_VALUES"))
                    # write each profile_dict object as a new line in the temp file
                    session_state.write(json.dumps(profile_dict) + '\n')

        # re-open temporary file in read mode
        # reads the profile_dicts written above, 
        # as well as any profiles saved from previous calls to this function
    
        # create new pdf object
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=20)
        pdf.cell(200, 10, txt="LogLess", ln=1, align='C')

        # read all profiles from temporary session state
        with open("logless.txt","r") as session_state:
            lines = session_state.readlines()
            profile_dicts = [json.loads(x) for x in lines]
            for profile_dict in profile_dicts:
                # write color-coded profile attributes to file
                pdf.set_text_color(3,37,126) #blue
                pdf.write(10, txt = profile_dict['event_type']+' ')
                pdf.set_text_color(128,49,167) #purple
                pdf.write(10, txt = profile_dict['assign_type']+' ')
                pdf.set_text_color(215,107,0) #orange
                pdf.write(10, txt = profile_dict['var_name']+' ')
                pdf.set_text_color(0,110,51) #green
                pdf.write(10, txt = profile_dict['var_value']+' ')
                pdf.ln()
        
        # save pdf file with current state
        pdf.output("logless.pdf") 

        #file name and file path version 
        #pdf.output(name = f'{self.file_path}/{self.file_name}.pdf', dest='F') 
          


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

    def allow_event_by_frequency(self, event_type) -> bool:
        """
        Checks if the tracing event type is supported in the frequency category, which is determined by the configured
        frequency value
        """
        frequency_value = self.mode_config.get("FREQUENCY")
        if not frequency_value or frequency_value not in [1, 2, 3]:
            frequency_value = 1
        if frequency_value == 1:
            return event_type in self.low_frequency
        elif frequency_value == 2:
            return event_type in self.medium_frequency
        elif frequency_value == 3:
            return event_type in self.high_frequency
