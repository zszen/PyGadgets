import re

str_new = ''

with open('test/format.txt','r') as f:
    # lines = f.readlines()
    status = 0
    count_idx = 0
    for line in f.read().splitlines():
        if line == '':
            continue
        elif re.search(r'^    ',line):
            if status!=2:
                count_idx = 0
                status = 2
                str_new+=f'名称|热键\n'
                str_new+=f'-|-\n'
            if count_idx%2==0:
                str_new+=f'{line.lstrip(" ")} | '
            else:
                str_new+=f'{line.lstrip(" ")}\n'
            count_idx+=1
            # print(line)
        else:
            status = 1
            # print(re.sub(r'\n','',line))
            str_new +=f'# {line}\n'

print(str_new)