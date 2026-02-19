#!/usr/bin/env python
# coding: utf-8

# ## ABANDONO ESCOLALAR CONALEP
# 
# 
# Se realizará un análisis de datos sobre el abandono escolar en México durante 2025, utilizando información abierta disponible en Datos.gob.mx correspondiente al CONAL (Censo Nacional de Asistencia y Logros Educativos). 
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns


# In[2]:


df = pd.read_csv('cd_Abandono_Escolar_CONALEP_2025.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.describe()


# In[6]:


df.nunique()


# In[7]:


df.sort_values(by="porcentaje_abandono_escolar", ascending=False)


# In[8]:


#groupby() convierte la variable agrupada en índice

#reset_index()  regresa el índice a columna normal


# In[9]:


promedio_estado = (df.groupby("entidad")["porcentaje_abandono_escolar"].mean()).reset_index()


# In[10]:


promedio_estado


# In[11]:


top7 = promedio_estado.sort_values(by="porcentaje_abandono_escolar", ascending=False).head(7)

print(top7)


# In[ ]:


plt.figure()
plt.bar(top7["entidad"], top7["porcentaje_abandono_escolar"])
plt.xticks(rotation=45)
plt.xlabel("Estado")
plt.ylabel("Promedio de abandono (%)")
plt.title("Top 7 Estados con Mayor Abandono Escolar")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




