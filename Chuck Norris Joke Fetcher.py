# DSC510
# Programming Assignment Week 9
# Sarah Theriot
# 8/1/2024


import requests


def get_cn_joke():
    """Retrieves a Chuck Norris joke from the Chuck Norris API (only the Science section)."""

    url = "https://api.chucknorris.io/jokes/random?category=science"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        return joke_data["value"]
    except requests.exceptions.HTTPError as e:
        return f"Error retrieving joke: {e}"


def main():
    print("Welcome to the Chuck Norris joke fetcher!")

    while True:
        joke = get_cn_joke()
        print(f"\nHere's your Chuck Norris joke: \n{joke}\n")

        user_input = input("Would you like to get another joke? (y/n): ").strip().lower()

        if user_input == 'y':
            continue
        elif user_input == 'n':
            print("Thanks for using the Chuck Norris joke fetcher!")
            break
        else:
            print("Invalid input. Please try again. Enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
