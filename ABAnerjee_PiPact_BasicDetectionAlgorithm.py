#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd #Importing a necessary library for data analysis

data = pd.read_csv("/home/pi/reference_code/ObstructionTypeScans/1.44m_AluminumFoil2.csv") #Reading an example .csv file containg RSSI values


# In[9]:


count = 0 #Measures how long devices were in contact for in seconds. This is optimized for indoors
out_count = 0 #Meausres how long devices were in contact for in seconds. This is optimized for outdoors.

for index, row in data.iterrows():
    if row["RSSI"] >= -63:
        count += 1 #Each row in the data is offset by a second. Each time RSSI is above -63, the two devices were within 2m. Optimized for indoors.
for index, row in data.iterrows():
    if row["RSSI"] >= -54:
        out_count += 1 #Each row in the data is offset by a second. Each time RSSI is above -54, the two devices were within 2m. Optimized for outdoors.

if count >= 600:
    print("COVID-19 Potential Exposure warning!" + " Contact with infected individual within 2m for " + str(int(count/60)) + " minutes." + " Please consult with local health department.")
if count < 600:
    print("No Actions necessary. " + "Devices within 2m for " + str(int(count/60)) + " minutes")    
if out_count >= 600:
    print("COVID-19 Potential Exposure warning!" + " Came into contact with infected individual within 2m for " + str(int(out_count/60)) + " minutes" + " Please consult with local health department.")
if out_count < 600:
    print("No Actions necessary. " + "Devices within 2m for " + str(int(out_count/60)) + " minutes")
        

