'''
Homework 1
Problems 3 and 4
V.Ruiz
'''

# P3: Function to read the data from the file discharge.dat, return a list of dates (as datetime objects) and discharge (ignoring any flags).
#Input : filename       Output: dates, disch

import datetime

def read_discharge(filename):
    
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


#P2: Function to read data from the file "drifter.dat", and return a dictionary based on the track name as indices, returning a list of lat/lon pairs.
#Input : filename       Output: track (dict)

def read_drifter(filename):
    
    f= open(filename,'r')
    lines= f.readlines()
    f.close()
    
    track = {}
    i=0
    for line in lines:
        if line.split('\t')[0]== 'Track' :
            key = line.split('\t')[1]
            values =[]
        if line.split('\t')[0]== 'Trackpoint':
            pos = line.split('\t')[1]
            lat = float(pos.split(' ')[1])
            lon = float(pos.split(' ')[3])
            values.append((lat,lon))
            track[key]= values
    return track