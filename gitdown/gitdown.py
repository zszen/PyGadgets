import os
import re

# change it
project_remote_git = input('git addr: ')
# 'https://github.com/ZackaryShen/TencentVideoD.git'

#solid const
root_path = '/Users/zszen/Desktop/network/git'

res = re.search(r'([^/]+)/([^/]+)(?!.*/)',project_remote_git)
project_name = f'{res.group(2)}[{res.group(1)}]'
project_path = root_path+'/'+project_name
# print()
if not os.path.exists(root_path):
    raise Exception('root path don\'t exist')

# print(os.path.exists(project_path))

if not os.path.exists(project_path):
    os.mkdir(project_path)

has_subpath = False
for k in os.listdir(project_path):
    if os.path.isdir(project_path+'/'+k):
        has_subpath=True
        break
# print([k for k in os.listdir(project_path) if os.path.isdir(project_path+'/'+k)][0])

if not has_subpath:
    os.chdir(project_path)
    os.system(f'git clone {project_remote_git}')
else:
    os.chdir([k for k in os.listdir(project_path) if os.path.isdir(project_path+'/'+k)][0])
    os.system(f'git fetch origin/master')
    os.system(f'git reset --hard origin/master ')
    os.system(f'git pull')

with open(project_path+'/'+'readme.txt','w') as f:
    f.write(project_remote_git+'\n')

git_path = project_path+'/'+[k for k in os.listdir(project_path) if os.path.isdir(project_path+'/'+k)][0]
os.system(f'code {git_path}')