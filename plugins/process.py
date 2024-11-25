# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🌿
# Using approve_chat_join_requests() method requests will be accepted one by one!

import os
import logging
import asyncio
from bot import Bot
from config import OWNER_ID
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

CMD = [".", "/", "!"]

is_running = False
max_retries = 5  
long_wait_time = 40  
approve_delay = 3   

@Bot.on_message(filters.command(["start", "run", "approve"], CMD) & filters.me)
async def start_approve(client, message):
    global is_running
    pvt_id = OWNER_ID
    chat_id = message.chat.id
    await message.delete(True)

    if is_running:
        await client.send_message(pvt_id,"<i><b>Approval process is already running.</b></i>")
        await asyncio.sleep(1) 
        await client.delete_messages(chat_id, message.id)
        return

    is_running = True
    await client.send_message(pvt_id, "<i><b>Process was started..</b></i>")
    await asyncio.sleep(1) 
    await client.delete_messages(chat_id, message.id)

    retry_attempts = 0
    while is_running:
        try:
            async for request in client.get_chat_join_requests(chat_id):
                if not is_running: 
                    break
                try:
                    await client.approve_chat_join_requests(chat_id, request.user.id)
                    await asyncio.sleep(approve_delay) 
                except FloodWait as t:
                    logging.warning(f"Rate limited. Waiting for {t.value} seconds.")
                    await asyncio.sleep(t.value)
                except Exception as e:
                    logging.error(f"while approving user {request.user.id}: {str(e)}")                  
                    continue
            await asyncio.sleep(1)
        except Exception as e:
            if "503" in str(e): 
                retry_attempts += 1
                if retry_attempts > max_retries:
                    logging.warning("<i><b>Max retries exceeded. Exiting.</b></i>")
                    logging.warning("<i><b>Process stopped after maximum retries. Please check manually.</b></i>")
                    await asyncio.sleep(long_wait_time)  
                    break 
                wait_time = 2 ** retry_attempts 
                logging.warning(f"Telegram is having internal problems. Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                logging.error(f"An unexpected error occurred: {str(e)}")
                break 
    if is_running: 
        pvt_id = OWNER_ID
        await client.send_message(pvt_id, "<i><b>Successfully approved all pending requests! ✅</b></i>")   
    is_running = False
    
@Bot.on_message(filters.command(["stop", "cancel"], CMD))
async def stop_approve(client, message):
    global is_running
    pvt_id = OWNER_ID
    chat_id = message.chat.id
    if not is_running:
        await client.send_message(pvt_id,"<i><b>No approval process is currently running.</b></i>")
        await asyncio.sleep(1) 
        await client.delete_messages(chat_id, message.id)
    else:
        is_running = False
        await client.send_message(pvt_id, "<i><b>Process was manually stopped!</b></i>")
        await asyncio.sleep(1)
        await client.delete_messages(chat_id, message.id)
