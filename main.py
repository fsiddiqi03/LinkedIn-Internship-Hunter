import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()



scopes = {
    os.getenv('SCOPE')
}