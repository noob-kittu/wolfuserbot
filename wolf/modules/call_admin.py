import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from wolf import CMD_HELP, bot
from wolf.events import mrsammy, admin_cmd
@mrsammy(outgoing=True, pattern="^\!report")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Reported to @admin"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


CMD_HELP.update({
    "report":
    "\
!report\
\nUsage: Reply to a message to report it to group admins "
})


