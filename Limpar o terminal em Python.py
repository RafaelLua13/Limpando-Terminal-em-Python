# Nome do projeto: Limpar Terminal em Python
# Linguagem: Python 
# Utilizações: Imports, Repetições, Variáveis e Funções
# Autor: Rafael Lua de Sousa e Silva - rafaellua13
# Referências: 
  #https://pt.stackoverflow.com/questions/72678/como-limpar-o-console-no-python

  #https://stackoverflow.com/questions/2084508/clear-terminal-in-python



# Limpar com prints normais
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
print('\033c')




# Usando o teclado
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
# Use Ctl + L no teclado para limpar terminal




# Importando OS
import os
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
os.system('clear') # vai ser = 0, se quiser que apareça um valor, coloque este comando em uma variavel e some o valor nela
                   # Demonstrado a seguir:




# Importando OS mais elaborado com mensagem
import os
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
x = os.system('clear') + 1 
if x == 1:
  print('Apagou-se')




# Usando espaços
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
print ('\n' * 200) 
print('Aqui em baixo.')




# Usando Espaços com OS
import os
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
# Exatamente o numero de espaços que tem o terminal
print("\n" * os.get_terminal_size().lines) 
# Descobrir tamanho do terminal
print(os.get_terminal_size())




# Usando comandos de terminal em print
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
print("\x1b[2J\x1b[5;20H" + 'Mensagem') 
# \x1b = printar um \n
# \x1b[2J = apagar terminal e printar a mesma quantidade de linhas anterior + um \n
# H = colunas 
# [5; = linhas
# [5;20H" = linha 5, coluna 20
# + Mensagem = mostrar palavra no local (não precisa ser usado) 




# importando curses com variavel
import curses
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
qualquerNome = curses.initscr()
qualquerNome.clear()
qualquerNome.refresh()




# importando OS e utilizando lambda:
import os
for x in range(1):
  print('Esta mensagem será apagada :)')
potato = input('->')
qualquerNome = lambda: os.system('clear')
qualquerNome()



