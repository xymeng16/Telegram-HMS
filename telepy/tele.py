# coding=utf-8
import sys
import io
import push_admin
import json
from push_admin import messaging

sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)
from telethon import TelegramClient, events
print(sys.stdout.encoding)
api_id = 00000000 # replace with your own one
api_hash = "replace with your own one"
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
client = TelegramClient('anon', api_id, api_hash)
app_id = "00000000"
app_secret = "replace with your own one"
push_admin.initialize_app(app_id, app_secret)
print("init push finished")

@client.on(events.NewMessage)
async def my_event_handler(event):
    sender = await event.get_sender()
    try:
        my_id = await client.get_me()
        print("sender.id=" + str(sender.id) + ", my_id=" + str(my_id.id))
        if sender.id == my_id.id:
            return
    except TypeError as e:
        print(e)
    name  = (sender.last_name if sender.last_name is not None else "") + " " + (sender.first_name if sender.first_name is not None else "") # name as title
    msg = "New MSG:" + event.raw_text # msg as body
    an = messaging.AndroidNotification(
        title=name,
        body=msg,
        click_action=messaging.AndroidClickAction(action_type=1, intent="intent://org.telegram.hmsmsger"),
        channel_id='-1',
        importance=messaging.AndroidNotification.PRIORITY_HIGH
    )
    android = messaging.AndroidConfig(
        collapse_key=-1,
        urgency=messaging.AndroidConfig.HIGH_PRIORITY,
        ttl="10000s",
        bi_tag='the_sample_bi_tag_for_receipt_service',
        notification=an
    )
    message = messaging.Message(android=android, token=['replace with your own token'])
    response = messaging.send_message(message, app_id="replace with your own one")
    print("response is ", json.dumps(vars(response)))
client.start()
client.run_until_disconnected()
