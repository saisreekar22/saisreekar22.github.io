import json
from ollama import Client
import re
import os

# Configuration
INPUT_FILE = "projects.json"
OUTPUT_FILE = "_data/projects.yml"
OLLAMA_CLIENT = Client(host='http://localhost:11434')

def summarize_readme(readme, project_name):
    prompt = f"""
    Summarize the following README from the GitHub project '{project_name}' into 2-3 concise bullet points suitable for a data science resume or portfolio. Focus on business value, impact, or skills demonstrated (e.g., improved accuracy, optimized processes, used specific tools). Avoid technical jargon unless necessary, and keep each bullet point under 30 words.

    README:
    {readme[:2000]}
    """
    try:
        print(f"Summarizing {project_name}...")
        response = OLLAMA_CLIENT.generate(model="llama3.1", prompt=prompt)
        print(f"Raw response for {project_name}: {response}")
        summary = response["response"].strip()
        bullets = [line.strip() for line in summary.split("\n") if line.strip().startswith("-")]
        return bullets if bullets else ["- No summary generated."]
    except Exception as e:
        print(f"Error summarizing {project_name}: {e}")
        return ["- Summary generation failed."]

def main():
    try:
        with open(INPUT_FILE, "r") as f:
            projects = json.load(f)
    except Exception as e:
        print(f"Error reading {INPUT_FILE}: {e}")
        return

    yml_projects = []
    for project in projects:
        summary = summarize_readme(project["readme"], project["name"])
        yml_projects.append({
            "name": project["name"],
            "url": project["url"],
            "description": project["description"],
            "summary": summary
        })

    # Create _data directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w") as f:
        f.write("projects:\n")
        for project in yml_projects:
            f.write(f"  - name: {project['name']}\n")
            f.write(f"    url: {project['url']}\n")
            f.write(f"    description: {project['description']}\n")
            f.write("    summary:\n")
            for bullet in project["summary"]:
                f.write(f"      - {bullet[2:].strip()}\n")

    print(f"Summaries saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
