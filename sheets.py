from googleapiclient.discovery import build
from google.oauth2 import service_account

SHEETS_KEYS = 'sheet_keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_file(
    SHEETS_KEYS, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

SPREADSHEET_ID = '1honsjXD0qIiF50-KDjDFFpw79Wa_-nbXPE4yUEdj0WY'
range = 'Menu!A1:B5'


def query_sheets(SPREADSHEET_ID, range):
    query_sheets = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID, range=range).execute()
    return query_sheets


values = query_sheets(SPREADSHEET_ID, range)
print(values)
