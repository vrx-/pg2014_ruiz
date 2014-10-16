'''
Homework 2
Problem 4
Discharge data Class and methods
V.Ruiz, October 2014
'''
import numpy as np
import datetime
from matplotlib import pyplot as plt

c = 0.0283168 #convert from cubic feet to cubic meter

class discharge_data(object):
    """Discharge object (datetime,discharge)"""
    def __init__(self, filename):
        self.filename=filename
        f = open(filename,'r')
        lines = f.readlines()
        f.close()
        dates=np.array([])
        disch=np.array([])
        for line in lines:
            if line[0] == 'U':
                data = str(line).split('\t')
                year=int(data[2].split('-')[0])
                month=int(data[2].split('-')[1])
                day=int(data[2].split('-')[2])
                date=datetime.date(year,month,day)
                dates=np.append(dates,date)
                if data[3].isdigit():
                    Q=float(data[3])*c
                    disch=np.append(disch,Q)
                else:
                    disch=np.append(disch,float('NaN'))
        self.dates = dates
        self.discharge= disch
        
    def extract_year(self,year):
        """Return dates and discharges for specified year"""
        years=np.array([(d.year) for d in self.dates])
        indx=np.where(years==year)
        return self.dates[indx], self.discharge[indx]
            
    def plot(self):
        """Plot discharge for the whole time series"""
        plt.plot(self.dates,self.discharge)
        plt.title('Hidrograph')
        plt.ylabel('Discharge [$m^3$/$s$]')
        plt.show()


        

        