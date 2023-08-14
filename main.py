import telebot
import requests
from telebot import types

bot = telebot.TeleBot("6468608909:AAFtgChc_0GtWV6O8vp_peoRUFaN5twTjPQ", parse_mode="html")
users = {}
print("_____ START BOT ________")


def simple_numbers(star_value, end_value):
    simple_num = []
    for i in range(star_value, end_value):
        flag = True
        for dil in range(star_value, end_value):
            if dil != 1 and dil < i:
                result = i % dil
                if result == 0:
                    flag = False
                    break

            if dil >= i:
                break
        if flag:
            simple_num.append(i)
    return simple_num


def get_user_name(msg):
    cid = msg.chat.id
    txt = msg.text
    users[f"{cid}"] = {}
    users[f"{cid}"]["name"] = txt
    mess = bot.send_message(cid, "Enter your age: ")
    bot.register_next_step_handler(mess, get_user_age)


def get_user_age(msg):
    cid = msg.chat.id
    txt = msg.text
    users[f"{cid}"]["age"] = txt
    msg_text = f'Name: {users[f"{cid}"]["name"]} \n' \
               f'Age: {users[f"{cid}"]["age"]}'
    bot.send_message(cid, msg_text, reply_markup=main_reply_menu())


def get_products():
    baseURL = "https://fakestoreapi.com"
    response = requests.get(f"{baseURL}/products")
    data = response.json()
    text = ""
    for item in data:
        text += f"{item['id']}. {item['title']} -- {item['price']}\n"

    return text


### REPLY KEYBOARD
def main_reply_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("🦆Показати продукти"))
    markup.row(types.KeyboardButton("🦆Прості числа"), types.KeyboardButton("💋SubMenu"),
               types.KeyboardButton("🙈Inline Menu"))
    markup.row(types.KeyboardButton("/start"), types.KeyboardButton("📍Ask me?"))
    return markup


def r_sub_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton("BTN - 1")
    btn_two = types.KeyboardButton("BTN - 2")
    btn_three = types.KeyboardButton("BTN - 3")
    btn_four = types.KeyboardButton("BTN - 4")
    btn_five = types.KeyboardButton("BTN - 5")
    btn_return = types.KeyboardButton("Назад")

    markup.row(btn_one, btn_two, btn_three)
    markup.row(btn_four, btn_five)
    markup.row(btn_return)

    return markup


### INLINE KEYBOARD
def i_test_menu():
    kb = types.InlineKeyboardMarkup()
    btn_one = types.InlineKeyboardButton("BTN ONE", callback_data="btn_one")
    btn_course = types.InlineKeyboardButton("SHOW COURSE", callback_data="btn_course")
    kb.row(btn_one, btn_one)
    kb.row(btn_course)
    return kb


@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg):
    cid = msg.chat.id
    bot.send_message(cid, "Hello!", reply_markup=main_reply_menu())
    # bot.reply_to(message, "Howdy, how are you doing?")


@bot.callback_query_handler(func=lambda call: True)
def inline_menu(call):
    cid = call.message.chat.id
    data = call.data
    if data == "btn_one":
        bot.send_message(cid, "Success inline key!", reply_markup=r_sub_menu())
    elif data == "btn_course":
        photo = open("img/barbie.webp", "rb")
        bot.send_photo(cid, photo, caption="Good picture!")


@bot.message_handler(func=lambda message: True)
def echo_all(msg):
    # bot.reply_to(message, message.text)
    cid = msg.chat.id
    if msg.text.lower() == "прості числа":
        bot.send_message(cid, "hello world !!!")
    elif msg.text == "🦆Прості числа":
        numbers = simple_numbers(1, 100)
        temp_text = "<b>Список простих чисел:</b> \n"
        for num in numbers:
            temp_text += f"{num} "
        bot.send_message(cid, temp_text)
    elif msg.text == "💋SubMenu":
        bot.send_message(cid, "💋", reply_markup=r_sub_menu())
    elif msg.text == "Назад":
        bot.send_message(cid, msg.text, reply_markup=main_reply_menu())
    elif msg.text == "🙈Inline Menu":
        bot.send_message(cid, "🙈", reply_markup=i_test_menu())
    elif msg.text == "📍Ask me?":
        mess = bot.send_message(cid, "Input your name: ")
        bot.register_next_step_handler(mess, get_user_name)
    elif msg.text == "🦆Показати продукти":
        ##############
        text = get_products()
        bot.send_message(cid, text)


bot.infinity_polling()
