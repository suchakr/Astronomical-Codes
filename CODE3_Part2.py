from astropy.coordinates import Angle
from astropy import coordinates as coord
from astropy import units as u
from astropy.time import Time
import pandas as pd
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u

sun_info_ra = []
sun_info_dec = []
n = 1
t = Time('2020-01-03 00:00:00')
for i in range(0, 100):
    t = t + n*u.year
    sun = coord.get_body('Sun', t)
    sun_info_ra.append([sun.ra])
    sun_info_dec.append([sun.dec])
ra = pd.DataFrame(sun_info_ra, columns=['ra'])
dec = pd.DataFrame(sun_info_dec, columns=['dec'])

# print(ra)
ra_lat = []
for i in range(0, 100):
    ra_lat.append(Angle(sun_info_ra[i]).deg)

b = pd.DataFrame(ra_lat, columns=['Latitude'])

dec_lat = []
for i in range(0, 100):
    dec_lat.append(Angle(sun_info_dec[i]).deg)

c = pd.DataFrame(dec_lat, columns=['Longitude'])
# print(b)
# plt.plot(ra_lat, label='Latitude')
plt.plot(dec_lat, label='Longitude')
plt.show()
