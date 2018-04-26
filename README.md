# Alted

**Cryptocurrency signals and statistics**

This project is in the alpha stage. Things will break and change a lot.

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

- Install docker and docker-compose

- Find the ID of the postgres container

```
docker ps
```
Image name should contain alted_postgres

- Create a database

```
docker exec -i <container ID> createdv -h postgres -U alted alted -O alted
```

Enter default `pass` password. You can change it in the `local.yml` file.


## Authors

- **Kamil Moczydłowski** - [fsdev.io](https://fsdev.io)

## License

This project is licensed under the AGPL License. If you want to deploy a modified version of this application you have to make it open source. See the [LICENSE.md](LICENSE.md) file for details
