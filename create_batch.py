import csv
import logging
import sys
from dotenv import load_dotenv
import requests
import os

# Configure logging
logging.basicConfig(filename='email_verification.log', level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('API_KEY')

# Function to read email addresses from 'Email' column in CSV file
def read_emails_from_csv(csv_file):
    """
    This function reads a CSV file and extracts email addresses and names from it.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary contains an email address and a name.
    """
    emails = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first line (labels)
        for row in reader:
            email = row[0]  # Email is the first column
            name = row[1] if len(row) > 1 else None  # Name is the second column (if available)
            emails.append({"email": email, "name": name})
    return emails

def create_batch(emails):
    """
    This function creates a batch of email addresses for verification using the Emailable API.

    Args:
        emails (list): A list of dictionaries, where each dictionary contains an email address and a name.
    """
    # Define the base URL
    base_url = "https://api.emailable.com/v1/batch"

    # Construct the URL
    url = f"{base_url}?api_key={api_key}"

    payload = {
        "emails": [email["email"] for email in emails]
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

        # Parse response JSON
        response_json = response.json()

        # Extract and print batch ID
        if "id" in response_json:
            batch_id = response_json["id"]
            print(f"Batch email verification request completed: Please run the following command to check status.\npython check_status.py {batch_id}")

    except Exception as e:
        # Log any exceptions that occur
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Check if CSV file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file>")
        sys.exit(1)

    # Get CSV file name from command-line argument
    csv_file = sys.argv[1]

    # Read email addresses from CSV file
    emails = read_emails_from_csv(csv_file)

    # Create batch with the email addresses
    create_batch(emails)