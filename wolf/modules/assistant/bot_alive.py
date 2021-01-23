from telethon import events

from wolf import ALIVE_NAME, bot

currentversion = "4.9"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "wolfs"
PM_IMG = "https://telegra.ph/file/500234445239ebade2d49.jpg"
pm_caption = "🔹 `Telethon:` **1.15.0** \n"
pm_caption += "🔸 `Python:` **3.7.4** \n"
pm_caption += "🔹 `Fork Bye:` **WolfGanG** \n"
pm_caption += "🔸 `Version:` **{DEFAULTUSER}** \n"
pm_caption += "🔹 `Join:`  **@WolfUpdates**\n"
pm_caption += "🔸 `Wolf Repo:` **[Deploy✔️](https://github.com/MrSammyXD/wolfuserbot)** \n"


@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
