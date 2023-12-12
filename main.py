import random
import telebot

bot = telebot.TeleBot("6926532358:AAGdsSIWUi2ULEcOwWN-KEGUVJD9ZOJ2jk4")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я готов помочь тебе с выбором фильма на вечер")

@bot.message_handler(commands=['help'])
def help(message):
    help_message = """
    Вот список доступных команд:
    /start - начать взаимодействие с ботом
    /help - получить справку о доступных командах
    /recommend - получить рекомендацию на вечер
    """
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands=['recommend'])
def recommend(message):
    movies = ["Зеленая Книга", "Синистер", "Форрест Гамп", "Человек паук 2003", "Тупой и еще тупее"]
    recommended_movie = random.choice(movies)
    bot.send_message(message.chat.id, f"Мой рекомендуемый фильм на вечер: {recommended_movie}")

@bot.message_handler(func=lambda message: True)
def answer_question(message):
    question = message.text
    #Код для обработки вопроса и генерации ответа
    answer = "Мой ответ на ваш вопрос"
    bot.send_message(message.chat.id, answer)

bot.polling()