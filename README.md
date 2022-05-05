FastAPI, tortoise-orm, aerich template
======================================


# Set .env and .env.[prod,dev,test]
Then create .env file (or rename and modify .env.example) in project root and
set environment variables for application:
```bash
touch .env
echo APP_ENV=dev
touch .env.dev
echo DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env.dev
echo SECRET_KEY=$(openssl rand -hex 32) >> .env.dev
```

# Prepare development environment
```bash
git clone git@github.com:ada0l/fastapi_tortoise_aerich_template.git
pip install poetry 
poetry install
# activate python environment
poetry shell
```

# Build and run
```bash
docker-compose build
docker-compose up
```

# Run tests
```bash
docker exec -it <name_container_web> /bin/bash
poetry run pytest .
```

# How add models for aerich?

You should add application name to ```backend.core.settings.AppSettings.installed_apps```.

# Related links
 - [FastAPI](https://fastapi.tiangolo.com/)
 - [Tortoise](https://tortoise.github.io/)
 - [Aerich](fastapi_tortoise_aerich_template)
