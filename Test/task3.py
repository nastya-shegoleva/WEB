import argparse
import requests
import sys
import json

parser = argparse.ArgumentParser()
parser.add_argument('rooms', nargs='*',
                    type=str, help='name rooms')
parser.add_argument("--future", default=2, type=int, help="select number")
parser.add_argument("--prev", type=int, help="select number")

args = parser.parse_args()
host, port = args.rooms.pop(0), int(args.rooms.pop(0))
rooms = requests.get(f'http://{host}:{port}').json()
if not rooms:
    print("Ошибка выполнения запроса:")
    # print(response)
    print("Http статус:", rooms.status_code, "(", rooms.reason, ")")
    sys.exit(1)
# rooms = {
#     "yard": [203, 119, 133, 276, 272],
#     "office": [268, 104, 1, 189, 176, 161, 123],
#     "kitchen": [210, 186, 63, 52],
#     "living_room": [95, 49, 187, 10, 3, 270]
# }
for room in args.rooms:
    for i, v in enumerate(rooms[room]):
        if v % args.future:
            rooms[room][i] += args.future - v % args.future
        elif args.prev:
            if v % args.prev == 0:
                rooms[room][i] //= args.prev

answer = []
for key in sorted(rooms.keys()):
    dct = {"room": key, "things": len(rooms[key]), "bigger": 0}
    dct['bigger'] = sum([v >= rooms[key][k] for k, v in enumerate(rooms[key][1:])])
    answer.append(dct)
# print(answer)
with open('past.json', 'w') as cat_file:
    json.dump(answer, cat_file)
