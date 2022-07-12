import discord
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Đăng nhập: "+client.user.name)
    
@client.command(name= "calc", help = f'** Tính toán Đội hình **\n``{prefix}calc <Tổng> <%Bộ Binh> <%Lính Xe> <%Cung Thủ>')
async def calc(ctx, t:int , a:int=None, b:int=None , c:int=None):
    if a is None:
            result_inf_default =int((t*60)/100) 
            result_car_default =int((t*10)/100)
            result_range_default =int((t*30)/100)
            embed= disnake.Embed(title="", description =f"**Bộ Binh**: {result_inf_default} \n**Lính Xe**: {result_car_default} \n**Cung Thủ**: {result_range_default}", color =0x9208ea)
            embed.add_field(name = f"Tổng:",value=f"{t}",inline= False)
            embed.set_footer(text="Đội hình Phương trận Mặc Định 60/10/30")
            await ctx.send(embed=embed)
    if a and b and c is not None:
        if a+b+c ==100:
            result_inf =int((t*a)/100) 
            result_car =int((t*b)/100)
            result_range =int((t*c)/100)
            embed= disnake.Embed(title="", description =f"**Bộ Binh**: {result_inf} \n**Lính Xe**: {result_car} \n**Cung Thủ**: {result_range}", color =0x9208ea)
            embed.add_field( name= f"Tổng: ", value = f"{t}" , inline= False)
            embed.set_footer(text=f"Đội hình Phương trận {a}/{b}/{c} ")
            await ctx.send(embed=embed)    
        else:
            await ctx.send('``Syntax Error: 3 chỉ số cuối phải là phần trăm lính (Tổng 100%)``')
       
@client.event
async def on_command_error(error):
    if isinstance(error, commands.CommandNotFound):
        pass  
client.run(token)
