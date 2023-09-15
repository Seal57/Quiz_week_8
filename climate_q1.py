import sqlite3

# Connect to the database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Define lists to store data
Year = []
CO2 = []
Temperature = []


# Fetch values from the database
cursor.execute('SELECT Year, CO2, Temperature, FROM ClimateData')
data = cursor.fetchall()

# Populate lists with corresponding values
for row in data:
    Year.append(row[0])
    CO2.append(row[1])
    Temperature.append(row[2])

# Close the connection
conn.close()

# Test print to verify data
print("Year:", Year)
print("CO2:", CO2)
print("Temperature:", Temperature)
