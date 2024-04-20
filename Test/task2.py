import json
import requests
import sys

with open('dinner.json') as cat_file:
    data = json.load(cat_file)
host, port = data['host'], data['port']
dishes = requests.get(f'http://{host}:{port}').json()
if not dishes:
    print("Ошибка выполнения запроса:")
    # print(response)
    print("Http статус:", dishes.status_code, "(", dishes.reason, ")")
    sys.exit(1)
# dishes = [
#     {"receipt": "king`s fried egg", "egg": 3, "salt": 1},
#     {"receipt": "fried egg", "egg": 2, "salt": 1},
#     {"receipt": "fried egg with cheese", "egg": 2, "cheese": 2, "salt": 1},
#     {"receipt": "omelette", "egg": 2, "salt": 1, "milk": 1},
#     {"receipt": "omelette with cheese", "egg": 2, "cheese": 2, "salt": 1, "milk": 2},
#     {"receipt": "omelette with cheese and bacon", "egg": 2, "cheese": 2, "bacon": 1, "salt": 1, "milk": 1}
# ]
answers = []
for dish in dishes:
    for key in dish:
        if not (key == 'receipt' or key in data and data[key] >= dish[key]):
            break
    else:
        answers.append(dish['receipt'])
print(*sorted(answers), sep='\n')
