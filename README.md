## This Repo

This GitHub repo contains the template to initiate a project using FastAPI and Heroku with the use of external database and JWT security.

## How to use

- create your project repo
- clone the repo into it
- create a virtual environvent
- install dependencies
- set up environment variables
- start building your own project

### Starting

Run the following commands to clone the repo:

```
# clone template to your project directory as a sub-directory
git clone https://github.com/BalloonBox-Inc/bbox-templates-fastapi-heroku.git

# move template content to your project directory (out of the sub-directory)
mv -v bbox-templates-fastapi-heroku/* .

# move hidden file to your project directory (out of the sub-directory)
mv bbox-templates-fastapi-heroku/.github .

# move hidden file to your project directory (out of the sub-directory)
mv bbox-templates-fastapi-heroku/.vscode .

# move hidden file to your project directory (out of the sub-directory)
mv bbox-templates-fastapi-heroku/.gitignore .
```

Delete bbox-templates-fastapi-heroku sub-directory from your project.

### Requirements

Run the following commands to create virtual environment and install dependencies:

```
# create environment
python -m venv venv

# activate environment
source venv/bin/activate

# install packages
pip install -r requirements.txt
```

### Credentials

Create a `.env` file with the following:

```
# Database
DATABASE_URI = your_database_uri

# Security
ACCESS_TOKEN_EXPIRE_MINUTES = time_in_minutes
JWT_SECRET_KEY = jwt_hashing_algorithm
JWT_SECRET_KEY = your_jwt_secret_key (run the following command to generate key: openssl rand -hex 512)
```
