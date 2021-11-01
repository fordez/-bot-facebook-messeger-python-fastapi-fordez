from googleapiclient.discovery import build
from google.oauth2 import service_account

SHEETS_KEYS = 'sheet_keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1honsjXD0qIiF50-KDjDFFpw79Wa_-nbXPE4yUEdj0WY'
RANGE_NAME = 'Productos!A1:C2'

credentials = service_account.Credentials.from_service_account_file(
    SHEETS_KEYS, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])
print(result)
