## Data Generation

import csv
import random
from datetime import datetime, timedelta
import os
import json
from azure.storage.blob import BlobServiceClient

storage_account_key = "Noy+yooKqRtXDja25c7CZEbOX+URW2PbQXfjust/CpvCmPiTRDh9pYyH2xWSoGZKgvyL5dXPzmu++AStlQYNJg=="
storage_account_name = "onetwentyusersa"
connection_string = "DefaultEndpointsProtocol=https;AccountName=fakedatacsv;AccountKey=Noy+yooKqRtXDja25c7CZEbOX+URW2PbQXfjust/CpvCmPiTRDh9pYyH2xWSoGZKgvyL5dXPzmu++AStlQYNJg==;EndpointSuffix=core.windows.net"
container_name = "user"

# Function to generate random name
def random_name():
    first_names = ["Morgan", "Chris", "Alex", "Jamie", "Abhinav", "Jevi", "Catie", "Kate", "Alen", "Sam", "Tony", "Neha"]
    last_names = ["White", "Green", "Johnson", "Parker", "Patty", "Neil", "Shanon", "Kumar", "Nair", "Mullen", "Garg"]
    return random.choice(first_names) + " " + random.choice(last_names)

# Function to generate random email
def random_email(name):
    name_parts = name.lower().split()
    domains = ["example.com", "test.com", "sample.com", "blog.com", "potron.com", "ireland.com"]
    return '.'.join(name_parts) + "@" + random.choice(domains)

# Function to generate random signup date
def random_signup_date(start_date='2020-01-01', end_date='2024-03-23'):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime('%Y-%m-%d')

# Function to generate random interests
def random_interests():
    interests_list = ["reading", "cooking", "gaming", "technology", "coding", "blockchain", "photography", "travel", "literature", "cricket", "boxing", "painting"]
    return ','.join(random.sample(interests_list, random.randint(1, len(interests_list))))

# Function to generate random interests
def random_interests_for_json():
    interests_list = ["reading", "cooking", "gaming", "technology", "coding", "blockchain", "photography", "travel", "literature", "cricket", "boxing", "painting"]
    return random.sample(interests_list, random.randint(1, len(interests_list)))

def create_csv(number_of_rows):
    # Create directory if it doesn't exist
    if not os.path.exists('csv_data'):
        os.makedirs('csv_data')

    # Generate data and write to CSV
    with open('csv_data/mock_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'email', 'signup_date', 'interests']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(number_of_rows):  # Adjust the range for the number of rows you want
            name = random_name()
            email = random_email(name)
            signup_date = random_signup_date()
            interests = random_interests()
            writer.writerow({'name': name, 'email': email, 'signup_date': signup_date, 'interests': interests})

    print("CSV file 'mock_data.csv' generated successfully.")

def create_json(number_of_rows):
    data = []
    # Create directory if it doesn't exist
    if not os.path.exists('json_data'):
        os.makedirs('json_data')
    for _ in range(number_of_rows):
        name = random_name()
        email = random_email(name)
        signup_date = random_signup_date()
        interests = random_interests_for_json()
        data.append({
            "name": name,
            "email": email,
            "signup_date": signup_date,
            "interests": interests
        })

    # Write data to JSON file
    with open('json_data/mock_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print("JSON file 'mock_data.json' generated successfully in the 'json_data' folder.")

## Uploading CSV file to Azure storage

def uploadToBlobStorage (file_path, file_name):

    blob_service_client = BlobServiceClient.from_connection_string (connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob (data)

    print (f"Uploaded {file_name}.")

create_csv(10)
create_json(10)
uploadToBlobStorage ('/Users/Jevi/Documents/Jevi/Project/db_management_service/csv_data/mock_data.csv', 'user/user_data.csv') #enter local source and blob container destination

