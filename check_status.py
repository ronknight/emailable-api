import os
import sys
import requests
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('API_KEY')

# Define the base URL
base_url = "https://api.emailable.com/v1/batch"

def get_batch_status(batch_id, api_key):
    # Construct the URL
    url = f"{base_url}?api_key={api_key}&id={batch_id}"

    try:
        # Make the GET request
        response = requests.get(url)

        # Parse response JSON
        response_json = response.json()

        # Get and print batch status message
        if "message" in response_json:
            message = response_json["message"]
            # print(f"Batch ID: {batch_id}, Message: {message}")
            return message
        else:
            print("Error: Batch status not found in response.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Check if batch ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python get_status.py <batch_id>")
        sys.exit(1)

    # Get batch ID from command-line argument
    batch_id = sys.argv[1]

    # Keep checking status every 30 seconds until verification is completed
    while True:
        status_message = get_batch_status(batch_id, api_key)
        if status_message == "Batch verification completed.":
            print("Batch verification completed.")
            print(f"Please run the following code to download result.\npython get_result.py {batch_id}")
            break
        elif status_message == "Your batch is being processed.":
            print("Your batch is being processed. Checking status again in 30 seconds...")
            time.sleep(30)
        else:
            print("Unknown status message. Exiting.")
            break
