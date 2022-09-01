## This Repo

This GitHub repo contains the template to initiate an application project using FastAPI. The application follows the principles of Object-oriented programming which aims modularity, reusability, easily upgradable and scalable.

This application also includes:

- External database integration
- API throttling
- API data validation (data type only)
- OAuth2 with password and hashing
- Bearer with JWT tokens
- API testing and Unit testing
- Heroku deployment

## How to use

1. Create your project repo
2. Clone this repo into your project repo
3. Create a virtual environvent
4. Install dependencies (packages)
5. Set up environment variables
6. Customize and start building your own project

### Starting

Run the following commands to clone the repo:

```
# clone template to your project directory as a sub-directory
git clone https://github.com/BalloonBox-Inc/bbox-templates-fastapi.git

# move template content to your project root directory (out of the cloned sub-directory)
mv -v bbox-templates-fastapi/{*,.*} .
```

Delete bbox-templates-fastapi sub-directory from your project.

### Requirements

Run the following commands to create virtual environment and install dependencies:

```
# create environment
python -m venv venv

# activate environment
source venv/bin/activate

# install packages
pip install -r requirements.txt
pip install --upgrade pip setuptools

# install hooks
pre-commit install
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

Learn how to set up environment variables on Github [here](https://adamtheautomator.com/github-actions-environment-variables/#Managing_Environment_Variables_via_GitHub_Actions_environment_variables_and_Secrets). This step is crutial for running tests without crashing.

### Directory Structure

The tree diagram below describes the structure of this Repo. Notice that the decision tree only features the most important files and disregards all others.

```bash
.
└───
    ├── .github
    │   ├── on_pull_request.yaml        # GitHub actions executed whenever a pull request is made
    │   └── on_push.yaml                # GitHub actions executed whenever a push is made
    ├── .vscode
    │   └── settings.json               # VS Code setting preferences
    ├── apis
    │   └── routers.py                  # API routers aggregator
    ├── db
    │   ├── crud.py                     # Create, Read, Update, Delete (CRUD) operations to manage data elements of relational databases
    │   ├── session.py                  # database connection setup
    │   ├── models.py                   # database tables
    │   └── utils.py                    # database connect/disconnect assurance process
    ├── helpers                         # [directory] multiple functions that support the application
    ├── schemas                         # [directory] multiple schemas used to validate received data and reformat it before sending back to the client/browser (http requests/responses)
    ├── security
    │   ├── dependencies.py             # required inejctions (security and authentication) to happen before running an API router
    │   ├── hashing.py                  # encrypting and verifying passwords
    │   └── tokens.py                   # JWT access tokens
    ├── tests
    │   ├── api_tests                   # [directory] multiple API tests: process of checking the functionality, reliability, performance, and security of the programming interfaces
    │   └── unit_tests                  # [directory] multiple Unit tests: process of checking each individual units of source code
    ├── .env                            # project environment variables
    ├── .gitignore                      # files/directories to be ignored by GitHub when commiting code
    ├── .pre-commit-config.yaml         # pre-commit hooks settings
    ├── .flake8                         # Flake8 settings and coding standards on a module-by-module basis
    ├── .pylintrc                       # Pylint settings and coding standards on a module-by-module basis
    ├── config.py                       # project settings
    ├── main.py                         # FastAPI application
    ├── Procfile                        # Heroku commands that are executed by the dyno's app on startup
    ├── README.md                       # this project guide
    └── requirements.txt                # Python libraries, modules, and packages that are used while developing this project
```
