from disnake.ext import commands

APP_NAME = 'demo' # имя приложения (такое название будет в маркетплейсе)
AUTHOR = 858672170792386582 # id автора дискорда
DESCRIPTION = 'Демонстрационное приложение RQmarketplace' # описание приложения
COGS = ['Helloworld'] # имя всех классов когов 

def start(bot: commands.Bot): 
    bot.load_extension(f'apps.{APP_NAME}.helloworld') # Загружаем ког helloworld