# Como usar uma list compreheension
'''nova_lista = [2 * i for i in range(10)]
# [Expressão for membro in iteravel]
print(nova_lista)'''


'''def aprovar_pessoa(nome):
    return nome + ' - Aprovado! '


nomes = ['Larissa', 'rafael', 'lucas', 'john']

print([nome + ' Aprovado ' for nome in nomes])
print([aprovar_pessoa(nome) for nome in nomes])
'''

'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

from pprint import pprint
pprint([[i for i in range(1, 6)] for x in range(5)])
