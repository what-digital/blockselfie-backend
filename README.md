# Project

Built on top of:
* Python 3
* Django

## Development / Local

### Installation

```
virtualenv .venv -p python3
source .venv/bin/activate
pip install -r requirements.txt
```

#### Environment

Create `.env` file based on the delivered example:
```
cp .example-env .env
```

add this in your virtualenv's postactivate:

```
#!/bin/bash
# This hook is sourced after this virtualenv is activated.

if [ -f ${PWD}/.env ]; then
    echo "activating .env..."
    set -a
    . ${PWD}/.env
    set +a
fi
```

On `workon <project>` it will source `.env` automagically.

Change `DJANGO_DEBUG` value to `True` for local setup.




## Deployment

- A superuser is created for you with a migration. (tech@what.digital with password 'tech@what.digital'). Please dont forget to delete it on production instances.

