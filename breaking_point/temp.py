import csv

from StringIO import StringIO

if __name__ == '__main__':
    # f_name = '0VM_RESTART_CS_AS_31.csv'
    # ff = open('0VM_RESTART_CS_AS_31.csv', 'r')
    # reader = csv.DictReader(ff)
    # for row in reader:
    #     print row
    dd = {'Test N':123, 'GG':{'Hello':'World'}}
    io = StringIO()
    # gg = csv.DictWriter(io)
    # print gg.