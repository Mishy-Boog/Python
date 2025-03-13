#minuscula e maiuscula contam como variaveis diferentes
#aspas simples ou duplas na variavel são a mesma coisa
x = 6
y = "Fulano"
print(x, y)
'''
saída = 6, Fulano
'''

##################################################################

x = 9
x = "Ciclano"
print(x)
'''
saída = Ciclano
as variaveis podem receber outro valor independente do seu tipo
'''

##################################################################

x = str(3)
y = int(4)
z = float (5)

print(x, y, z)
'''
saída = 3 4 5.0
É possivel especificar usando a conversão
'''
###################################################################

x = 'Fulano'
y = 7

print(type(x))
print(type(y))
'''
saída = str
        int
descobrindo o tipo da variavel
'''
