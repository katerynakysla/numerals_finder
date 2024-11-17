from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Шаблони для перевірки на корені числівників (з врахуванням відмінків)
patterns = [
    r'\b\w*багат\w*|\w*мало|\w*мале\w*\b',
    r'\b\w*багац\w*\b',
    r'\bобо\w*\b',
    r'\b\w*кільк\w*\b',
    r'\bпівтор\w*\b',
    r'\b\d+\b',
    r'\b\w*льйон\w*\b',
    r'\bтисяч\w+\b',
    r'\bнул\w+\b',
    r'\b(сто\w*|ста\w*)\b',
    r'\b(одн\w*|один\w*|один)\b',
    r'\b\w*дв\w+\b',
    r'\b(три|три\w+|трьох\w*|трьом\w*|тре\w+|трі\w+|тро\w+)\b',
    r'\bчотир\w+\b',
    r"п[’'']ят\w*\b",
    r'\b(шіст\w+|шест\w+)\b',
    r'\b(сім\w+|сем\w+)\b',
    r'\b(вісім\w*|восьм\w+|вісьм\w+)\b',
    r'\bдев’ят\w+\b',
    r'\bдев’ян\w+\b',
    r'\bдесят\w+\b',
    r'\w+дцят\w+\b',
    r'\b(сорок|сорок\w+)\b',
    r'\b(\w*перш\w+|\w*друг\w+|\w*четвер\w+|\w*шост\w+|\w*сьом\w+|\w*восьм\w+|\w*девʼят\w+|\w*девʼян\w+|\w*сот\w+|\w*тисяч\w+)\b'
]

# Функція для пошуку числівників
def find_numerals(text):
    numerals_found = set()  # Використовуємо set для унікальних значень
    text = text.lower()  # Перетворюємо текст у нижній регістр
    for pattern in patterns:
        matches = re.findall(pattern, text)  # Шукаємо відповідності
        numerals_found.update(matches)  # Додаємо знайдені числівники у множину
    return list(numerals_found)

@app.route('/', methods=['GET', 'POST'])
def home():
    numerals = []
    error_message = ""
    if request.method == 'POST':
        text = request.form['text'].strip()  # Отримуємо введений текст та прибираємо зайві пробіли
        if not text:
            error_message = "Будь ласка, введіть текст."
        else:
            numerals = find_numerals(text)  # Знайти числівники
            if not numerals:
                error_message = "Числівників не знайдено."
    return render_template('index.html', numerals=numerals, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True, port=5004)