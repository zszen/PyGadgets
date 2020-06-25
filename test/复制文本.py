import pyperclip

str = '''
                        %.1f%%{
                            background: url(../images/nav_list1/sanjiao_list/%d.png) no-repeat;
                            background-size: 100%% 100%%;
                        }
'''

max = 180
str_out = ''
for i in range(1,max):
    str_out+=str%(float(i-1)/max*100,min(i,88))
    str_out+='\n'

pyperclip.copy(str_out)