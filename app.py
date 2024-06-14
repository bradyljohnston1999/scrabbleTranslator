from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

translation_dict = {
    'A': 1, 'N': 2, 'B': 3, 'O': 4, 'C': 5, 'P': 6,
    'D': 7, 'Q': 8, 'E': 9, 'R': 10, 'F': 11, 'S': 12,
    'G': 13, 'T': 14, 'H': 15, 'U': 16, 'I': 17, 'V': 18,
    'J': 19, 'W': 20, 'K': 21, 'X': 22, 'L': 23, 'Y': 24,
    'M': 25, 'Z': 26, ' ': 27
}

reverse_translation_dict = {v: k for k, v in translation_dict.items()}

def translate_to_numbers(word: str) -> str:
    try:
        numbers = [str(translation_dict[char.upper()]) for char in word if char.upper() in translation_dict]
        return ' '.join(numbers)
    except KeyError:
        return "Invalid character in input."

def translate_to_word(numbers: str) -> str:
    try:
        letters = [reverse_translation_dict[int(num)] for num in numbers.split()]
        return ''.join(letters)
    except (ValueError, KeyError):
        return "Invalid number in input."

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/translate/", response_class=HTMLResponse)
async def translate(request: Request, action: str = Form(...), text: str = Form(...)):
    print(f"Received action: {action}, text: {text}")  # Debug print
    if action == 'n':
        result = translate_to_numbers(text)
    elif action == 'w':
        result = translate_to_word(text)
    else:
        result = "Invalid action."
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
