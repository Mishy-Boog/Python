x = 'pastel'

def myfunc():
  print("Quero comer um " + x)

myfunc()
'''
variavel fora da função
'''
######################################################
x = 'refri'

def myfunc():
  x = 'suco'
  print('Eu quero beber um ' + x) #pega a variavel local

myfunc()

 print('Eu quero beber um ' + x) #pega a variavel global


#######################################################

def myfunc():
  global x
  x = 'pipoca '

myfunc()

 print('Eu quero comer' + x) #vira global tbm

######################################################

x = 'pão de queijo'

def myfunc():
  global x
  x = 'bolinha de queijo' #muda a global dentro da função
myfunc()

print('Eu quero comer ' + x)




