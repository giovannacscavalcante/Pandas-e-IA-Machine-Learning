#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)
display(funcionarios_df)
display(clientes_df)
display(servicos_df)


# In[3]:


import pandas as pd
funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
print(funcionarios_df)

funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Beneficios'] + funcionarios_df['Impostos'] + funcionarios_df['VT'] + funcionarios_df['VR'] 
print("O valor total da folha salarial é de R$ {:,} reais".format(sum(funcionarios_df['Salario Total'])))
valor = sum(funcionarios_df['Salario Total'])
reajuste = 0.10
aumento = reajuste * valor
valorFinal = valor + aumento 
print("")
print("Com o aumento de 10% na folha salarial o valor total é R$ {:,} reais".format(valorFinal))


# 

# In[ ]:




