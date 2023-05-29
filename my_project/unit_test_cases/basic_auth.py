import requests
from selenium import webdriver
from requests.auth import HTTPBasicAuth

username = "admin"
password = "admin"

url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

response = requests.get(url)

if response.status_code == 200:
    print("Authentication successful!")
else:
    print("Authentication failed!")
