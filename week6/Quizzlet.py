def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct_count = 0
    total = len(translations)

    for english, spanish in translations.items():
        user_input = input(f"What is the Spanish translation for {english}? ").strip().lower() 
        if user_input == spanish:
            print("That is correct!\n")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.\n")
     
    print(f"You got {correct_count}/{total} words correct, come study again soon!")

if __name__ == '__main__':
    main()
