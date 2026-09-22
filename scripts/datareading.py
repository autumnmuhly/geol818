def readmydata():
    """ 
    Reads EQ information out of a data file.
    Returns mag,lat,lon.
    """
    mag=[]
    lat=[]
    lon=[]
    with open('../data/All.deep_sorted','r') as file:
        for line in file:
            print(line)
            items = line.split()
            mag.append(float(items[3]))
            lat.append(float(items[5]))
            lon.append(float(items[6]))
            # if 6 < mag < 8:
            #     print('yay')
    return mag,lat,lon

