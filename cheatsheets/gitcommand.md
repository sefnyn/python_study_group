# Cheat sheet for git command line


## Install git on your machine.
See:  <https://git-scm.com/downloads>


## Create a personal access token:
  Login to Github.com  
  Browse to: <https://github.com/settings/tokens>  
  Generate new token (classic)  
  Select scope:  repo  
  Generate token  
  Copy token  

Now your account can push to a git repo on GitHub.  Paste the token when asked for your password.



## Clone a git repo:
  git clone https://github.com/sefnyn/python_study_group.git


## Show status of local python_study_group repo:
  cd python_study_group  
  git status 

  If local and remote repos are the same, computer will say:  
    On branch main  
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean


## Update your local repo with latest changes on GitHub
  git pull

  Computer will say:  
    Already up to date.

  Or it will try to update your local repo.  


## Create new file in local repo:
  cd python_study_group  
  git pull  
  touch example.txt :memo: **Note:** This command creates a file on Linux but do whatever works on your OS  
  git status  

  Computer will say:  
    On branch main  
    Your branch is up to date with 'origin/main'.  

    Untracked files:  
    (use "git add <file>..." to include in what will be committed)  
  	example.txt  

    nothing added to commit but untracked files present (use "git add" to track)

## Push new file to remote repo on GitHub

  git pull  
  git add example.txt  
  git commit -m "Describe your changes here"  
  git push  
>Enter **GitHub username**  
>Enter **personal access token**  [This is your password]  

