# s.pyderman Web Crawler

Web crawler, also called web spider, is an automated program which searches for and browses web pages of the world wide web. Its job is searching and extracting the data from the web, which is then stored in a database and can be later used in various ways, depending on our goals. The goal of our project was to implement a multithreaded web crawler that would crawl domains ending in _gov.si_.

## Prerequisites

Before running the web crawler, we need to start a Docker container with a Postgre SQL database, which we will use as storage for our web crawler.

To start the container, open the command line tool in the [root folder of the crawler](/pa1/crawler) and run the following command:
```
docker run --name postgresql-wier -e POSTGRES_PASSWORD=SecretPassword -e POSTGRES_USER=user -v $PWD/pgdata:/var/lib/postgresql/data -v $PWD/init-scripts:/docker-entrypoint-initdb.d -p 5432:5432 -d postgres:12.2
```

Then, run the `database.sql` script to intialize the crawldb database with all the necceseary tables and relations.

To check container's logs, run `docker logs -f postgresql-wier`.

To log into the database and execute SQL statements, run the following command: `docker exec -it postgresql-wier psql -U user`.

To have better control over the database, we recommend the use of pgadmin.

## Running the crawler

In order to run the crawler, simply run the `main.py` file. To adjust some of the settings, change the constants inside `project_properties.py`.