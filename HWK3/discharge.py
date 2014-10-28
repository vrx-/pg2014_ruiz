'''
Homework 3
Re-do Problem 1.3
V.Ruiz
'''

import datetime

def read_discharge(filename):
    '''
    Function to read the data from the file discharge.dat, 
    return a list of dates (as datetime objects) and discharge (ignoring any flags).
    Input : filename       Output: dates, disch
    '''
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    dates=[]
    disch=[]
    for line in lines:
        if line[0] != '#':
            data = str(line).split('\t')
            year=int(str(data[2]).split('-')[0])
            month=int(str(data[2]).split('-')[1])
            day=int(str(data[2]).split('-')[2])
            date= datetime.date(year,month,day)
            dates.append(date)
            Q=''
            for i in range(len(data[3])):
                if data[3][i].isdigit():
                    Q+=data[3][i]
            disch.append(int(Q))
            
    return dates, disch;

if __name__=='__main__':
    dates, discharge=read_discharge('discharge.dat')
    for i in range(len(dates)):
        print dates[i], discharge[i]
    print "dates is", type(dates), "of", type(dates[0])
    print "discharge is", type(discharge), "of", type(discharge[0])


