import telebot
from peewee import *
from telebot import types

# Создаем подключение к базе данных
db = SqliteDatabase('database.db')

# Определяем модель данных
class Person(Model):
    number = IntegerField()
    full_name = CharField()
    email = CharField()
    group = CharField()

    class Meta:
        database = db

# Создаем таблицу в базе данных (если ее еще нет)
db.create_tables([Person])

# Создаем объект бота с помощью токена
bot = telebot.TeleBot('6283738632:AAEMyXKX6X3Nd3Q6qfXJddWrsywVO8aCUZI')


@bot.message_handler(commands=['start'])
def handle_start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button_1 = types.KeyboardButton('/Добавить')
    button_2 = types.KeyboardButton('/Вывод')
    button_3 = types.KeyboardButton('/Удалить')
    markup.add(button_1, button_2, button_3)
    bot.reply_to(message, "Привет! Я бот для работы с базой данных.", reply_markup=markup)


@bot.message_handler(commands=['Добавить'])
def handle_add(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Введите данные в формате: №, ФИО, email, группа")
    bot.register_next_step_handler(msg, process_add_step)

def process_add_step(message):
    chat_id = message.chat.id
    data = message.text.split(', ')
    if len(data) == 4:
        try:
            # Создаем запись в базе данных
            Person.create(number=int(data[0]), full_name=data[1], email=data[2], group=data[3])
            bot.send_message(chat_id, "Данные успешно добавлены.")
        except Exception as e:
            bot.send_message(chat_id, f"Ошибка при добавлении данных: {e}")
    else:
        bot.send_message(chat_id, "Неверный формат данных. Попробуйте снова.")


@bot.message_handler(commands=['Вывод'])
def handle_list(message):
    chat_id = message.chat.id
    rows = Person.select()
    data = ''
    for row in rows:
        data += f"№: {row.number}\nФИО: {row.full_name}\nEmail: {row.email}\nГруппа: {row.group}\n\n"
    if data:
        bot.send_message(chat_id, data)
    else:
        bot.send_message(chat_id, "Нет данных в базе.")

@bot.message_handler(commands=['Удалить'])
def handle_delete(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Введите номер для удаления:")
    bot.register_next_step_handler(msg, process_delete_step)

def process_delete_step(message):
    chat_id = message.chat.id
    number = message.text
    try:
        # Проверяем наличие записи с указанным номером
        person = Person.get(Person.number == number)
        person.delete_instance()
        bot.send_message(chat_id, "Запись успешно удалена.")
    except Person.DoesNotExist:
        bot.send_message(chat_id, "Запись с указанным номером не найдена.")
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при удалении записи: {e}")

# Запускаем бота
bot.polling()
