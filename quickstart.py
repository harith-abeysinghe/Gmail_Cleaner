from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']


def generate_token_file():
    creds = None

    try:
        # Load existing credentials from token.json if it exists
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        # If there are no (valid) credentials available, initiate the authentication flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds

    except Exception as e:
        print(f'An error occurred during authentication: {str(e)}')
        return None

def read_emails():
    creds = generate_token_file()
    try:
        # Call the Gmail API with a query to filter emails
        service = build('gmail', 'v1', credentials=creds)

        # Define multiple keywords to search for
        keywords = [""]  # Add keywords

        # Create a query that uses the OR operator for multiple keywords
        query = " OR ".join(f"subject:{keyword}" for keyword in keywords)
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])

        if not messages:
            print('No emails found with the specified keyword.')
            return

        print('Emails with the specified keyword:')
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            subject = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'Subject'][0]
            print(f'Subject: {subject}')


    except HttpError as error:
        print(f'An error occurred: {error}')


def delete_emails_with_keyword(keyword):
    creds = generate_token_file()
    try:
        # Call the Gmail API with a query to filter emails
        service = build('gmail', 'v1', credentials=creds)
        query = f"subject:{keyword}"  # Use the specified keyword

        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])

        if not messages:
            print(f'No emails found with the keyword: {keyword}')
            return

        print(f'Deleting emails with the keyword: {keyword}')

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            subject = [header['value'] for header in msg['payload']['headers'] if header['name'] == 'Subject'][0]
            print(f'Deleting Subject: {subject}')
            # Delete each email
            service.users().messages().delete(userId='me', id=message['id']).execute()


    except HttpError as error:
        print(f'An error occurred: {error}')


read_emails()
delete_emails_with_keyword("udemy")
