# RQ marketplace
## Что такое RQ marketplace
Каждый разработчик ботов может написать приложение для RQ marketplace. Для этого вы должны соблюсти структуру приложения, правила приложения и правильно подать заявку. Ниже вы можете увидеть описание каждого из этих пунктов.		

## Структура приложения
Для написания приложений нужно использовать библиотеку [disnake](https://github.com/DisnakeDev/disnake) (fork discord py). В этом репозитории есть демонстрационное приложение в папке `demo/`. Там вы можете посмотреть пример приложения. Структура приложения:
 - `__init__.py` - файл с настройками приложениями
 - `helloworld.py` - ког

Когов можно загружать сколько потребуется для вашего приложения. Структура `__init__.py`:

    from disnake.ext import commands
    
    APP_NAME = 'demo' # имя приложения (такое название будет в маркетплейсе)
    AUTHOR = 858672170792386582 # id автора дискорда
    DESCRIPTION = 'Демонстрационное приложение RQmarketplace' # описание приложения
    COGS = ['Helloworld'] # имя всех классов когов 
    
    def start(bot: commands.Bot): 
        bot.load_extension(f'apps.{APP_NAME}.helloworld') # Загружаем ког helloworld

Каждый параметр приложения проверяется модерацией.

## Как подать заявку?
Вы должны создать репозиторий на github со структурой выше, где `__init__.py` и коги - в корне. Для того, чтобы подать заявку, вам нужно добавить гитхаб пользователя `RQmarketplace` в ваш репозиторий. Также вам нужно зайти на наш [дискорд сервер](https://discord.gg/M4JAeAZ3Bp), иначе мы не сможем вам ответить.




