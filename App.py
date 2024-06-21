# -*- coding: utf-8 -*-
"""helloworld

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bie8_wNdNk8pc19Wo5aUTA9fUkkg-aHq
"""

# libraries
import numpy as np
from datetime import datetime


# Hello world function
def hiworld() -> None:
    ''' Imprime el string 'hello world'
    '''
    return 'Hello World'

# Rock paper scissors function
def rps(rps:string) -> None:
    ''' Función interactiva que permite jugar piedra papel o tijera con la maquina, recibe
        un string que debe ser 'r', 'p' o 's', si es ninguno, la iteración termina.
    '''
    
    if play not in ['r', 'p', 's']:
        return "Invalid input. Please enter 'r' for rock, 'p' for paper, or 's' for scissors."
        

    r = np.random.randint(0, 3)
    d = ['rock', 'paper', 'scissors']
    out = d[r]

    if out[0] == play:
        return (f'{out}, it\'s a draw!')
    elif (out == 'rock' and play == 's') or (out == 'scissors' and play == 'p') or (out == 'paper' and play == 'r'):
        return (f'{out}, you lose!')
    else:
        return (f'{out}, you win!')


# Function to print the current date
def print_date() -> None:
    ''' Función que imprime la fecha y hora del momento.
    '''
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     return f'Current date and time: {current_date}'

def is_leap_year(year: int) -> bool:
    """Function to calculate if it is a leap year."""
    if year%400 == 0: # Multiples of 400 are leap years.
        leap_year = True
    elif year%100 == 0: # The rest of the multiples of 100 are not leap years.
        leap_year = False
    elif year%4 == 0: # The rest of the multiples of 4 are leap years.
        leap_year = True
    else: # The rest of the years are not leap years.
        leap_year = False

    if leap_year:
        print(str(year), "is a leap year.")
    else:
        print(str(year), "is not a leap year.")

assert is_leap_year(2024)== 'is a leap year.'
assert hiworld() == 'Hello World'
assert rps('rock') == "Invalid input. Please enter 'r' for rock, 'p' for paper, or 's' for scissors."
assert type(print_date()) == str
# Example usage
