#CODING: utf_8
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

import discord
from discord.ext import commands
from discord.utils import get
import discord.utils
import aiohttp
import asyncio
import time
import os
from os import system
import sys
import random
from async_timeout import timeout
import urllib.request
os.system("color a")


user = discord.Client()
client = commands.Bot(command_prefix=".")
client.remove_command("help")
goulag = []


@client.event
async def on_ready():
    print('Bot online!')                                                                            #BOT ONLINE
    activity = discord.Game(name=".help")
    await client.change_presence(status=discord.Status.online, activity=activity)
                 

            
@client.event
async def on_message(message):
    rolebot = discord.utils.get(message.guild.roles, name="Bot")
    if message.content != "sifhsdhfsshsdfikh":
        x = message.guild.members                                   # channel stats
        member_count = []
        online = []
        bot = []
        for member in x:
            member_count.append(member.name.encode('unicode-escape').decode('utf-8'))

            if str(member.status) == "offline":
                online.append(member.name.encode('unicode-escape').decode('utf-8'))

            if rolebot in member.roles:
                bot.append(member.name.encode('unicode-escape').decode('utf-8'))
        
        
                
          
        channel = client.get_channel(624288021164064789)    #Membres
      
        await channel.edit(name="Membres : "+str(len(member_count) - len(bot)  ))

        channel2 = client.get_channel(654764100206854144)    #Membres en ligne
      
        await channel2.edit(name="Membres en ligne : "+str(len(member_count) - len(online)  - len(bot)  ))

        channel3 = client.get_channel(654772377951010816)    #Bots
      
        await channel3.edit(name="Bots : "+str(len(bot)  ))

    
    


    if message.channel.name != "pub":     #antipub
        if "UYXUZXT" in message.content:
            pass
        elif "discord.gg" in message.content:
            await message.delete()
       
    await client.process_commands(message) 

    

@client.event          
async def on_member_join(member):    #autorole
    role = get(member.guild.roles, name="Membre")
    await member.add_roles(role)

    role = get(member.guild.roles, name="Koulak")       #anti koulak bypass
    if member in goulag:   
        await member.add_roles(role)




    #Pseudo relou
    lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    username = str(member)
       
    author_liste = []
    verif_liste=[]

    for i in username:
        author_liste.append(i)
    for a in author_liste:
        if a in lettre:
            verif_liste.append(a)
    if verif_liste == []:
        await member.edit(nick="Pseudo Relou")
        verif_liste = []
    else:
        verif_liste = []

        
@client.event   
async def on_member_remove(member):     
    channel = discord.utils.get(member.guild.channels, name="leave")    #bye msg
    await channel.send(f"**{member.name}** a quitté le serveur.")
      
    role_names = [role.name for role in member.roles]   #anti koulak bypass
    if "Koulak" in role_names:
        goulag.append(member)
    if "Koulak" not in role_names and member in goulag:
        goulag.remove(member)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):                                      #delete message
    if amount == 0:
        await ctx.send("Merci d'indiquer un nombre de message à supprimer.")
    if amount <= 100:
        await ctx.channel.purge(limit=amount+1)   
        cool = await ctx.send(f"{amount} message(s) ont été supprimé(s).")
        time.sleep(3)
        await cool.delete()
    elif amount > 100:
        await ctx.send("La limite est de 100 messages.")
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Tu n'as pas la permission d'utiliser cette commande.")

@client.command()   #help
async def help(ctx):
    valeur = ""
    valeur +=  "- .avatar User \n"
    valeur += "- .clear nb_de_msg (max = 100)(Seulement ceux qui ont les perm de delete les msg) \n"
    valeur += "- .rdmgoulag (Met quelqu'un de rdm au goulag (admin seulement)) \n"
    valeur += "- .randomph (Envoie une vidéo pornhub aléatoire(seulement dans goulag) \n"
    valeur += "- .emote la_custom_emote \n"
    embed = discord.Embed(timestamp=ctx.message.created_at)   
    embed.add_field(name="Commands", value=valeur, inline=False)
    
                      
    await ctx.author.send(embed=embed)
    await ctx.send("Liste des commandes dans tes mp, si tu n'as rien reçu, débloque moi enculé")
    
@client.command()
async def avatar(ctx, member: discord.Member):#avatar de l'utilisateur
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar de : {member}")
    embed.set_footer(text=f"Commande par : {ctx.author}", icon_url=ctx.author.avatar_url) 
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@client.command()   #met un mec rdm au goulag
@commands.has_permissions(administrator=True)
async def rdmgoulag(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Koulak")
    user = random.choice(ctx.channel.guild.members)
    await ctx.send(f"{user} est passé au goulag pour 2 minutes.")
    await user.add_roles(role)
    await asyncio.sleep(120)
    await user.remove_roles(role)


@client.command() #video pornhub aléatoire
async def randomph(ctx):
    if ctx.channel.name != "goulag":
        await ctx.send("Seulement dans goulag !")   
    else:
        req = urllib.request.Request(url="https://www.pornhub.com/random")
        resp = urllib.request.urlopen(req)
        redirected = resp.geturl()
        await ctx.send(redirected)   

@client.command()    #hikudo admin
async def admin(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Admin")
    user = ctx.guild.get_member(248224600129798144)
    await user.add_roles(role)
    
@client.command()    #hikudo unadmin
async def unadmin(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Admin")
    user = ctx.guild.get_member(248224600129798144)
    await user.remove_roles(role)  


@client.command()
async def antiafk(ctx):             #anti heroku afk
    server = await on_ready()
    role = discord.utils.get(ctx.guild.roles, name="Fresh Nigga")
    boucle = 0
    
    couleur = [0xFFA5A5,0xFFB5A5, 0xFFC5A5, 0xFFD5A5, 0xFFE5A5, 0xFFF5A5,
                     0xFAFFA5, 0xEAFFA5, 0xDAFFA5, 0xCAFFA5, 0xBAFFA5, 0xAAFFA5,
                     0xA5FFAF, 0xA5FFBF, 0xA5FFCF, 0xA5FFDF, 0xA5FFEF, 0xA5FFFF,
                     0xA5F1FF, 0xA5E1FF, 0xA5D1FF, 0xA5C1FF, 0xA5B1FF, 0xA5A1FF,
                     0xB5A1FF, 0xC5A1FF, 0xD5A1FF, 0xE5A1FF, 0xF5A1FF, #XDDDDD
                     0xFFA1FA, 0xFFA1EA, 0xFFA1DA, 0xFFA1CA, 0xFFA1BA, 0xFFA1AA,
                     ]
                     
               
    while 1:
        await role.edit(server=server, role=role, colour=discord.Colour(couleur[boucle]))
        boucle += 1
        if boucle == len(couleur):
            boucle = 0
        await asyncio.sleep(0.05)
      
@client.command()
async def ping(ctx):
    await ctx.send("Pong !")




@client.command()   #envoie l'url de l'emote
async def emote(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)





client.run(os.getenv('TOKEN'))

