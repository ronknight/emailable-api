import os
import csv
import logging
import sys
from dotenv import load_dotenv
import requests
import glob

# Configure logging
logging.basicConfig(filename='api.log', level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('API_KEY')

# Define the base URL
base_url = "https://api.emailable.com/v1/batch"

# Function to read email addresses from 'Email' column in CSV file
def read_emails_from_csv(csv_file):
    emails = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first line (header)
        for row in reader:
            email = row[11]  # Assuming 'Email' is in the 12th column (index 11)
            if email:
                emails.append(email)
    return emails

def create_batch(emails):
    # Construct the URL
    url = f"{base_url}?api_key={api_key}"

    # Set the payload
    payload = {
        "emails": emails
    }

    # Set the headers
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request
        response = requests.post(url, json=payload, headers=headers)

        # Log the response status code and text
        logging.info(f"Response status code: {response.status_code}")
        logging.info(f"Response text: {response.text}")
    except Exception as e:
        # Log any exceptions that occur
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Auto-detect CSV file in the current directory
    csv_files = glob.glob("*.csv")

    if not csv_files:
        print("Error: No CSV files found in the current directory.")
        sys.exit(1)

    # Choose the first CSV file found
    csv_file = csv_files[0]

    # Read email addresses from 'Email' column in CSV file
    emails = read_emails_from_csv(csv_file)

    # Create batch with the email addresses
    create_batch(emails)
