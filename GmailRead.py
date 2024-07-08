import os
import pickle
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    #bellow i made 2 lines of code a comment what happens is if you remove them the code will 
    # ask you to relog back into your gmail when it executes again while the comment is on it will work on that same gmail/email all the time


    # if os.path.exists('token.pickle'):
    #     os.remove('token.pickle')

    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def mark_emails_as_read(service, except_emails):
    query = 'is:unread'
    for email in except_emails:
        query += f' -from:{email}'

    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    if not messages:
        print('No unread messages found.')
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            msg_id = msg['id']
            msg_labels = msg['labelIds']

            if 'UNREAD' in msg_labels:
                msg_labels.remove('UNREAD')
                service.users().messages().modify(userId='me', id=msg_id, body={'removeLabelIds': ['UNREAD']}).execute()
                print(f'Marked message with ID {msg_id} as read.')

def main():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    
    except_emails = ['brandonmudau2@gmail.com', 'ndaedzomu101@gmail.com']  # Add all exception emails here
    
    
    while True:
        mark_emails_as_read(service, except_emails)
        print("Waiting for 1 minute before checking again...")
        time.sleep(2)  # Sleep for 2 seconds

if __name__ == '__main__':
    main()
