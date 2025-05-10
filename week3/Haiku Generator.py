from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    haiku = call_gpt(f"turn the {name} and {topic} into a haiku")
    print(haiku)


if __name__ == "__main__":
    main()