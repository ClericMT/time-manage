from datetime import date
from datetime import time
from datetime import datetime

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("MUO Python Sheets") # open sheet


worksheet = sheet.get_worksheet(0)
today = str(date.today())
today_sheet = worksheet.find(today)

language = input("Hours spent on language: ")
language_row = (today_sheet.row)

coding = input("Hours spent on coding: ")
coding_row = (today_sheet.row) + 1

audio = input("Hours spent on audio: ")
audio_row = (today_sheet.row) + 2

visual = input("Hours spent on visual: ")
visual_row = (today_sheet.row) + 3

ecom = input("Hours spent on ecom: ")
ecom_row = (today_sheet.row) + 4


worksheet.update_cell(today_sheet.row, language_row, language)
worksheet.update_cell(today_sheet.row, coding_row, coding)
worksheet.update_cell(today_sheet.row, audio_row, audio)
worksheet.update_cell(today_sheet.row, visual_row, visual)
worksheet.update_cell(today_sheet.row, ecom_row, ecom)
