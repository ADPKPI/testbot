from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import mysql.connector
import logging
from mysql.connector import pooling

#hgdhghjghagwjhdgajhwdjhagjdhgajhwdghwGDjhAWgdhjg
#ПРОВЕРКА CI/CD

dbconfig = {
    "host": "78.140.189.245",
    "user": "ttt_user",
    "password": "qwerty",
    "database": "test_db"
}

cnxpool = pooling.MySQLConnectionPool(pool_name = "mypool",
                                      pool_size = 5,
                                      **dbconfig)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Use /show to display table content.')

def show_table_content(update, context):
    """Show table content using a connection from the pool."""
    # Получение соединения из пула
    cnx = cnxpool.get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM test_table")
    rows = cursor.fetchall()
    message = "Table Contents!!!!!!!!!!!!!!!!:\n" + "\n".join([f"id: {row[0]}, name: {row[1]}" for row in rows])
    update.message.reply_text(message)
    cursor.close()
    cnx.close()  # Возвращение соединения в пул

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7150906174:AAEJf_lbV_vRGkmFmwqMZiXLBE4npfcXEaM")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("show", show_table_content))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()