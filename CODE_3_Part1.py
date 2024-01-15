#Importing the libraries
import numpy as np
from astropy.coordinates import get_sun, get_moon, AltAz, EarthLocation
from astropy.time import Time
import astropy.units as u
import matplotlib.pyplot as plt

# Function to compute angular separation between two celestial objects
def angular_separation(coord1, coord2):
    return coord1.separation(coord2)

# Function to generate time array for 100 years with sampling every n days
def generate_time_array(start_time, end_time, n_days):
    time_array = Time(
        np.arange(start_time.jd, end_time.jd, n_days), format='jd')
    return time_array

# Function to compute positions of sun and moon for given time array
def compute_positions(time_array, observer_location):
    sun_coords = get_sun(time_array).transform_to(
        AltAz(obstime=time_array, location=observer_location))
    moon_coords = get_moon(time_array).transform_to(
        AltAz(obstime=time_array, location=observer_location))
    return sun_coords, moon_coords

# Function to plot angular separation vs time
def plot_angular_separation(time_array, angular_separation_values, n_days):
    plt.plot(time_array.datetime, angular_separation_values,
             label=f'Sampling every {n_days} days')
    plt.xlabel('Time')
    plt.ylabel('Angular Separation (degrees)')
    plt.legend()
    plt.show()


# Set the start and end times
start_time = Time('1924-01-01', format='iso')
end_time = start_time + 36525 * u.day  # 100 years in days

# Define the observer's location (e.g., latitude and longitude for a specific place)
observer_location = EarthLocation(lat=40 * u.deg, lon=-75 * u.deg)

# Define the sampling intervals (N = 100, 10, 1)
sampling_intervals = [100, 10, 1]

# Loop through each sampling interval
for n_days in sampling_intervals:
    # Generate time array
    time_array = generate_time_array(start_time, end_time, n_days)

    # Compute positions of sun and moon
    sun_coords, moon_coords = compute_positions(time_array, observer_location)

    # Compute angular separation
    angular_separation_values = angular_separation(sun_coords, moon_coords)

    # Plot the results
    plot_angular_separation(time_array, angular_separation_values, n_days)
