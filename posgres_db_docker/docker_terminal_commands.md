### Docker teminal commands

Pulling postgres image: ```docker pull postgres```

Running postgres container: ```docker run --name postgres-db -e POSTGRES_PASSWORD=pass -d postgres```

Creating the db in container: ```docker exec -u postgres postgres-db createdb postgres-db```

Connecting to db in container: ```docker exec -it postgres-db psql -U postgres -d postgres-db```