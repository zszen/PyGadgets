import os
import shutil

folder = 'podcasts'

make_sure_remove_all = input('你确定要清空%s吗? (OK / any)'%folder)

if make_sure_remove_all.startswith("OK"):
    print("清理开始")
    if os.path.exists(folder):
        for k in os.listdir(folder):
            if os.path.isdir(folder+'/'+k):
                shutil.rmtree(folder+'/'+k)
    print("清理完毕")
else:
    print("放弃清理")