#!/usr/bin/python3
import logging
from commandGiver import *
import time




def mainloop(botti):
    last_update = botti.get_last_update()
    update_id = last_update['update_id']
    send_update_id = update_id

    while True:
        last_update = botti.get_last_update()
        update_id=last_update['update_id']
        if update_id != send_update_id:
            chat_id = str(botti.get_chat_id())
            message = last_update["message"]["text"].split(" ")
            command = message[0]
            print(message)
            text= " ".join(message[1:])
            if command == "voice":
                botti.get_voice_message(" ".join(message[1:]),chat_id)

            elif command == "/help":
                helppi = "Commands: \nvoice [voice message]: get voice message. \nlist: list of available messages"
                botti.send_message(helppi, chat_id)

            elif command == "list":
                botti.list_of_voice_messages(chat_id)
            else:
                botti.send_message("moi", chat_id)


        time.sleep(1)
        send_update_id=update_id


if __name__ == "__main__":
    botti = Commander()
    botti.fetch_update()
    mainloop(botti)
