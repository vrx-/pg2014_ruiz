#Function to read data from the file drifter.dat.  Return a dictionary based on the track name as indices, returning a list of lat/lon pairs.

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