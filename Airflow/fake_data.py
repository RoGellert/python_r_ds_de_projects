from faker import Faker

if __name__ == "__main__":
    fake_generator = Faker()

    print(fake_generator.profile())
