## This Repo

This GitHub repo contains the template to initiate a project using FastAPI and Heroku with the use of an external database.

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
git clone https://github.com/BalloonBox-Inc/bbox-templates-fastapi-heroku.git
mv -v bbox-templates-fastapi-heroku/* .
mv bbox-templates-fastapi-heroku/.github .
mv bbox-templates-fastapi-heroku/.vscode .
mv bbox-templates-fastapi-heroku/.gitignore .
```

Delete bbox-templates-fastapi-heroku folder from your project.

### Requirements

Run the following commands to create virtual environment and install dependencies:

```
python -m venv venv
source venv/bin/activate
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
