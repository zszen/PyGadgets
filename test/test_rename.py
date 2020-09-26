import os,re

need_rename_path = None
replace_format = None

def rename_fun(res):
    substr = str(replace_format)
    for i in range(1,10):
        try:
            substr = substr.replace(f'${i}',res[i])
        except:
            break
    return substr

# path - 路径
# file_contain - 正则包含的文件范围
# file_except - 正则不包含的文件范围
# rename_condition - 正则要搜集提取的变量
# rename_changed - 替换提取的字符串
def rename_it(*, path, file_contain, file_except, rename_condition, rename_changed, isDebug = False):
    global replace_format
    replace_format = rename_changed
    for p,fds,fls in os.walk(path):
        for f in fls:
            if file_contain!=None and not re.search(file_contain, f):
                continue
            if file_except!=None and re.search(file_except, f):
                continue
            name_new = re.sub(rename_condition, rename_fun, f)
            if isDebug:
                print(f'{f} => {name_new}')
            else:
                os.rename(f'{p}/{f}',f'{p}/{name_new}')


if __name__ == "__main__":
    while True:
        need_rename_path = input('重命名文件夹：')
        need_rename_path = need_rename_path.strip()
        need_rename_path = re.sub(r'\\ ',' ', need_rename_path)
        print("need_rename_path", need_rename_path)
        rename_it(path = need_rename_path ,\
        file_contain=r'\.mp4$',\
        file_except=None,\
        rename_condition=r'(\d+)_(\d+)_(.*?)\_?(.mp4)',\
        rename_changed='$1$2_$3$4',\
        isDebug=False\
        )