# News

## Running the backend application
### Debug mode
python3 -m flask --app news.py run --debug 
 

## Backend

Built in Python with Flask.

## Setting up the Virtual Environment (only first time)
python3 -m venv .venv

Main reason to use venv is to isolate packages (dependencies)

## Enter the virtual environment
./.venv/Scripts/activate

## Install dependencies
python3 -m pip -r requirements.txt

## List all Python dependencies
pip list


## Submitting a change

### Creating a branch
git checkout -b "branch-name" 

### Staging changes
git add *

### Commit the change
git commit -m "some message"
