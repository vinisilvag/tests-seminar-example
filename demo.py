from faker import Faker


def main():
    fake = Faker()
    # fake.seed_instance(42)
    # fake = Faker(["pt_BR", "pt_BR"])

    # Basics
    print(fake.name())
    print(fake.address())
    print(fake.email())

    print(fake.url())

    print(fake.ipv4_private())
    print(fake.ipv4_public())

    print(fake.phone_number())

    print(fake.text())

    # More advanced function generation
    for _ in range(5):
        print(fake.bothify(text="????-####-??-##", letters="ABCDEFGH"))

    for _ in range(5):
        print(fake.hexify(text="MAC: ^^:^^:^^:^^:^^:^^", upper=True))

    # Custom providers
    # TODO


if __name__ == "__main__":
    main()
