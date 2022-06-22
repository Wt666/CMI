## chatbot.py
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# The messageHandler is used for all message updates
import configparser
import logging
import redis

# import os

global redis1


def main():
    # Load your token and create an Updater for your Bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    # You can set this logging module, so you will know when and why things do not work as expected
    global redis1
    redis1 = redis.Redis(host=(config['REDIS']['HOST']), password=(config['REDIS']['PASSWORD']),
                         port=(config['REDIS']['REDISPORT']))

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # register a dispatcher to handle message: here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("add", add))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hello", hello))
    dispatcher.add_handler(CommandHandler("calorie", calorie_command))
    dispatcher.add_handler(CommandHandler("dietary", dietary))
    dispatcher.add_handler(CommandHandler("SearchGym", gym))
    dispatcher.add_handler(CommandHandler("healthmenu", menu))

    # To start the bot:
    updater.start_polling()
    updater.idle()


def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)


def menu(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /menu is issued."""
    try:
        global redis1
        logging.info(context.args[0])
        msg = context.args[0]
        update.message.reply_text('https://www.takeaway.com/bg-en/menu/fitness-menu  for ' + msg)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /menu <keyword>')


def calorie_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /Calorie is issued."""
    update.message.reply_text('Calorie Caculator: https://www.calculator.net/calorie-calculator.html')


def gym(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /gym is issued."""
    update.message.reply_text('Where is gym, just follow this link: https://www.google.com/maps/search/gym/')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Helping you helping you.')


def add(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /add is issued."""
    try:
        global redis1
        logging.info(context.args[0])
        msg = context.args[0]  # /add keyword <-- this should store the keyword
        redis1.incr(msg)
        update.message.reply_text('You have said ' + msg + ' for ' + redis1.get(msg).decode('UTF-8') + ' times.')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <keyword>')


def hello(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /hello is issued."""
    try:
        global redis1
        logging.info(context.args[0])
        msg = context.args[0]
        update.message.reply_text('Good Day, ' + msg)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /hello <keyword>')


def dietary(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /dietary is issued."""
    try:
        global redis1
        logging.info(context.args[0])
        msg = int(context.args[0])
        if msg > 2000:
            msg = "Bad dietary"
        elif msg < 1800:
            msg = "Bad dietary"
        elif msg == 2000:
            msg = "Perfect dietary"
        else:
            msg = "Good dietary"
        update.message.reply_text(msg)
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /dietary <number of Today calorie intake>')


if __name__ == '__main__':
    main()