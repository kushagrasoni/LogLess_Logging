import os
from fpdf import FPDF
from conf.config import MODE_CONFIG, INFO
from dataclasses import dataclass

@dataclass
class Profile:
    event_type: str
    assign_type: str
    var_name: str
    var_value: str
    level: str


