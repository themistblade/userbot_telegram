api_id = '' # from https://my.telegram.org/apps
api_hash = ''

"""That bot can send the sum of the message 1 + 2 + 3 etc."""
# I need that bot to sum my brainstorm math

from pyrogram import Client
from pyrogram import filters

app = Client("my_account", api_id, api_hash)


@app.on_message(filters.command("sum", prefixes="."))
def sum1(app, msg):
    try:
        res = list(msg.reply_to_message.text.split('+'))
        result = 0
        for ent in res:
            result += int(ent)
        msg.edit_text(f"`{result}`")
    except:
        pass

app.run()