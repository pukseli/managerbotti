import requests
import logging
import urllib.request
from random import randint
import time
import datetime


AKSELIN_CHAT_ID = "193210704"
logging.basicConfig(level=logging.WARNING,  format="%(asctime)s %(levelname)s  %(message)s")



class Commander:
    _BOT_TOKEN = "496561553:AAFEub5mhvF-BQJiDRyN0xmzzdf9u5WatUg" #managerbotti
    #_BOT_TOKEN = "471505208:AAHs8IFgDdYwVLnPzAvAm4SOGBJVixO6QSI" #aksuntestibotti
    _BOT_URL = "https://api.telegram.org/bot" + _BOT_TOKEN + "/"
    last_update_id = 0
    last_send_update_id = 0
    _update = ""
    update_given = False
    emojis = ["\U0001F37B", "\U0001F4A9", "\U0001F60D", '\U0001F37A', "\U0001F34C", "Isä voisi puhua vähemmän",
              "\U0001F52B", "\U0001F525", "Nyt nukkumaan!", "Asiasisältöä", "\U0001F3E5","\U0001F494"]
    kahvikuppeja = 0
    kahvi_keitetty = datetime.datetime(2000,2,20)


    def tiivista(self):
        emoji = self.emojis[randint(0,len(self.emojis)-1)]
        print(emoji)
        chat_id = self.get_chat_id()
        self.send_message(emoji,chat_id=chat_id)


    def send_gild_photo(self,):
        timestamp = "?ts=" +str(time.time())
        chat_id = self.get_chat_id()
        self.last_send_update_id = self.last_update_id
        urllib.request.urlretrieve("http://tietojohtajakilta.net/webcam/cam_1.jpg", "kuva.png")
        url = self._BOT_URL + "sendPhoto?chat_id=" + str(chat_id) + "&photo=" + "http://tietojohtajakilta.net/webcam/cam_1.jpg" + timestamp

        r = requests.post(url)
        print(r.text)



    def send_message(self, message, chat_id):
        url = self._BOT_URL +"sendMessage?chat_id="+ str(chat_id) + "&text="+ str(message)
        self.last_send_update_id = self.last_update_id
        print(url)
        if not self.update_given:
            self.update_given = True
            return
        requests.post(url)


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


    def kahvia(self):
        if self.kahvikuppeja == 1:
            kahviviesti = "Kahvia jäljellä " + str(self.kahvikuppeja) + " kuppi"
        else:
            kahviviesti = "Kahvia jäljellä " + str(self.kahvikuppeja) + " kuppia"
        aikaviesti = "Kahvi keitetty "
        aika = datetime.time()

        self.send_message(kahviviesti, self.get_chat_id())

if __name__ == "__main__":
    a = Commander()
    a.fetch_update()
    a.send_message("Miten menee?")
    print(a.get_chat_id())
