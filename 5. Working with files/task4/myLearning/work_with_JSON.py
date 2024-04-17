# # JSON - JavaScript Object Notation
# import json
# import pprint
# from random import randint
# from datetime import datetime
#
# str_json = """
# {
#     "response": {
#         "count": 4830804,
#         "friends_count": 7,
#         "items": [
#             {
#                 "id": 858069409,
#                 "first_name": "Светлана",
#                 "last_name": "Морозова",
#                 "can_access_closed": true
#
#             },
#             {
#                 "id": 708898616,
#                 "first_name": "Кристина",
#                 "last_name": "Матвеева",
#                 "can_access_closed": true
#             }
#         ]
#     }
# }"""
#
# data = json.loads(str_json)
# # print(type(data))
# # pprint.pprint(data)
# for item in data['response']['items']:
#     del item['id']
#     item['likes'] = randint(100, 200)
#     item['a'] = None
#     item['now'] = datetime.now().strftime('%d.%m.%y')
# pprint.pprint(data['response']['items'])
#
# with open('my.json', 'w') as file:
#     json.dump(data, file, indent = 3)
#
# # new_json = json.dumps(data, indent = 2)
# # print(new_json)
# #
# # print(json.loads(new_json))


# import json
#
# with open('my.json', 'r') as file:
#     data = json.load(file)
# print(json.dumps(data,indent = 3))

