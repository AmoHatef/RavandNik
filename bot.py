from bale import Bot , Message
import time
bot = Bot (token = '1119681388:qtZI2h3TJ4zlWdC4cuUismy18pBIMm4S72U')
A = 0
@bot.event
async def on_message(pm = Message):
    while A == 0:
        await bot.send_message(chat_id = '4360392520' , text = 'عاب بخور💦')
        await bot.send_message(chat_id = '4862063605' , text = 'عاب بخور💦')
        await bot.send_message(chat_id = '282784158' , text = 'عاب بخور💦')
        await bot.send_message(chat_id = '1652444615' , text = 'عاب بخور💦')
        time.sleep(1800)

if __name__ == '__main__':
    bot.run()
