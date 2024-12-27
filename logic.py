from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text          # текст вопроса
        self.__answer_id = answer_id  # порядковый номер правильного ответа
        self.options = list(options)  # список с вариантами ответа

    @property
    def text(self):
        return self.__text     # геттер для получения текста вопроса

    def generate_keyboard(self):
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)  # устанавливаем ширину строки в зависимости от количества вариантов ответов

        for i, option in enumerate(self.options):
            if self.__answer_id == i:   # если текущий индекс равен правильному ответу
                markup.add(InlineKeyboardButton(option, callback_data='correct'))
            else:
                markup.add(InlineKeyboardButton(option, callback_data='wrong'))
                
        return markup
