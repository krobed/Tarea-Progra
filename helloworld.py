import numpy as np

# Hello world function
def hiworld():
  print('Hello World')

# Rock paper scissors function
def rps():
  play = input('Choose between rock, paper or scissors (r, p or s): ')
  r = np.random.randint(0,2)
  d = ['rock', 'paper','scissors']
  out= d[r]
  if out[0] == play:
    print(f'{out}, it's a draw!')
  elif out == 'rock' and play=='p':
    print f'{out}, you lost!'
  elif play == 'p' and out=='scissors':
    print f'{out}, you lose!'
  else:
    print f'{out}, you win!
  again= input('Play again? (y/~): ')
  if again=='y':
    rps()
