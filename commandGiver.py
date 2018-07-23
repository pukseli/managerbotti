import requests
import logging
from random import randint
import time
import datetime
import telegram


AKSELIN_CHAT_ID = "193210704"
logging.basicConfig(level=logging.WARNING,  format="%(asctime)s %(levelname)s  %(message)s")


class Commander:

    #_BOT_TOKEN = "496561553:AAFEub5mhvF-BQJiDRyN0xmzzdf9u5WatUg" #managerbotti
    #_BOT_TOKEN = "471505208:AAHs8IFgDdYwVLnPzAvAm4SOGBJVixO6QSI" #aksuntestibotti
    _BOT_TOKEN = "627633049:AAHQMWa4hp5XLbTkBQZrBsX64tl2fgrQ2wM" #voicemessagebot
    _BOT_URL = "https://api.telegram.org/bot" + _BOT_TOKEN + "/"
    last_update_id = 0
    last_send_update_id = 0
    _update = ""
    update_given = False
    VOICE_MESSAGES = {"brutal":"src/voice_messages/brutal.ogg","kakka":"src/voice_messages/kakka.ogg", "playing to win":"src/voice_messages/playing_to_win.ogg","wow":"src/voice_messages/wow.ogg","kiitos":"src/voice_messages/kiitos.ogg"}
    bot = telegram.Bot(token=_BOT_TOKEN)

    def voice_message_is_in_database(self,voice, chat_id):
        try:
            test = self.VOICE_MESSAGES[voice]
            print(test)
            return True
        except KeyError:
            self.bot.send_message(text="No such a message in database",chat_id=chat_id,)
            return False

    def get_voice_message(self, voice, chat_id):
        print(voice)
        if self.voice_message_is_in_database(voice, chat_id):
            self.bot.send_voice(voice=open(self.VOICE_MESSAGES[voice],"rb"), chat_id=chat_id,timeout=200)
        else:
            return




    def send_message(self, message, chat_id):
        self.last_send_update_id = self.last_update_id
        self.bot.send_message(chat_id, message + "")


    def get_last_update(self):
        self.fetch_update()

        if len(self._update) > 0:
            last_update = self._update[-1]
        else:
            last_update = self._update[len(self._update)]
        self.last_update_id = last_update["update_id"]
        return last_update


    def fetch_update(self):
        params = {'timeout': 30, 'offset': None}
        update = requests.get( self._BOT_URL + "getUpdates", data=params)
        self._update = update.json()["result"]



    def get_chat_id(self):
        chat_id = self._update[-1]['message']['chat']['id']
        if self.last_update_id == 0:
            return "0"
        return chat_id


if __name__ == "__main__":
    a = Commander()
    a.fetch_update()
    print(a.get_chat_id())
