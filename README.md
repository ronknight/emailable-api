<p><a target="_blank" href="https://app.eraser.io/workspace/ESN7oNzt0MgX2rhjNflR" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Email Verification Tool - emailable-api
This project consists of three Python scripts that allow you to verify email addresses using the Emailable API, check the status of the verification process, and download the results.

## Scripts
### 1. `create_batch.py` 
This script creates a batch of email addresses to be verified using the Emailable API. Here's how it works:

1. It reads email addresses from the 'Email' column of a provided CSV file.
2. It sends a POST request to the Emailable API to create a new batch with the email addresses.
3. It prints the batch ID and instructions for checking the status of the batch.
**Usage**:

```bash
python create_batch.py <csv_file>
```
### 2. `check_status.py` 
This script checks the status of a batch of email verifications on the Emailable API. Here's how it works:

1. It checks if a batch ID is provided as a command-line argument.
2. It sends a GET request to the Emailable API with the batch ID to check the status of the batch.
3. It prints the status message and either waits for 30 seconds (if the batch is still being processed) or prompts you to download the results (if the batch verification is completed).
**Usage**:

```bash
python check_status.py <batch_id>
```
### 3. `get_result.py` 
This script downloads the results of a completed batch of email verifications from the Emailable API. Here's how it works:

1. It checks if a batch ID is provided as a command-line argument.
2. It sends a GET request to the Emailable API with the batch ID to retrieve the batch data.
3. It writes the email verification results (email, reason, and state) to an `output.csv`  file.
4. It logs the API response to a `response.log`  file with a timestamp.
**Usage**:

```bash
python get_result.py <batch_id>
```
## Setup
1. Clone the repository or download the scripts.
2. Create a `.env`  file in the project directory and add the following environment variable:
    - `API_KEY` : Your Emailable API key.
3. Install the required dependencies by running `pip install -r requirements.txt` .
## Usage
1. Run `create_batch.py`  with a CSV file containing email addresses as an argument to create a new batch of email verifications.
2. After running `create_batch.py` , it will print the batch ID. Copy this ID.
3. Run `check_status.py`  with the batch ID as an argument to check the status of the batch.
4. Once the batch verification is completed, run `get_result.py`  with the batch ID as an argument to download the results and save them to `output.csv` .
## Dependencies
This project uses the following Python libraries:

- `requests` : For making HTTP requests to the Emailable API.
- `python-dotenv` : For loading environment variables from a `.env`  file.
- `csv` : For reading and writing CSV files.
These dependencies are listed in the `requirements.txt` file and can be installed using `pip install -r requirements.txt`.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Email Verification Tool - emailable-api-1.eraserdiagram" data-element-id="P7ugdkr9ARMh15Eb3dhmU"><img src="/.eraser/ESN7oNzt0MgX2rhjNflR___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----3eace891d68cdf9c15a8b75004ac1a6e-Email-Verification-Tool---emailable-api.png" alt="" data-element-id="P7ugdkr9ARMh15Eb3dhmU" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/ESN7oNzt0MgX2rhjNflR --->