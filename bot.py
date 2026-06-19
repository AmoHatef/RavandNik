from bale import Bot , Message
import time
import asyncio
bot = Bot (token = '1119681388:qtZI2h3TJ4zlWdC4cuUismy18pBIMm4S72U')
A = 0
marhale = 0
@bot.event
async def on_message(pm = Message):
    global marhale
    if pm.content == ('عاب خوردم'):
        await pm.reply('استراحت هم کردی؟🥵')
        marhale = 1
    elif pm.content == ('استراحت هم کردم'):
        print ('استراحت کرده شد')

    if pm.content == ('استراحت هم کردم') and marhale == 1:
        await pm.reply('عاب خوردی🌈')
    elif pm.content == ('عاب خوردم'):
        print ('عاب خورده شد')
    if pm.content == ('1478'):
        A = 1
        while A == 1:
                await bot.send_message(chat_id = '4360392520' , text = 'عاب بخور💦')
                await bot.send_message(chat_id = '4862063605' , text = 'عاب بخور💦')
                await bot.send_message(chat_id = '282784158' , text = 'عاب بخور💦')
                await bot.send_message(chat_id = '1652444615' , text = 'عاب بخور💦')
                await asyncio.sleep(1800)
        

if __name__ == '__main__':
    bot.run()
