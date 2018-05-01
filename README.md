# Alted

**Cryptocurrency signals and statistics**

This project is in the alpha stage. Things will break and change a lot.

## Features

- Collecting and normalizing data from exchanges
- Custom signals based on coin/market price

##### In progress

- Price charts
- Telegram/Slack/browser/email signal notifications
- Indicator-based signals

### Supported exchanges

| Code | Name | Couuntries |
| --- | --- | --- |
| BITM | Bitmarket | Poland |
| PLNX | Poloniex | US |
| BTRX | Bittrex | US |
| BITMS | Bitmaszyna | Poland |
| BITB | BitBay | Poland |


- Bitmarket
- Bittrex
- Poloniex

## Tools used

- [Cookiecutter Django](https://github.com/pydanny/cookiecutter-django) - Initial project structure

Backend:

- Python
- Django
- Django REST Framework
- [django-allauth](https://github.com/pennersr/django-allauth)
- Celery

Frontend:

- Javascript
- React
- React Autosuggest
- Redux
- Redux Form
- D3
- SASS
- [Material Design Lite](https://getmdl.io/)

Deployment:

- Docker
- Docker Compose
- Rancher
- CircleCI

## Project Structure

[alted/static] - Static files source

[alted/static/pages] - Each page HTML source

[static] - Ready to deploy static files

[alted/taskapp] - Celery tasks root

[config/settings] - Django settings

#### React roots

| Name | Url | Root Directory |
| --- | --- | --- |
| Coin Detail | /coin/\<slug>/ | [alted/static/coins/coin_detail] |
| Market Detail | /market/\<slug>/ | [alted/static/markets/market_detail] |
| Signal List | /signals/ | [alted/static/signals/signal_list] |
| Signal Detail | /signal/\<id>/ | [alted/signals/signal_detail] |

## Local instance

Requirements:
- Docker
- docker-compose
- Node.js and npm

Instalation:

1. Clone Alted and make it your working directory

    `
    git clone https://github.com/fsdevio/alted.git && cd alted
    `

2. Build it and run with configuration for local instance.

    `
    docker-compose -f local.yml up
    `

3. Populate the database with initial data from exchanges APIs.
    
    `
    docker-compose -f local.yml run django python manage.py initialize
    `

4. Install Frontend packages
    
    `
    npm install
    `

5. Run webpack server in development mode

    `
    npm test
    `

Open `http://127.0.0.1:8000/` to access the website.

Default admin username is `admin@mail.com` and password `pass`.

## Authors

- **Kamil Moczydłowski** - [fsdev.io](https://fsdev.io)

## License

This project is licensed under the AGPL License. If you want to deploy a modified version of this application you have to make it open source. See the [LICENSE.md](LICENSE.md) file for details
