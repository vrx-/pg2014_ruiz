'''
Homework 3
Re-do Problem 1.3
V.Ruiz
'''

def read_drifter(filename):
    '''
    Function to read data from the file "drifter.dat",
    return a dictionary based on the track name as indices, and values of lat/lon pairs.
    #Input : filename       Output: track (as a dictionary)
    '''
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

if __name__=='__main__':
    track=read_drifter('drifter.dat')
    print "track names in file:"
    print track.keys()
    print "track of GANDALF"
    print track['GANDALF']



