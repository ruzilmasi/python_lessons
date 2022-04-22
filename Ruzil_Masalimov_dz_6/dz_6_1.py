f_url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
f_name = 'nginx_logs.txt'

out = []
with open(f_name, 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr = (line[:line.find("-") - 1])
        request_type = (line[line.find('"') + 1:line.find(' /')])
        requested_resource = (line[line.find(' /') + 1:line.find('HTTP') - 1])
        result = (remote_addr, request_type, requested_resource)
        out.append(result)

for el in out:
    print(el)
