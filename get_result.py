import os
import sys
import json
import csv
import datetime  # Import the datetime module
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('API_KEY')

# Define the base URL
base_url = "https://api.emailable.com/v1/batch"

def get_batch(batch_id):
    """
    This function retrieves the results of a batch email verification request from the Emailable API.

    Args:
        batch_id (str): The ID of the batch.

    The function logs the response from the API and writes the results to a CSV file.
    """
    # Construct the URL with the id parameter
    url = f"{base_url}?id={batch_id}"

    try:
        # Make the GET request
        response = requests.get(url, headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"})

        # Log the response to response.log with timestamp
        with open('response.log', 'a') as log_file:
            log_file.write(f"[{datetime.datetime.now()}] \nResponse status code: {response.status_code}\n")
            log_file.write("[{datetime.datetime.now()}] Response text:\n")
            log_file.write(json.dumps(response.json(), indent=4))
            log_file.write("\n\n")

        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Write to output.csv
            with open('output.csv', 'w', newline='') as csvfile:
                fieldnames = ['email', 'reason', 'state']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for email_info in data.get('emails', []):
                    writer.writerow({
                        'email': email_info.get('email', ''),
                        'reason': email_info.get('reason', ''),
                        'state': email_info.get('state', '')
                    })

            print("Output written to output.csv")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        # Log any exceptions that occur
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    """
    This script retrieves the results of a batch email verification request from the Emailable API.
    It logs the response from the API and writes the results to a CSV file.
    """
    # Check if the batch_id argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <batch_id>")
        sys.exit(1)

    batch_id = sys.argv[1]
    get_batch(batch_id)