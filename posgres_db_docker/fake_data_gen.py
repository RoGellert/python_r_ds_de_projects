from faker import Faker
fake = Faker()

if __name__ == "__main__":
    number_of_entries = 100
    fake = Faker()

    fake_data = []

    for _ in range(number_of_entries):
        name_surname = fake.name()
        name_surname = name_surname.split()
        name, surname = name_surname[0], name_surname[1]
        print(f"('{name}', '{surname}', '{fake.email()}', '{fake.date()}'),")
