import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()


scopes = {
    os.getenv('SCOPE')
}

creds = Credentials.from_service_account_file("creds.json", scopes=scopes)
client = gspread.authorize(creds)


sheet = client.open_by_key(os.getenv('SHEET_ID'))

values = sheet.sheet1.row_values(1)
print(values)