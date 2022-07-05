import numpy as np

q_matrix= np.zeros((6,4), dtype=np.float64) 

print (q_matrix)

#atribuição dos valores de recompensa inicial da matriz

q_matrix[-1:,:]=10 #operação fixar que no estado 6 a recompensa é 10
q_matrix[:5,:]=-1

print (q_matrix)

#Definição das ações

actions_names = ['UP', 'DW', 'LF', 'RG']
actions_names

alpha = 0.5
gamma = 1

print(f'O alpha determinado foi de {alpha} \nO gamma determinado foi de {gamma}')

"""
  Criação da matriz de recompensas
    Sabendo que no estado 6 eu tenho uma recompensa de 10 e nos demais tenho -1
"""
rewards_matrix = np.array([-1]*6)
rewards_matrix[5] = 10
rewards_matrix

"""
  Definição de caminhos
    Para salvar os caminhos foram usadas as informações dadas 
    inicialmente de estado inicial, ação e estado final
    Vale ressaltar que a matriz está começando do estado 0 
    invés do estado 1 como descrito no exercício
    paths possui 5 caminhos possíveis passados
"""
#[estado, ação, próximo estado]

paths = [[[0, 'UP', 1],[1, 'DW', 1],[1, 'RG', 1], 
          [1,'LF', 0],[0, 'RG', 2], [2, 'LF', 2], 
          [2, 'LF', 2], [2, 'UP', 4], [4, 'RG', 5]],
         [[0, 'UP', 2],[2,'UP',4],[4,'LF',2],
          [2,'LF',2],[2,'LF',4],[4,'RG',5]],
         [[0, 'DW', 0],[0, 'UP', 2], [2, 'RG', 4], 
          [4, 'UP', 4],[4, 'DW', 4], [4, 'LF', 4], 
          [4, 'DW', 2], [2, 'UP', 4], [4, 'RG', 4], 
          [4, 'RG', 5]],
         [[0, 'UP', 2],[2, 'RG', 3], [3, 'UP', 5]],
         [[0, 'LF', 0], [0, 'UP', 0], [0, 'UP', 2], 
         [2, 'UP', 4], [4, 'LF', 4], [4, 'DW', 2], 
         [2, 'UP', 4], [4, 'UP', 4], [4, 'UP', 4], 
         [4, 'DW', 2], [2, 'UP', 2], [2, 'LF', 2], 
         [2, 'RG', 3], [3, 'UP', 5]]]
         
"""
  Função auxiliar
    Imprime as matrizes no formato do ambiente
"""

def print_matrix(matrix):
    print('[' + str(matrix[4]) + ' ' + str(matrix[5]))
    print(str(matrix[2]) + ' ' + str(matrix[3]))
    print(str(matrix[0]) + ' ' + str(matrix[1]) + ']\n')


print_matrix(q_matrix)

"""
  Atualização dos valores da matriz
    Função desenvolvida considerando as recompensas para quando o o estado 
    final for igual ao estado inicial
"""

def update_matrix(state, action, next_state, rewards_matrix, q_matrix, alpha, gamma):
  
  selected_reward = -10

  if next_state != state:
    selected_reward = rewards_matrix[state]
 
  estimate_q = selected_reward + gamma * max(q_matrix[next_state]) 
  q_value = q_matrix[state][action] + alpha*(estimate_q - q_matrix[state][action])
  return q_value

"""
  Atualizaçao das matrizes:
    As trajetórias são iteradas e a cada um dos passos 
    fornecidos que tem o valor da matriz q 
    é atualizado levando em consideração a ação desejada e o estado que obteve

"""

for i in range(len(paths)):
  print(f'Está atualizando a trajetórias {i}')
  for j in range(len(paths[i])):
    state, action, next_state = paths[i][j]
    print(f'No passo {j} na trajetória {i}')
    print(f'Estado {state}')
    print(f'Ação {action}')
    print(f'Próximo estado {next_state}')
    if action == 'UP':
      q_value = update_matrix(state, 0, next_state, rewards_matrix, q_matrix, alpha, gamma)
      print(f'Q_value {q_value}')
      q_matrix[state][0] = q_value
      print_matrix(q_matrix)
    if action == 'DW':
      q_value = update_matrix(state, 1, next_state, rewards_matrix, q_matrix, alpha, gamma)
      print(f'Q_value {q_value}')
      q_matrix[state][1] = q_value
      print_matrix(q_matrix)
    if action == 'LF':
      q_value = update_matrix(state, 2, next_state, rewards_matrix, q_matrix, alpha, gamma)
      print(f'Q_value {q_value}')
      q_matrix[state][2] = q_value
      print_matrix(q_matrix)
    if action == 'RG':
      q_value = update_matrix(state, 3, next_state, rewards_matrix, q_matrix, alpha, gamma)
      print(f'Q_value {q_value}')
      q_matrix[state][3] = q_value
      print_matrix(q_matrix)
