#here will be the code of the bot.

# Path: config.py
#here will be the token of the bot.
import config
token = config.token


import discord
from discord.ext import commands
import os
import random
import asyncio

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['roach', 'nigga'])
async def _8ball(ctx, *, question):

    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return
        
@client.command()
async def mute(ctx, member : discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)

@client.command()
async def unmute(ctx, member : discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    await channel.connect()
    server = ctx.message.guild
    voice_channel = server.voice_client
    player = await voice_channel.create_ytdl_player(url)
    player.start()

@client.command()
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    await voice_channel.disconnect()

@client.command()
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.pause()

@client.command()
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.resume()

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="List of commands are:", color=0xeee657)

    embed.add_field(name="!ping", value="Returns Pong!", inline=False)
    embed.add_field(name="!nigga or !roach", value="Answers a question with a random answer", inline=False)
    embed.add_field(name="!clear", value="Clears the chat", inline=False)
    embed.add_field(name="!kick", value="Kicks a member", inline=False)
    embed.add_field(name="!ban", value="Bans a member", inline=False)
    embed.add_field(name="!unban", value="Unbans a member", inline=False)
    embed.add_field(name="!mute", value="Mutes a member", inline=False)
    embed.add_field(name="!unmute", value="Unmutes a member", inline=False)
    embed.add_field(name="!join", value="Joins a voice channel", inline=False)
    embed.add_field(name="!leave", value="Leaves a voice channel", inline=False)
    embed.add_field(name="!play", value="Plays a song", inline=False)
    embed.add_field(name="!stop", value="Stops the song", inline=False)
    embed.add_field(name="!pause", value="Pauses the song", inline=False)
    embed.add_field(name="!resume", value="Resumes the song", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def hi(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! How are you?')
    await asyncio.sleep(5)
    await ctx.send(f'Oh, I see you are {ctx.author.mention}! Thats nice!')
    await asyncio.sleep(5)
    await ctx.send(f'Well, I have to go now {ctx.author.mention}! Bye!')

    


        
client.run(token)

