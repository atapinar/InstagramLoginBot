# InstagramLoginBot

## Instagram Login Automation Script
This Python script automates the process of logging into Instagram using Selenium WebDriver. It opens a Chrome browser, navigates to Instagram, and logs in using the credentials you provide at runtime.

## Table of Contents
* Features
* Prerequisites
* Installation
* Usage
* Security Considerations
* Notes
* References

## Features
* Automates the login process to Instagram.
* Uses Selenium WebDriver for browser automation.
* Prompts for username and password at runtime for security.
* Handles common post-login pop-ups ("Save Your Login Info", "Turn On Notifications").
* Adds random delays to mimic human behavior.

## Prerequisites
* Python 3.6 or higher installed on your system.
* Google Chrome browser installed.
* pip package manager.

## Installation
1. Clone the Repository

```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```
2. Install Required Packages

Install the necessary Python packages using pip:

```
pip install selenium webdriver-manager
```
## Usage
1. Run the Script

Execute the script from your terminal or command prompt:

```
python instagram_login.py
```
2. Enter Your Credentials

*  When prompted, enter your Instagram username.
*  Enter your Instagram password (the password input will be hidden for security).

3. Observe the Automation

*  The script will open a Chrome browser window.
* It will navigate to Instagram and log in using the provided credentials.
* The browser will remain open for 60 seconds after login for observation.

## Security Considerations

* Password Input: The script uses getpass.getpass() to securely prompt for your password without displaying it on the screen.
* Credentials Storage: No credentials are stored in the script or on disk; they are entered at runtime.
* Privacy: Be cautious when using automation scripts with personal accounts. Ensure you understand Instagram's terms of service.

## Notes

* Selenium WebDriver: Automates browser actions.
* webdriver_manager: Automatically downloads and manages the ChromeDriver binaries.
* Random Delays: Added to mimic human behavior and potentially avoid detection.
* Error Handling: The script includes try-except blocks to handle exceptions and ensure the browser is closed properly.

## References

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [webdriver_manager Documentation](https://pypi.org/project/webdriver-manager/)
- [ChromeDriver Documentation](https://sites.google.com/a/chromium.org/chromedriver/)
- [getpass Module Documentation](https://docs.python.org/3/library/getpass.html)

