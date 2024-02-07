from faker import Faker
import random
fake = Faker()


def fake_movies(number_of_entries):
    for _ in range(number_of_entries):
        rand_int = random.randrange(0, 100)
        print(f"(''),")


def fake_users(number_of_entries):
    for _ in range(number_of_entries):
        name_surname = fake.name()
        name_surname = name_surname.split()
        name, surname = name_surname[0], name_surname[1]
        print(f"('{name}', '{surname}', '{fake.email()}', '{fake.date()}'),")


if __name__ == "__main__":
    # fake_users(100)
    fake_movies(100)