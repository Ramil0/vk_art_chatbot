import vk_api
import time
import random
import numpy as np

TOKEN = # Here is where the token is to be placed.
vk_ = vk_api.VkApi(token=TOKEN)
vk = vk_.get_api()

names = np.load('names.npy')
n_pictures = sum([len(names[i]) for i in range(len(names))])
USER_ID = 35201895
PHOTO_IDS = [456239832, 456239933, 456240078]

correct_answer = {}

values = {'out': 0, 'count': 1,'time_offset': 60}
while True:
    response = vk_.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        img_id = random.randrange(n_pictures)
        message = ''
        if item['user_id'] in correct_answer.keys():
            message = u'Правильный ответ:\n' + correct_answer[
            item['user_id']] + u'\n\nНовая картинка:\n'
        if img_id < len(names[0]):
            vk.messages.send(user_id=item['user_id'], 
                             message=message,
                             attachment='photo-166583211_' + 
                             str(PHOTO_IDS[0] + img_id))
            correct_answer[item['user_id']] = names[0][img_id]
        elif img_id < len(names[0]) + len(names[1]):
            vk.messages.send(user_id=item['user_id'], 
                             message=message,
                             attachment='photo-166583211_' + 
                             str(PHOTO_IDS[1] + img_id - len(names[0])))
            correct_answer[item['user_id']] = names[1][img_id - len(names[0])]
        else:
            vk.messages.send(user_id=item['user_id'], 
                             message=message,
                             attachment='photo-166583211_' +
                             str(PHOTO_IDS[2] + img_id -
                                 len(names[0]) - len(names[1])))
            correct_answer[item['user_id']] = names[2][
                img_id - len(names[0]) - len(names[1])]
    time.sleep(1)