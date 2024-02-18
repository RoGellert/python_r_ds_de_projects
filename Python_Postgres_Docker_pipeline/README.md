### Pipeline between two Postgres Databases (in Docker)

Video form FreeCodeCamp was quite helpful in that regard:
https://www.youtube.com/watch?v=PHsC_t0j1dU&t=9961s

A simple python script to extract data from one Postgres database into the other.

Projects involves creation of three docker containers: two for databases and one for the script.

To execute run ```docker compose up``` from the root folder provider docker is installed and running.
In ```fake_data_get.py``` I was experimenting with fake data creation.
