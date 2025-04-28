from telegram.ext import Updater, MessageHandler, Filters
# esto es para forzar deploy

import os
TOKEN = os.getenv("TOKEN")


def bienvenida(update, context):
    for miembro in update.message.new_chat_members:
        # Envía una imagen desde tu PC
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open('img.jpg', 'rb'),  # Cambiá por el nombre de tu imagen
            caption=f"¡Bienvenido {miembro.first_name}!\nA nuestra zoociedad 🎉\nsolo se permite zoo de mujeres \n❌si mandas otro contenido seras eliminado ojo."
        )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, bienvenida))

    updater.start_polling()
    print("Bot con bienvenida visual iniciado...")
    updater.idle()

if __name__ == '__main__':
    main()
