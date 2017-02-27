import re

# def claculate(ss):
#     for part in re.findall(r'\[slot=\d+,port=\d+\]', ss):
#         slot = re.match('')


if __name__ == '__main__':
    ss = '{[slot=1,port=1]=1, [slot=1,port=0]=0:[reserved=admin,group=1,number=1]}'


    dd = re.findall(r'\[slot=(\d+),port=(\d+)\]=(\d+)', ss)
    print(dd)