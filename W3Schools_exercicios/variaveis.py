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
############################################################3

x, y, z = 'Uva', 'Banana', 'Caju'

print(x, y, z)

'''
saída = Uva Banana Caju
atribuição de vários valores em uma só linha
'''

###############################
x = y = z = 'Laranja'
print(x)
print(y)
print(z)

'''
saída = Laranja
        Laranja
        Laranja
É possivel atribuir o mesmo valor a atributos diferentes
'''
###############################################################3
frutas = ["Maçã", "Banana", "Uva"]
x, y, z = frutas
print(x)
print(y)
print(z)

pessoas = ('Fulano', 'Ciclano', 'Beltrano')
a, b, c = pessoas
print(a)
print(b)
print(c)
'''
saída = Maçã
        Banana
        Uva
        Fulano
        Ciclano
        Beltrano
É possivel retirar atributos de listas e tuplas
'''
###################################################
a = 'Estou com fome'
print(a)

b = 'Estou'
c = 'com'
d = 'fome'
print(b, c, d)

e = 'Estou '
f = 'com '
g = 'fome'

print(e + f + g)


