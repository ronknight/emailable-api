import os
import sys
import logging
import json
from dotenv import load_dotenv
import requests

# Configure main logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure response logging
response_logger = logging.getLogger('response')
response_logger.setLevel(logging.INFO)
response_handler = logging.FileHandler('response.log')
response_logger.addHandler(response_handler)

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('API_KEY')

# Define the base URL
base_url = "https://api.emailable.com/v1/batch"

def get_batch(batch_id):
    # Construct the URL with the id parameter
    url = f"{base_url}?id={batch_id}"

    # Set the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
        # Make the GET request
        response = requests.get(url, headers=headers)

        # Log the response status code
        response_logger.info(f"Response status code: {response.status_code}")

        # Prettify and log the response text
        response_text = json.dumps(response.json(), indent=4)
        response_logger.info(f"Response text: \n{response_text}")
    except Exception as e:
        # Log any exceptions that occur
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Check if the batch_id argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <batch_id>")
        sys.exit(1)

    batch_id = sys.argv[1]
    get_batch(batch_id)
