---

# Gmail Email Reader & Mark as Read Script

This Python script connects to your Gmail account, finds unread emails, and marks them as read except those from specified email addresses. It’s ideal for keeping your inbox organized and for those who want to filter out certain emails while automatically marking others as read.

## Features
- Connects securely to your Gmail account
- Marks unread emails as read
- Excludes specific emails you choose (by sender's email address)
- Runs automatically every 2 seconds to keep your inbox updated

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Script Customization](#script-customization)
4. [Running the Script](#running-the-script)
5. [Troubleshooting](#troubleshooting)

---

### Prerequisites

Before running this script, ensure you have:
- Python installed on your computer ([Download Python](https://www.python.org/downloads/))
- A Google Cloud project with access to the Gmail API (follow steps below)

### 1. Setting Up the Gmail API
1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Click **Create Project**, name your project, and click **Create**.
   
2. **Enable Gmail API**:
   - In your project dashboard, go to **Library**.
   - Search for **Gmail API**, click on it, and then click **Enable**.

3. **Set Up OAuth Credentials**:
   - Do this if you understand or else just use my cred i dont care to be honest
   - In the left sidebar, go to **Credentials**.
   - Click **Create Credentials** and select **OAuth client ID**.
   - Configure the consent screen by adding an App name, support email, etc.
   - Once done, choose **Desktop App** as the Application Type and click **Create**.
   - Click **Download JSON** to save your credentials file as `credentials.json` (keep this file in the same folder as your script).

---

### 2. Getting Started

1. **Clone or Download the Script**:
   - Place this script and your `credentials.json` file in the same directory.

2. **Install Required Python Libraries**:
   - Open your command line or terminal.
   - Run the following command to install the necessary libraries:
     ```bash
     pip install google-auth
     ```
     ```bash
     pip install google-auth-oauthlib
     ```
     ```bash
     pip install google-auth-httplib2
     ```
     ```bash
     pip install google-api-python-client
     ```

### 3. Script Customization

- Open the script file (`gmail_email_reader.py`) in any text editor.
- In the `except_emails` list, replace `'example@gmail.com'` and `'secondexample@gmail.com'` with the email addresses you want to **exclude** from being marked as read:
  ```python
  except_emails = ['email_to_exclude1@gmail.com', 'email_to_exclude2@gmail.com']
  ```
  
### 4. Running the Script

1. **Run the Script**:
   - Open a command line in the folder where the script is located.
   - Run the following command:
     ```bash
     python gmail_email_reader.py
     ```
2. **Authorize the Script**:
   - The first time you run the script, a new browser window will open asking you to log in and give the app permission to access your Gmail.
   - Once authorized, the script will start running, and it will mark emails as read every 2 seconds.

---

### Troubleshooting

**If the Script Asks for Authorization Every Time**:
- In the script, ensure the `token.pickle` file isn’t being deleted (it saves your login session).
  - Comment out these lines:
    ```python
    # if os.path.exists('token.pickle'):
    #     os.remove('token.pickle')
    ```
**Common Errors**:
- If you encounter errors, check that:
  - Your `credentials.json` file is in the correct folder.
  - Gmail API is enabled.
  - Required Python libraries are installed.

**Error: File Not Found**:
- Make sure your `credentials.json` file is in the same folder as the script.

---

### Notes
This script runs continuously and checks for new emails every 2 seconds. To stop the script, simply close the command line or press `CTRL+C` on your keyboard.

---

### Disclaimer
Use this script responsibly. Marking emails as read means you might miss important notifications. Always double-check your exception list to ensure critical emails aren't automatically marked as read.

---
