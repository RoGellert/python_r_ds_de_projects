from faker import Faker
import random
fake = Faker()


def fake_movies(number_of_entries):
    movie_add = ""

    for _ in range(number_of_entries):
        movie_num = random.randrange(1, 5)
        match movie_num:
            case 1:
                movie_add = "'s film"
            case 2:
                movie_add = "'s movie"
            case 3:
                movie_add = "'s debut"
            case 4:
                movie_add = "'s art house"
        movie_name = fake.name() + movie_add

        rating = ""
        rating_num = random.randrange(1, 4)
        match rating_num:
            case 1:
                rating = "PG 13"
            case 2:
                rating = "R"
            case 3:
                rating = "G"

        print(f"('{movie_name}','{fake.date()}', {round(random.uniform(40, 70), 2)}, '{rating}', "
              f"{round(random.uniform(1, 5), 1)}),")


def fake_users(number_of_entries):
    for _ in range(number_of_entries):
        name_surname = fake.name()
        name_surname = name_surname.split()
        name, surname = name_surname[0], name_surname[1]
        print(f"('{name}', '{surname}', '{fake.email()}', '{fake.date()}'),")


if __name__ == "__main__":
    # fake_users(100)
    fake_movies(100)
