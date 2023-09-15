import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('climate.csv')

years = data['Year']
co2_levels = data['CO2']
temperatures = data['Temperature']

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(years, co2_levels, color='red')
plt.title('CO2 Levels')
plt.xlabel('Year')
plt.ylabel('CO2 Level (ppm)')


plt.subplot(2, 1, 2)
plt.plot(years, temperatures, color='blue')
plt.title('Temperature Data')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')


plt.tight_layout()


plt.show()
