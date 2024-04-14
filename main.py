import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()


scopes = [os.getenv('SCOPE')]

creds = Credentials.from_service_account_file("creds.json", scopes=scopes)
client = gspread.authorize(creds)


# Open the Google Sheet by ID and get the spread sheet
sheet = client.open_by_key(os.getenv('SHEET_ID')).sheet1  

jobs = [
    {
        "company": "Microsoft",
        "job_title": "Product Management: Intern Opportunities for University Students",
        "location": "New York, NY",
        "job_url": "https://www.linkedin.com/jobs/view/product-management-intern-opportunities-for-university-students-at-microsoft-3203330682"
    },
    {
        "company": "Microsoft",
        "job_title": "Content Strategist",
        "location": "United States",
        "job_url": "https://www.linkedin.com/jobs/view/content-strategist-at-microsoft-3257692764"
    }
]

# Prepare data for insertion
values = [[job['company'], job['job_title'], job['location'], job['job_url'], 'Need To Apply'] for job in jobs]

# Append data into the sheet
sheet.append_rows(values)  
