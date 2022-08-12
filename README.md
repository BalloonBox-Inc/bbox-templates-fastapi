## This Repo

This GitHub repo contains the template to initiate a project using FastAPI and Heroku with the use of an external database.

## How to use

- create your project repo
- clone the repo into it
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

Run the following command to install dependencies:

```
pip install -r requirements.txt
```

### Credentials

Create a `.env` file with the following:

```
ADMIN_TOKEN = your_admin_token
DATABASE_URI = your_database_uri
```
