import json

my_dict = {}

f_name1 = 'users.csv'
f_name2 = 'hobby.csv'
with open(f_name1, 'r', encoding='utf-8') as f1:
    with open(f_name2, 'r', encoding='utf-8') as f2:
        for line1 in f1:
            line2 = f2.readline().strip()
            if not line2:
                line2 = None
            if line1 not in my_dict:
                my_dict[line1.strip()] = line2
        content = f2.read()

with open('users_hobbys.json', 'w', encoding='utf-8') as out:
    dict_as_string = json.dumps(my_dict, ensure_ascii=False)
    out.write(dict_as_string)
with open('users_hobbys.json', 'r', encoding='utf-8') as f:
    content2 = f.read()
    result = json.loads(content2)
print(result)
