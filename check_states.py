import requests
import json

# GET
commit_response=requests.get("https://api.github.com/repos/jjpterdh/jjpterdh.github.io/commits")
issue_response=requests.get("https://api.github.com/repos/jjpterdh/jjpterdh.github.io/issues")
pull_response=requests.get("https://api.github.com/repos/jjpterdh/jjpterdh.github.io/pulls")
language_response=requests.get("https://api.github.com/repos/jjpterdh/jjpterdh.github.io/languages")

# commit count
commits=commit_response.content
commits=json.loads(commits)
commit_count=len(commits)

# issue count
issues= issue_response.content
issues=json.loads(issues)
issue_count=len(issues)

# pull count
pulls=pull_response.content
pulls=json.loads(pulls)
pulls_count=len(pulls)

# used language
languages=language_response.content
languages=json.loads(languages)



print(f"Commit Count: {commit_count}")
print(f"Issue Count: {issue_count}")
print(f"Pull Request Count: {pulls_count}")
print(f"Used languages: {languages}")