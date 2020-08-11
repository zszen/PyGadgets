import os
from PIL import Image
import sqlite3

root = os.path.dirname(__file__)

tablename = 'imagesize'

conn = sqlite3.connect(f'{root}/watch.db')
cur = conn.cursor()
cur.execute(f'''create table IF NOT EXISTS {tablename} (
    id integer primary key autoincrement,
    name varchar(128) not null,
    path varchar(1024) not null,
    size varchar(64) not null
);''')
conn.commit()

path = input('watch path: ')
path = path.rstrip()
path = path.replace('\ ',' ')
if not os.path.isdir(path):
    path = os.path.dirname(path)
for dir,folders,files in os.walk(path):
    for filename in files:
        if filename.startswith('.'):
            continue
        im = Image.open(dir+'/'+filename)
        isExist = False
        cur.execute(f'select * from {tablename} where name=\'{filename}\' and path=\'{dir}\' ')
        res = cur.fetchall()
        for unit in res:
            isExist = True
            id = unit[0]
            size = unit[3]
            if not size==f'{im.size}':
                print(f'ERR: {filename} org size:{size}, now size:{im.size}')
                # cur.execute(f'update {tablename} set size=\'{im.size}\' where id={id}')
        if not isExist:
            cur.execute(f'insert or replace into {tablename} (name,path,size) values(\'{filename}\',\'{dir}\',\'{im.size}\')')
        im.close()
            
conn.commit()
conn.close()

print('==DONE==')