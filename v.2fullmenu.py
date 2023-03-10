#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API Key Management System

A tool for managing API keys and securing them against attacks such as brute-force attacks and API key leakage.
"""

import openai_secret_manager
import openai
import json

def print_menu():
    print("""
╔══════════════════════════════════════╗
║       portuno api keys by tadash10    ║
╠══════════════════════════════════════╣
║ 1. API Key Management System         ║
║ 2. Create API Key                    ║
║ 3. View All API Keys                 ║
║ 4. View API Key Details              ║
║ 5. Update API Key                    ║
║ 6. Delete API Key                    ║
║ 7. Translation Tool                  ║
║ 8. List Supported Languages          ║
║ 9. Exit                              ║
╚══════════════════════════════════════╝
""")

def create_api_key():
    api_key_name = input("Enter a name for your API key: ")
    new_secret = openai_secret_manager.create_secret()
    api_key = {
        "name": api_key_name,
        "secret_id": new_secret.id
    }
    with open("api_keys.json", "r") as f:
        api_keys = json.load(f)
    api_keys.append(api_key)
    with open("api_keys.json", "w") as f:
        json.dump(api_keys, f, indent=4)
    print(f"API key created successfully. Save the following API key value:\n{new_secret.secret_value}")

def view_all_api_keys():
    with open("api_keys.json", "r") as f:
        api_keys = json.load(f)
    print("All API keys:")
    for index, api_key in enumerate(api_keys):
        print(f"{index+1}. {api_key['name']}")

def view_api_key_details():
    with open("api_keys.json", "r") as f:
        api_keys = json.load(f)
    for index, api_key in enumerate(api_keys):
        print(f"{index+1}. {api_key['name']}")
    api_key_index = int(input("Enter the index of the API key to view details: ")) - 1
    api_key = api_keys[api_key_index]
    secret = openai_secret_manager.get_secret_by_id(api_key['secret_id'])
    print(f"Name: {api_key['name']}")
    print(f"API Key: {secret.secret_value}")

def update_api_key():
    with open("api_keys.json", "r") as f:
        api_keys = json.load(f)
    for index, api_key in enumerate(api_keys):
        print(f"{index+1}. {api_key['name']}")
    api_key_index = int(input("Enter the index of the API key to update: ")) - 1
    api_key = api_keys[api_key_index]
    new_api_key_name = input("Enter a new name for the API key: ")
    api_key['name'] = new_api_key_name
    with open("api_keys.json", "w") as f:
        json.dump(api_keys, f, indent=4)
    print("API key updated successfully.")

def delete_api_key():
    with open("api_keys.json", "r")
