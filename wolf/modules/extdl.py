#   Copyright 2019 - 2020 DarkPrinc3

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.




# Thanks to Dark prince for this plugin..which was already here in DC but we were not awake of this..


""" 
   Thats the reason I say I am an idiot... To use this you have to fill the var PLUGIN_CHANNEL from which you want all your plugins to be installed.. Similar like installall.py / load_all.py which initially wolfs made..but it did existed here 
Since a long time...

"""
#modified by sh1vam
from wolf import bot
from wolf import bot as borg
from telethon import events
from telethon import functions, types
from telethon.tl.types import InputMessagesFilterDocument
from wolf.utils import command, remove_plugin, load_module

from pathlib import Path
from wolf import LOAD_PLUG
import sys
import asyncio
import traceback
import os
import wolf.utils
PLUGIN_CHANNEL=int(os.environ.get("PLUGIN_CHANNEL",-100))
@command(pattern="^!extdl", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    chat = PLUGIN_CHANNEL
    documentss = await bot.get_messages(chat, None , filter=InputMessagesFilterDocument)
    total = int(documentss.total)
    total_doxx = range(0, total)
    await event.delete()
    for ixo in total_doxx:
        mxo = documentss[ixo].id
        downloaded_file_name = await event.client.download_media(await borg.get_messages(chat, ids=mxo), "wolf/modules/")
        if "(" not in downloaded_file_name:
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            await borg.send_message(event.chat_id, "Installed Plugin `{}` successfully.".format(os.path.basename(downloaded_file_name)))
        else:
            await borg.send_message(event.chat_id, "Plugin `{}` has been pre-installed and cannot be installed.".format(os.path.basename(downloaded_file_name)))