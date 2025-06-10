import requests

# Replace with your actual GitHub token
GITHUB_TOKEN = "PAT"
API_URL = "https://api.github.com"

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Load repository names
with open("repos.txt", "r") as f:
    repos = [line.strip() for line in f if line.strip()]

# Ask for confirmation once
confirm = input(f"This will delete {len(repos)} repositories. Are you sure? (yes/no): ").lower()

if confirm == "yes":
    for repo in repos:
        url = f"{API_URL}/repos/{repo}"
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print(f"Deleted: {repo}")
        else:
            print(f"Failed to delete {repo}. Status Code: {response.status_code}")
else:
    print("Operation cancelled.")
