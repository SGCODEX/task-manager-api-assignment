import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")


def get_repo():
    g = Github(GITHUB_TOKEN)
    return g.get_repo(GITHUB_REPO)


def create_github_issue(title, description):
    try:
        repo = get_repo()

        issue = repo.create_issue(
            title=title,
            body=description
        )

        return str(issue.number)

    except Exception as e:
        print("GitHub issue creation failed:", e)
        return None


def update_github_issue(issue_id, title, description):
    try:
        repo = get_repo()

        issue = repo.get_issue(int(issue_id))
        issue.edit(title=title, body=description)

    except Exception as e:
        print("GitHub issue update failed:", e)


def close_github_issue(issue_id):
    try:
        repo = get_repo()

        issue = repo.get_issue(int(issue_id))
        issue.edit(state="closed")

    except Exception as e:
        print("GitHub issue close failed:", e)
        
# import os
# from github import Github
# from dotenv import load_dotenv

# load_dotenv()

# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# GITHUB_REPO = os.getenv("GITHUB_REPO")

# g = Github(GITHUB_TOKEN)
# repo = g.get_repo(GITHUB_REPO)

# def create_github_issue(title, description):
#     # try:
#     #     issue = repo.create_issue(
#     #         title=title,
#     #         body=description
#     #     )
#     #     return str(issue.number)
#     # except Exception as e:
#     #     print("GitHub issue creation failed:", e)
#         return None
    
# def update_github_issue(issue_id, title, description):
#     # try:
#     #     issue = repo.get_issue(int(issue_id))
#     #     issue.edit(title=title, body=description)
#     # except Exception as e:
#     #     print("GitHub issue update failed:", e)
#     return None


# def close_github_issue(issue_id):
#     # try:
#     #     issue = repo.get_issue(int(issue_id))
#     #     issue.edit(state="closed")
#     # except Exception as e:
#     #     print("GitHub issue close failed:", e)
#     return None