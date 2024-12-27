import telebot
from collections import defaultdict
from logic import Question

API_TOKEN = 'YOUR_API_TOKEN'  # Замените на ваш токен бота
bot = telebot.TeleBot(API_TOKEN)

# Словарь для хранения вопросов
quiz_questions = [
    Question("Какой цвет неба?", 0, "Синий", "Зеленый", "Красный"),
    Question("Сколько дней в неделе?", 2, "5", "6", "7"),
    Question("Какой язык программирования самый популярный?", 1, "Python", "Java", "C++")
]

# Словари для отслеживания ответов пользователей и их очков
user_responses = {}
points = defaultdict(int)

@bot.message_handler(commands=['start'])
def send_question(chat_id):
    if chat_id not in user_responses:
        user_responses[chat_id] = 0  # Первое сообщение для пользователя, ставим 0

    question_index = user_responses[chat_id]  # получаем номер последнего вопроса

    if question_index < len(quiz_questions):  # если есть еще вопросы
        question = quiz_questions[question_index]
        bot.send_message(chat_id, question.text, reply_markup=question.generate_keyboard())
    else:
        bot.send_message(chat_id, f"The end! Ваши очки: {points[chat_id]}")  # Отправляем количество очков

@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    chat_id = call.message.chat.id
    question_index = user_responses[chat_id]

    if call.data == "correct":
        bot.answer_callback_query(call.id, "Правильный ответ!")
        points[chat_id] += 1  # Добавляем очки за правильный ответ
    else:
        bot.answer_callback_query(call.id, "Неправильный ответ.")

    user_responses[chat_id] += 1  # увеличиваем номер последнего вопроса

    # Отправляем следующий вопрос или сообщение о завершении
    send_question(chat_id)

if __name__ == "__main__":
    bot.polling()
