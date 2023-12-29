from faker import Faker
import pandas

if __name__ == "__main__":
    fake_generator = Faker()
    num_of_fake_profiles = 10000

    data = []
    for i in range(num_of_fake_profiles):
        if i % 1000 == 0:
            print(i)
        data.append(fake_generator.profile())

    df = pandas.DataFrame(data)
    df.to_csv("./fake_data", index=False, index_label=False)
