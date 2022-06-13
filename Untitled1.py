#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt 

datafile= np.genfromtxt('jmars_nspring.csv' , delimiter=',' , skip_header=3)
datafile2 = np.genfromtxt('jmars_nsummer.csv' , delimiter=',' , skip_header=3)

lon = datafile[:,0]%360 
lat = datafile [:,1]
ls = datafile [:,2]
lt = datafile [:,3]
radiance = datafile[8,7:149]
time = datafile[:,4]
temp = datafile[:,6]
                          
time2 = datafile2[:,4]
temp2 = datafile2[:,6]
lon2 = datafile2[:,5]
lat2 = datafile2 [:,3]
                          


# In[2]:


# for scatter plot
plt.scatter (lon, lat, c=ls, cmap = 'jet')
plt.title= ("Season Coverage")
plt.xlabel ('Longitude')
plt.ylabel ('Latitude')
plt.colorbar()


# # For Northern Spring

# In[3]:


# for scatter plot
plt.scatter (time, temp,)
plt.title= ("Season Coverage")
plt.xlabel ('Time')
plt.ylabel ('Brightness Temperature')


# # For Northern Summer

# In[4]:


# for scatter plot
plt.scatter (time2, temp2, )
plt.title= ("Season Coverage")
plt.xlabel ('Time')
plt.ylabel ('Brightness Temperature')


# In[5]:


plt.scatter(lon2, lat2, c=temp2, cmap= 'Spectral')
plt.title= ("Season Coverage")
plt.xlabel ('Longitude')
plt.ylabel ('Latitude')
plt.colorbar()


# In[6]:


plt.scatter(time2, temp2)
plt.title= ("Season Coverage")
plt.xlabel ('Time')
plt.ylabel ('Temp')
plt.colorbar()


# In[ ]:





# In[ ]:





# In[ ]:




