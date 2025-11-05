from faker import Faker
from faker.providers import BaseProvider, DynamicProvider


class LLMProvider(BaseProvider):
    def llm(self) -> str:
        return self.random_element(["GPT", "Gemini", "BERT", "PaLM", "Llama", "Claude"])


def main():
    fake = Faker()
    # fake.seed_instance(42)
    # fake = Faker(["pt_BR", "ja_JP"])

    # Basics
    print(fake.name())
    print(fake.address())
    print(fake.email())

    print(fake.url())

    print(fake.ipv4_private())
    print(fake.ipv4_public())

    print(fake.phone_number())

    print(fake.text())

    ## More advanced function generation
    for _ in range(5):
        print(fake.bothify(text="????-####-??-##", letters="ABCDEFGH"))

    for _ in range(5):
        print(fake.hexify(text="MAC: ^^:^^:^^:^^:^^:^^", upper=True))

    my_word_list = [
        "force",
        "jedi",
        "sith",
        "Padawan",
        "lightsaber",
        "Yoda",
        "Stormtrooper",
        "Millennium Falcon",
        "droid",
        "Death Star",
    ]

    print(fake.sentence())
    print(fake.sentence(ext_word_list=my_word_list))

    ## Custom providers
    fake.add_provider(LLMProvider)
    print(fake.llm())

    medical_professions_provider = DynamicProvider(
        provider_name="medical_profession",
        elements=["dr.", "doctor", "nurse", "surgeon", "clerk"],
    )

    fake.add_provider(medical_professions_provider)
    print(fake.medical_profession())

    ## Unique values
    names = [fake.unique.first_name() for _ in range(500)]
    print(names[:8], len(names))
    assert len(set(names)) == len(names)

    # for i in range(3):
    # Raises a UniquenessException
    # fake.unique.boolean()


if __name__ == "__main__":
    main()
