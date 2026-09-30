from game import SUPPORTED_LENGTHS, WordleGame


def choose_length():
    options = "/".join(str(length) for length in SUPPORTED_LENGTHS)
    while True:
        choice = input(f"Choose word length ({options}) or q to quit: ").strip().lower()
        if choice == "q":
            return None
        if choice.isdigit() and int(choice) in SUPPORTED_LENGTHS:
            return int(choice)
        print(f"Please choose one of: {options}.")

if __name__ == "__main__":
    length = choose_length()
    if length is not None:
        WordleGame(length).run()
