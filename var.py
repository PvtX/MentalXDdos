import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "21559899"))
    API_HASH = os.getenv("API_HASH", "5ea4f771002450f709f0d5ff5a9b42b0")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7124043863:AAFP7Qi_fqGn6GF2Ugx0DrowuPt7WvMmJ6s")
    sudo = os.getenv("SUDO", "6079943111")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)
