import os

# Translation dictionary mapping each letter to its corresponding number
translation_dict = {
    'A': 1, 'N': 2, 'B': 3, 'O': 4, 'C': 5, 'P': 6,
    'D': 7, 'Q': 8, 'E': 9, 'R': 10, 'F': 11, 'S': 12,
    'G': 13, 'T': 14, 'H': 15, 'U': 16, 'I': 17, 'V': 18,
    'J': 19, 'W': 20, 'K': 21, 'X': 22, 'L': 23, 'Y': 24,
    'M': 25, 'Z': 26
}

# Reverse dictionary for number to letter translation
reverse_translation_dict = {v: k for k, v in translation_dict.items()}


# Function to translate a word into a series of numbers based on the dictionary
def translate_to_numbers(word):
    # Initialize an empty list to hold the translated numbers
    numbers = []

    # Iterate through each character in the word
    for char in word.upper():  # Convert character to uppercase to match dictionary keys
        # Check if the character is in the translation dictionary
        if char in translation_dict:
            # Append the corresponding number to the numbers list
            numbers.append(str(translation_dict[char]))
        else:
            # Append a '?' if the character is not found in the dictionary (handles unknown characters)
            numbers.append('?')

    # Join the list of numbers into a single string with spaces between them
    return ' '.join(numbers)


# Function to translate a series of numbers back into a word
def translate_to_word(numbers):
    # Split the numbers string into a list of individual numbers
    number_list = numbers.split()

    # Initialize an empty list to hold the translated letters
    letters = []

    # Iterate through each number in the list
    for num in number_list:
        # Convert the number string to an integer
        num_int = int(num)

        # Check if the number is in the reverse translation dictionary
        if num_int in reverse_translation_dict:
            # Append the corresponding letter to the letters list
            letters.append(reverse_translation_dict[num_int])
        else:
            # Append a '?' if the number is not found in the dictionary (handles unknown numbers)
            letters.append('?')

    # Join the list of letters into a single string
    return ''.join(letters)


# Function to clear the terminal screen
def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:  # Assume Unix or MacOS
        os.system('clear')


# Main function to handle user input
def main():
    while True:

        # Color codes
        red = "\033[91m"
        green = "\033[92m"
        reset = "\033[0m"

        # Ask the user if they want to translate to numbers or words
        clear_screen()
        print("What would you like to translate?")
        print(f"-Words to Numbers ({green}n{reset})")
        print(f"-Numbers to Words ({green}w{reset})")
        print(f"-Exit ({red}e{reset})")
        choice = input(">> ").strip().lower()

        if choice == 'n':
            clear_screen()
            word = input("Enter the word to translate to numbers: ").strip()
            translated = translate_to_numbers(word)
            clear_screen()
            print(f"Translated to numbers: {green}{translated}{reset}")
            input("Press Enter to continue...")
            clear_screen()
        elif choice == 'w':
            clear_screen()
            numbers = input("Enter the numbers to translate to words (separate numbers with spaces): ").strip()
            translated_back = translate_to_word(numbers)
            clear_screen()
            print(f"Translated to words: {green}{translated_back}{reset}")
            input("Press Enter to continue...")
            clear_screen()
        elif choice == 'e':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 'n', 'w', or 'e'.")


# Run the main function
if __name__ == "__main__":
    main()
