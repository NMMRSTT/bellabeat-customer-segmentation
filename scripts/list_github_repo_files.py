import os
import requests

# Your GitHub repository details
username = 'NMMRSTT'
repository = 'gdac_capstone'
path_to_directory = ''  # Set to the appropriate directory path

# Access the token from the environment variable
token = os.environ.get('GITHUB_ACCESS_TOKEN')

# Construct the API URL
url = f'https://api.github.com/repos/{username}/{repository}/contents/{path_to_directory}'

# Set up the headers with your token for authentication
headers = {
    'Authorization': f'token {token}'
}

# Make a GET request to the GitHub API
response = requests.get(url, headers=headers)

# Check for a successful response
if response.status_code == 200:
    data = response.json()
    # Extract filenames
    filenames = [item['name'] for item in data if 'type' in item and item['type'] == 'file']
    # Print the list of filenames
    for filename in filenames:
        print(filename)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
