import discord, os, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=False
)

client.run(os.getenv("MTA2MzQ3NTkxODg0NjI5NjE0NQ.GVKty2.wz_PsQO31An_Ja4LvI-bGAjGb1S3KRs29XQRG0"), bot=False)
