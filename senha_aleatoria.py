#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random

def senha_aleatoria(mi, ma, n, e, dtype=int):

    # Iniciação de vetores com caracteres de senha.
    pre_senha = ''
    minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    maiusculo = list(map(lambda x: x.upper(), minusculo))
    numeros = list(map(lambda x: str(x), np.arange(0, 10)))
    especial = ['?', '!', '+', '-', '*', '/', '@', '#', '$', '%', '&']
    
    # Concatenação dos caracteres.
    for i in range(1):
        for i in range(mi):
            pre_senha += minusculo[random.randint(0,25)]
        for i in range(ma):
            pre_senha += maiusculo[random.randint(0,25)]
        for i in range(n):
            pre_senha += numeros[random.randint(0,9)]
        for i in range(e):
            pre_senha += especial[random.randint(0,10)]

    # Iniciação de vetores para embaralhamento da senha.
    m_palavra = list(map(lambda x: x, pre_senha))
    tam_palavra = len(m_palavra)
    senha_def = ''
    escolha = list(np.arange(tam_palavra))

    # Embaralhamento randômico da senha.
    for i in range(tam_palavra):
        tam_escolha = len(escolha)
        n = escolha[random.randint(0,tam_escolha-1)]
        senha_def += m_palavra[n]
        escolha.remove(n)
    
    return senha_def

