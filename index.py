import json
import random
from datetime import datetime, timedelta
import os
import subprocess

path = "./data.json"

def mark_commit(x, y):
    date = datetime.now() - timedelta(days=365) + timedelta(days=1) + timedelta(weeks=x) + timedelta(days=y)
    date_str = date.isoformat()
    
    data = {
        "date": date_str
    }
    
    with open(path, 'w') as file:
        json.dump(data, file)
    
    subprocess.run(["git", "add", path])
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", date_str], env=env)
    subprocess.run(["git", "push"])

def make_commits(n):
    if n == 0:
        return subprocess.run(["git", "push"])
    
    x = random.randint(0, 54)
    y = random.randint(0, 6)
    date = datetime.now() - timedelta(days=365) + timedelta(days=1) + timedelta(weeks=x) + timedelta(days=y)
    date_str = date.isoformat()
    
    data = {
        "date": date_str
    }
    
    print(date_str)
    
    with open(path, 'w') as file:
        json.dump(data, file)
    
    subprocess.run(["git", "add", path])
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", date_str], env=env)
    
    make_commits(n - 1)

make_commits(100)