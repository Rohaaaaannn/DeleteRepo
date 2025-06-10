import requests

# Replace with your GitHub username and Personal Access Token
GITHUB_USERNAME = "Your Username"
GITHUB_TOKEN = "PAT"

API_URL = f"https://api.github.com/user/repos"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Parameters: fetch 100 repos per page
params = {
    "visibility": "all",
    "affiliation": "owner",
    "per_page": 100,
    "page": 1
}

repo_list = []

print("🔄 Fetching repositories...")
while True:
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch repos. Status Code: {response.status_code}")
        break

    repos = response.json()
    if not repos:
        break  # No more repos

    for repo in repos:
        full_name = repo['full_name']  # format: username/repo-name
        repo_list.append(full_name)

    params["page"] += 1

# Save to repos.txt
with open("repos.txt", "w") as f:
    for repo in repo_list:
        f.write(repo + "\n")

print(f"Saved {len(repo_list)} repositories to repos.txt")
