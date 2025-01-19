# t.me/AI_B2112_bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

v = """
А й правда, крилатим ґрунту не треба.
Землі немає, то буде небо.

Немає поля, то буде воля.
Немає пари, то будуть хмари.

В цьому, напевно, правда пташина...
А як же людина? А що ж людина?

Живе на землі. Сама не літає.
А крила має. А крила має!

Вони, ті крила, не з пуху-пір"я,
А з правди, чесноти і довір"я.

У кого — з вірності у коханні.
У кого — з вічного поривання.

У кого — з щирості до роботи.
У кого — з щедрості на турботи.

У кого — з пісні, або з надії,
Або з поезії, або з мрії.

Людина нібито не літає...
А крила має. А крила має!
"""

v2 = """Давно,
іще в шістсот якомусь році,
ну, цебто більш як три віки тому,
коли носили шпаги ще при боці
і розважали стратами юрму,
коли відьом палили при народі,
коли наук не знали ще ладом, —

кажу, давно, кажу, у Вишгороді
підсудна Анна стала пред судом.

Було тій Анні, може, десять рочків,
Її привів розлючений сусід.
Багряне листя, кілька тих листочків,
останнє листя із кленових віт
було на стіл покладене, як доказ,
і шаруділо тихо на сукні.
Осіннє сонце, яблуко-недоквас,
стояло в голих кленах у вікні.

І той сусід сказав тоді у тиші:
— Панове судді! Я її привів.
Вона робила... кольорові миші
з оцих ось жовтих і сухих листків.
Ото складе листочок до листочка,
два рази хукне — так і побіжать.

У мене діти, в мене син і дочки,
у них цяцьки так жужмом і лежать.
Вони були нормальні і здорові,
а ця чаклунка збила їх з пуття."""

# Завдання додати 10 віршів
list_comand = """
/help - назви всіх команд
/hello - Привітання
/say1 - вірш Ліни Костенко Крила 
/say2 - Кольорові миші Ліна Костенко
"""
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def say1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(list_comand)

async def verse2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(v2)

app = ApplicationBuilder().token("7658906392:AAGl0c8CdU__nsUzGRE_srhoIej_wj25zo4").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("say1", say1))
app.add_handler(CommandHandler("say2", verse2))

app.run_polling()