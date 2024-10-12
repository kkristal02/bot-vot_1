import logging
from telegram.ext import Application, MessageHandler, filters
from secret_token import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

async def echo(update, context):
    match update.message.text:
        case 'Привет':
            text = 'Привет'
        case 'Пока':
            text = 'Пока'
        case 'Как дела?':
            text = 'Отлично'
        case 'Расскажи о товаре.':
            text = 'Я могу рассказать о наших товарах.'
        case _:
            text = 'Я вас не понимаю.'
    await update.message.reply_text(text)
    
def main():
    application = Application.builder().token(TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, echo)
    application.add_handler(text_handler)
    application.run_polling()

if __name__ == '__main__':
    main()
