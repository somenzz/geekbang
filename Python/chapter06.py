# import json

# params = {
#     'symbol': '123456',
#     'type': 'limit',
#     'price': 123.4,
#     'amount': 23
# }

# params_str = json.dumps(params)

# print('after json serialization')
# print('type of params_str = {}, params_str = {}'.format(type(params_str), params_str))

# original_params = json.loads(params_str)

# print('after json deserialization')
# print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

# ########## 输出 ##########




import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))
