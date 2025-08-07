'''
#Regex ou Regular Expression
* De forma geral, o regex é como se fosse uma forma de encontrar,
substituir e extrair um único ou uma sequência de caracteristicas
de dentro de uma string.'''
# CARACTERE - qualquer letra, digito ou símbolo

import re

hey = 'carol@gmail.com.br'
# Findall
result = re.findall(r"(@.{1,8}\.)", hey)
print(result)
# Search
result = re.search(r"(@.{1,8}\.)", hey)
print(result)
# Split
result = re.split(r"(@.{1,8}\.)", hey)
print(result)
# Sub
result = re.sub(r"(@.{1,8}\.)", '@yahoo')
print(result)
