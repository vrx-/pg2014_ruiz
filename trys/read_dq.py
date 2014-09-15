# Write a function to read the data from the file discharge.dat, return a list of dates (as datetime objects) and discharge (ignoring any flags).

import datetime

def rd_dq(filename):
    f = open(filename)
    
    dates = []
    disch = []
    lines =[]
    for line in f.readlines():
        data = str(line).split('\t')
        lines.append(data)
    return lines
#        if data[0] != '#':
#            print data[1]
#            year = int(data[2].split('-')[0])
#            month= int(data[2].split('-')[1])
#            day  = int(data[2].split('-')[2])
#            date = datetime.date(year,month,day)
#            dates.append(date)
#            Q = int(data[4][:-2])
#            disch.append(Q)
#    return dates, disch


    
