#!/usr/bin/env python
# coding: utf-8

# In[9]:


import yfinance as yf
import matplotlib.pyplot as plt


# In[10]:


acoes = ['AAPL', 'MSFT', 'PETR4.SA', 'BBDC4.SA']


# In[16]:


dados_acoes = yf.download(acoes,
                          period='1d',
                          start='2022-01-01')


# In[28]:


dados_acoes['Close'].plot()
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Rastreador de ações')
plt.legend(acoes, fontsize=7)
plt.show()


# In[29]:


dados_normalizados = dados_acoes['Close'] / dados_acoes['Close'].iloc[0]
dados_normalizados.plot()
plt.xlabel('Data')
plt.ylabel('Preço Normalizado')
plt.title('Rastreador de ações')
plt.legend(acoes, fontsize=7)
plt.show()


# In[ ]:




