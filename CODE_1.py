#%%
## Code1
## Get the coordinates of the moon for 30 days 
## from a specific day – 
## right ascension, declination, latitude, and longitude.

#Importing the libraries
from astropy.coordinates import Angle
from astropy import coordinates as coord
from astropy import units as u
from astropy.time import Time
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
#%%

def get_moon_coords_for_30_days() :
    t = Time('2020-01-03 00:00:00')
    accumulator = []
    for i in range(0, 30):
        t = t + 1*u.day
        ymd = t.isot.split('T')[0]
        Moon = coord.get_body('Moon', t)
        Moon_ecliptic = Moon.transform_to(coord.GeocentricTrueEcliptic())
        accumulator.append ([ymd, Moon.ra.deg, Moon.dec.deg, Moon_ecliptic.lon.deg, Moon_ecliptic.lat.deg])
    df = pd.DataFrame(accumulator, columns=['time', 'ra', 'dec' , 'lon', 'lat'])
    return df

display(get_moon_coords_for_30_days())




#%%
#Making empty lists
Moon_info_ra = []
Moon_info_dec = []

t = Time('2020-01-03 00:00:00')

#Getting the data using coord.get_body() function of astropy
for i in range(0, 30):
    t = t + 1*u.day
    Moon = coord.get_body('Moon', t)
    Moon_info_ra.append([Moon.ra])
    Moon_info_dec.append([Moon.dec])

ra = pd.DataFrame(Moon_info_ra, columns=['ra']) 
dec = pd.DataFrame(Moon_info_dec, columns=['dec'])


# Appending the data
ra_lon = []
for i in range(0, 30):
    ra_lon.append(Angle(Moon_info_ra[i]).deg)
    

b = pd.DataFrame(ra_lon, columns=['Latitude'])  ## Review: Why is it latitude?
display(b)

# Again Appending the data
dec_lat = []
for i in range(0, 30):
    dec_lat.append(Angle(Moon_info_dec[i]).deg)

c = pd.DataFrame(dec_lat, columns=['Longitude'])    ## Review: Why is it longitude?
display(c)


# plotting the data
# plt.plot(ra_lon, label='Longitude')
plt.plot(dec_lat, label='Latitude')
plt.xlabel('Days')
plt.ylabel('Latitude')
# plt.xlabel('Days')
# plt.ylabel('Longitude')
plt.legend()
plt.show()

# %%
