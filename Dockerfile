FROM python:3.11-slim

# Устанавливаем Tesseract-OCR и нужные зависимости
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем Python-библиотеки
RUN pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Команда запуска бота
CMD ["python", "bot.py"]
