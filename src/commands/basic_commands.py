from discord import Embed
from discord.ext import commands


class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start_command(self, ctx: commands.Context):
        embed = Embed(
            title='Bem vindo ao bot de RPG!',
            description='Para começar a jogar, digite `!start`',
            color=0x00ff00
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['start'])
    async def init_player(self, ctx: commands.Context):
        embed = Embed(
            title=f'Bem vindo {ctx.author.name}',
            description='Voce iniciou sua jornada!'
                        '\nInventario:'
                        '\n- 1 Espada de madeira'
                        '\n- 1 Armadura de couro'
                        '\n- 1 Poção de vida'
                        '\n- 1 Poção de mana'
                        '\nComandos disponíveis:'
                        '\n`!profile` ou `!p` - Mostra o seu perfil'
                        '\n`!shop` - Mostra a loja'
                        '\n`!buy` - Comprar um item'
                        '\n`!sell` - Vender um item'
                        '\n`!inventory` ou `!inv` - Mostra o seu inventário'
                        '\n`!help` - Mostra os comandos disponíveis',
            color=0x00ff00
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['p'])
    async def profile(self, ctx: commands.Context):
        profile_url = ctx.author.avatar
        print(profile_url)
        embed = Embed(
            title=f'{ctx.author.name} - Perfil',
            description=f'{ctx.author.name}'
                        '\nProgress'
                        '\nLevel: 1'
                        '\nExp: 0/100'
                        '\nGold: 0'
                        '\n\nAtributos'
                        '\nVida: 100'
                        '\nMana: 100'
                        '\nForça: 10'
                        '\nInteligência: 10'
                        '\nAgilidade: 10',
            color=0x0000ff,
        )
        embed.set_thumbnail(url=profile_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def shop(self, ctx: commands.Context):
        await ctx.send(f'shop')

    @commands.command()
    async def buy(self, ctx: commands.Context):
        await ctx.send(f'buy')

    @commands.command()
    async def sell(self, ctx: commands.Context):
        await ctx.send(f'sell')

    @commands.command(aliases=['inv'])
    async def inventory(self, ctx: commands.Context):
        await ctx.send(f'inventory')


async def setup(bot):
    await bot.add_cog(BasicCommands(bot))
