#!/usr/bin/python3
import logging
from commandGiver import *




def mainloop(botti):
    while True:
        botti.fetch_update()
        last_update = botti.get_last_update()
        last_update_id = last_update['update_id']

        if last_update_id != botti.last_send_update_id:

            try:
                chat_id = str(botti.get_chat_id())

                command = last_update["message"]["text"].split(" ")[0]

                if command == "/kiltacam" or command == "/kiltacam@managerinbot":
                    print("nyt tehdään kiltacämi")
                    botti.send_gild_photo()

                elif command == "/tiivista" or command == "/tiivista@managerinbot":
                    botti.tiivista()

                else:
                    botti.send_message("moi",chat_id)
            except KeyError:
                logging.log(Warning, "Unkown command received. Ddunno how. Please fix")
                pass





if __name__ == "__main__":
    botti = Commander()
    botti.fetch_update()
    mainloop(botti)
