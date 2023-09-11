import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load client credentials from JSON file
credentials = service_account.Credentials.from_service_account_file(
    'client_credentials.json',
    scopes=['https://www.googleapis.com/auth/gmail.modify']
)

# Create a Gmail API client
service = build('gmail', 'v1', credentials=credentials)
print(credentials)
