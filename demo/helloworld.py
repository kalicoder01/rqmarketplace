from disnake.ext import commands


class Helloworld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def helloworld(self, inter):
        """
        Возвращает "Привет, мир!"
        """

        await inter.send('Привет, мир!')


def setup(bot):
    bot.add_cog(Helloworld(bot))