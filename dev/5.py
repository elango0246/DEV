import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Load Zomato data (Replace 'zomato_data.csv' with your file)
zomato_data = pd.read_csv(r"C:\Users\LENOVO\Downloads\zomato_data.csv")

# Drop missing latitude and longitude
zomato_data = zomato_data.dropna(subset=['latitude', 'longitude'])

# Initialize the map
plt.figure(figsize=(10, 6))
m = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')

# Draw map features
m.drawcoastlines()
m.drawcountries()

# Plot Zomato locations
x, y = m(zomato_data['longitude'].values, zomato_data['latitude'].values)
m.scatter(x, y, s=5, c='red', alpha=0.6)

# Add title
plt.title("Zomato Locations")
plt.show()
