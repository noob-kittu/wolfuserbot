from wolf import bot
from wolf.utils import admin_cmd

@bot.on(admin_cmd(pattern=r"deployme"))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Click Here to deploy My Bot](https://heroku.com/deploy?template=https://github.com/MrSammyXD/wolfuserbot/blob/main)")
