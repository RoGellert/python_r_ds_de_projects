from faker import Faker
fake = Faker()

if __name__ == "__main__":
    number_of_entries = 100
    fake = Faker()

    fake_data = []

    for _ in range(0, number_of_entries):
        fake_data.append([fake.name(), fake.address()])

    print([i for i in fake_data])
