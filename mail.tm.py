import requests
import random
import string
import time

API = "https://api.mail.tm"

def random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def get_domain():
    resp = requests.get(f"{API}/domains")
    domains = resp.json()["hydra:member"]
    return random.choice(domains)["domain"]

def create_account(email, password):
    resp = requests.post(f"{API}/accounts", json={
        "address": email,
        "password": password
    })
    # Account may already exist, so ignore error here
    return resp.json()

def get_token(email, password):
    resp = requests.post(f"{API}/token", json={
        "address": email,
        "password": password
    })
    return resp.json()["token"]

def check_inbox(token):
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{API}/messages", headers=headers)
   _name = get_domain()
    email = f"{username}@{domain}"
    password = random_name(12)

    print(f"\nTemporary Email Created: {email}")
    print(f"Password: {password}\n")

    create_account(email, password)
    token = get_token(email, password)

    print("Use this email for verification. Checking inbox every 10 seconds...\n(Press Ctrl+C to stop)\n")

    try:
        while True:
            messages = check_inbox(token)
            if messages:
                print(f"\nYou have {len(messages)} message(s):")
                for msg in messages:
                    print(f"From: {msg['from']}, Subject: {msg['subject']}")
                    detail = read_message(token, msg["id"])
                    print par):

1. **Python aur requests install karein:**