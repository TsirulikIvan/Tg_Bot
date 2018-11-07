import requests
import json

class Pipl:
    name = ''
    username = ''
    id = ''
    is_bot = ''
    def __init__(self, data):
        self.name = data['message']['from']['first_name']
        self.username = data['message']['from']['username']
        self.id = data['message']['from']['id']
        self.is_bot = data['message']['from']['is_bot']
    def see_all_inf(self):
        return "Name: %s, username: %s, id: %s" %
         (self.name, self.username, self.id)


url = "https://api.telegram.org/bot635901796:AAF9u-PDgx8vOErwB96jo8Uy41EoC9bUYfE/"
def parse_to_obj_dict(data):
    num = data['result']
    dic = {}
    for item in num:
            dic[item['message']['from']['first_name']] = Pipl(item)
    return dic

def get_updates_json(request):
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


dicts = parse_to_obj_dict(get_updates_json(url))
for i in dicts.values():
    print(i.see_all_inf())

#chat_id = get_chat_id(last_update(get_updates_json(url)))
#send_mess(chat_id, 'Привет Егор!')
