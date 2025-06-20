import requests

# Replace with your login URL
login_url = 'https://example.com/login'

# Replace with your actual credentials
payload = {
    'username': 'your_username',
    'password': 'your_password'
}

# Create a session to persist cookies
session = requests.Session()

# Post the login request
response = session.post(login_url, data=payload)

# Check if login was successful
if response.ok:
    print("Login successful!")
    # Access a protected page
    protected_url = 'https://example.com/dashboard'
    protected_page = session.get(protected_url)
    print(protected_page.text)
else:
    print("Login failed!")

