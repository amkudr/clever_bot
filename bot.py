"""
Научите бота играть в города. Правила такие - внутри бота есть список городов, пользователь пишет /cities Москва и если в списке такой город есть, бот отвечает городом на букву "а" - "Альметьевск, ваш ход". Оба города должны удаляться из списка.

Помните, с ботом могут играть несколько пользователей одновременно
"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import cities


logging.basicConfig(filename="bot.log", level=logging.INFO)
def greet_user(update,context):
    print("Пользователь найден")
    update.message.reply_text('Олды тут?')

    print(update)
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def city_game(update, context):
    print("Игра началась")
    game_list = cities.CITIES   
    text = update.message.text.split()
    if len(text) == 1:
        update.message.reply_text("Введите город") 
    user_city = text[1].lower().capitalize()
 
    if game_list.count(user_city) == 1:
        game_list.remove(user_city)
        letter = user_city[-1].upper()
        for city in game_list:
            if city[0] == letter:
                bot_city = city
                return update.message.reply_text(f'{bot_city} , ваш ход')                                
    else:
        update.message.reply_text('Нет такого города')  


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cities", city_game))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("start botik")
    mybot.start_polling()
    mybot.idle()
if __name__ == "__main__":
    main()