# Gmail Cleaner

## Introduction
This script utilizes the Gmail API to manage your inbox efficiently by filtering and deleting emails based on specified keywords in the subject line. It includes functionalities to read emails matching specific keywords and delete them.

## Requirements
- Python 3.x
- `google-auth` library
- `google-auth-oauthlib` library
- `google-api-python-client` library

## Setup
1. Clone the repository or download the script files.
2. Install the required dependencies:
    ```bash
    pip install google-auth google-auth-oauthlib google-api-python-client
    ```
3. Obtain the necessary credentials:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project (if you haven't already).
   - Enable the Gmail API for your project.
   - Create OAuth 2.0 credentials.
   - Download the credentials file (`client_credentials.json`) and place it in the same directory as the script.

## Usage
1. Run the script:
    ```bash
    python gmail_cleaner.py
    ```
2. The script will prompt you to authenticate your Google account and authorize access to the Gmail API. Follow the instructions in the terminal.
3. Once authenticated, the script will read emails matching specified keywords and display their subjects.
4. To delete emails with a specific keyword, modify the `delete_emails_with_keyword` function call at the end of the script with your desired keyword(s).
5. Run the script again to delete the emails matching the specified keyword(s).

## Important Notes
- Ensure that you have enabled the Gmail API and obtained the necessary credentials before running the script.
- Be cautious when deleting emails, as this action cannot be undone.
- Use the script responsibly and ensure compliance with Google's usage policies and terms of service.

