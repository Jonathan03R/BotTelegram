import telebot


TOKEN = '6977517981:AAEEnHzWqJPtx5m-z6GomNCkElUePQ1xv8w'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    # Mensaje de bienvenida
    welcome_message = (
        "HOLA ESTA ES UNA PRUEBA DE MI PRIMER BOT DE TELEGRAM\n\n"
        "este es mi primer bot de telegram hecho con Pythom\n\n"
        "Mi nombre es Jonathan Jesus Roque"
    )

    bot.reply_to(message, welcome_message)

@bot.message_handler(commands=['help'])
def handle_help(message):
    # Mensaje de ayuda
    help_message = (
        "¡Hola! Parece que estás buscando ayuda.\n\n"
        "Actualmente estamos desarrollando nuevas funciones para nuestro bot, "
        "así que por ahora solo existen los siguientes comandos:\n\n"
        "/start - Iniciar el bot\n"
        "/help - Mostrar este mensaje de ayuda\n\n"
        "¡Gracias por tu comprensión!"
    )
    # Responder al mensaje de ayuda con el mensaje de ayuda
    bot.reply_to(message, help_message)
    
    
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    unrecognized_message = "Comando no reconocido. Por favor, utiliza /help para obtener ayuda."
    bot.reply_to(message, unrecognized_message)

# Inicia el bot
if __name__ == "__main__":
    bot.polling(none_stop=True )
    print("El bot está funcionando correctamente. Esperando mensajes...")