# Backend Course

## Entity Relationship Diagram

After understanding the business rules, one of the next steps for the design of a backend application is the design of the data structure that will contain the persistent information of the system. In this case it has been decided to use a relational database. You can see the Entity Relationship Diagram below.

![ERD Diagram](./documentation/ERD.png)

You can also refer to the Hand-on Database ERD video, which explains the making of this diagram.

[Hand-on Database ERD](https://www.notion.so/ioet/Hands-on-Database-ERD-9118e93dffee48f69e987968f7fa350d)

## App structure

```Txt
📦backend
 ┣ 📂adapters
 ┃ ┣ 📂src
 ┃ ┗ 📂tests
 ┣ 📂api
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂dtos
 ┃ ┃ ┗ 📂routes
 ┃ ┗ 📂tests
 ┣ 📂app
 ┃ ┣ 📂src
 ┃ ┗ 📂tests
 ┣ 📂docs
 ┣ 📂factories
 ┃ ┣ 📂config
 ┃ ┣ 📂repositories
 ┃ ┗ 📂use_cases
 ┗ 📂infrastructure
   ┣ 📂docker
   ┗ 📂postgres-data
```

## Branch Naming strategy

You must base your new branch with the main branch. The new branch should start with 'backend/' followed by your name, and finally a '-' (dash) adn the feature tat you worked on.
```
backend/MyName-the-new-feature
```
Example:
```
backend/JuanPerez-product-create-endpoint
```

## How to Start
### Requirements
* Python 3.10.12 or newer
* Docker

### Environment variables
You must create a .env file, you can use the file .env.example as a reference to do that.

Then replace the values inside brackets ({} and the brackets) with the conection parameters for the Docker PostgreSQL database.

By default the following values are defined in the docker compose file.
```
user: root
password: toor
database: ioet_catalog_db
```

### First steps

This project contains several make scripts located inside of the Makefile.

To initialize your environment you can run one of the following commands:

In case of using Mac or Linux:
```
make create_dev_env
```

In case of using Mac or Linux:
```
make win_create_dev_env
```

The next step is to create the docker instance for the PostgreSQL database.
```
make build
```

You must use the following two commands every time you run the code.

First you start the docker instance.
```
make up
```

And then use the following command to start the python code.

If you use mac or linux
```
make start
```

If you use windows
```
make win_start
```

Once the app ir running you can access the the self documented API endpoint in the next URL: http://localhost:8000/docs/
