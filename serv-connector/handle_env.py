from dotenv import load_dotenv, set_key, find_dotenv,dotenv_values


def load(): return load_dotenv()

def change_value(key, value) -> None:
    set_key(key_to_set=key, value_to_set=value, dotenv_path=find_dotenv())
    