import os
from pathlib import Path
from dotenv import load_dotenv, set_key, find_dotenv,dotenv_values

PATH = Path('.env')

def load(): return load_dotenv(dotenv_path=PATH)

def change_value(key, value) -> None:
    set_key(key_to_set=key, value_to_set=value, dotenv_path=find_dotenv())
