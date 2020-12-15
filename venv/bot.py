# bot.py
import os

import discord
from dotenv import load_dotenv

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

currentDay = date.today().strftime("%d/%m/%y")

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('venv\client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

GUILD = os.getenv('DISCORD_GUILD')

bot = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    print("{0.author}: {0.content}".format(message))
    if message.author == client.user:
        return

    if "@" in message.content:
        await message.channel.send(message.author.mention)


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        updateCell(member)
        print("{0} joined {1.channel}".format(member, after))

def updateCell(member):
    sheet = client.open("tesst Attendance").sheet1
    cCell = sheet.find(str(currentDay))
    print("Found something at C%s" % (cCell.col))
    try:
        rCell = sheet.find(str(member))
        print("Found something at R%s" % (rCell.col))
    except:



bot.run(TOKEN)
