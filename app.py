from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Translation dictionary mapping each letter to its corresponding number
translation_dict = {
    'A': 1, 'N': 2, 'B': 3, 'O': 4, 'C': 5, 'P': 6,
    'D': 7, 'Q': 8, 'E': 9, 'R': 10, 'F': 11, 'S': 12,
    'G': 13, 'T': 14, 'H': 15, 'U': 16, 'I': 17, 'V': 18,
    'J': 19, 'W': 20, 'K': 21, 'X': 22, 'L': 23, 'Y': 24,
    'M': 25, 'Z': 26, ' ': 27
}

# Reverse dictionary for number to letter translation
reverse_translation_dict = {v: k for k, v in translation_dict.items()}

# Function to translate a word into a series of numbers based on the dictionary
def translate_to_numbers(word):
    numbers = [str(translation_dict.get(char.upper(), '?')) for char in word]
    return ' '.join(numbers)

# Function to translate a series of numbers back into a word
def translate_to_word(numbers):
    letters = [reverse_translation_dict.get(int(num), '?') for num in numbers.split()]
    return ''.join(letters)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        action = request.form.get('action')
        text = request.form.get('text')
        if action == 'n':
            result = translate_to_numbers(text)
        elif action == 'w':
            result = translate_to_word(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
