import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
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
fig = plt.figure(figsize=(12,6))
ax=plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.LAND, color="oldlace")
plt.scatter(lon,lat, c='blue',transform=ccrs.PlateCarree())
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
plt.title('Earthquake Locations')
plt.show()