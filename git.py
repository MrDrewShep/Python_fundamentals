
"""
#HW https://thegeeksalive.com/how-to-create-a-new-git-repository-and-push-it-to-github/


# From github.com
1. Create new repo, do not initialize with readme.md
2. Copy the repo's url


# From vscode, create the following files
1. readme.md
2. .gitignore
        Directories listed as-is
        Files listed with .[extension]
3. (requirements.txt will be created in powershell)


# From powershell - CREATE, ADD, COMMIT, PUSH
1. Activate virtual environment
        venv_folder/Scripts/activate (windows)
        . venv/bin/active (linux)
2. Save list of package dependancies into a txt document
        pip freeze > requirements.txt
3. Initialize local git repository
        git init
-. As needed, verify if the .git folder is in place)
        dir -Force
-. As needed, status
        git status
4. Add files/directories to the staging area
        git add <what to add>
        git .                   (to include everything in that directory, less .gitignore items)
-. As needed, login
        git config user.email "user@user.com"
        git config user.name "Test User"
        git config --global user.email "user@user.com"          to set it permanently
        git config --global user.name "Test User"               to set it permanently
6. Add the url for, and create "origin" location reference
        git remote add origin https://github.com/MrDrewShep/Python_fundamentals.git
        
5. Commit files from the staging area
        git commit -m "{message goes here}"         (e.g. message = "Initial commit")

            if needed:
                    git remote remove origin
7. Push the commit to the cloud/github
        git push origin master
                where "origin" is the location, where we want to push. this is a key to a dict entry.
                where "master" is what we want to push
                note: adam strongly discourages the use of "-u" in the git push syntax


# From Powershell - CHECKOUT, BRANCH
1. Activate virtual environment
2. Checkout a branch
                git checkout -b dev
                git checkout dev
                -b    if this branch does not exist, create it for me
-. If needed, find out which branch you are on
                git branch
-. If needed, find out which url your branch is assigned to
                git remote show origin


# TO PULL AN UPDATE
1. Pull the update
                git pull origin master




if you get stuck in vim:
    ":q!"   to exit terminal

"""