import requests
import base64
import os
import json

# Configuration
GITHUB_USERNAME = "saisreekar22"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Set your PAT in environment
OUTPUT_FILE = "projects.json"  # Store project data

def fetch_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch repos: {response.status_code}")
    return response.json()

def fetch_readme(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/readme"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")
        return content
    return "No README found."

def main():
    repos = fetch_repos()
    projects = []
    for repo in repos:
        if repo["name"] != f"{GITHUB_USERNAME}.github.io":  # Skip portfolio repo
            readme = fetch_readme(repo["name"])
            projects.append({
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"] or "No description",
                "readme": readme
            })
    with open(OUTPUT_FILE, "w") as f:
        json.dump(projects, f, indent=2)
    print(f"Project data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()