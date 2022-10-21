from fastapi import FastAPI
from random import randrange
from enum import Enum

app = FastAPI()

class Weapon(str, Enum):
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    spock = 'spock'
    lizard = 'lizard'

@app.get('/')
async def read_root():
    return {'message': 'Hello World'}

@app.get('/shoot')
async def shoot(weapon: Weapon):

    game_key = {
        ('lizard', 'spock'): 'Lizard poisons spock! You lose!',
        ('lizard', 'paper'): 'You win! Lizard eats paper!',
        ('lizard', 'rock'): 'You lose! Rock crushes lizard!',
        ('lizard', 'scissors'): 'You lose! scissors decapitates lizard!',
        ('lizard', 'lizard'): 'Draw! lizard and lizard are a tie!',
    
        ('spock', 'spock'): 'Draw! spock and spock',
        ('spock', 'paper'): 'You lose! Paper disproves Spock',
        ('spock', 'rock'): 'You win! Spock vaporizes rock',
        ('spock', 'scissors'): 'You win! Spock smashes scissors',
        ('spock', 'lizard'): 'You lose! Lizard poisons Spock',
        
        ('rock', 'paper'): "You lose.",
        ('rock', 'scissors'): "You won!",
        ('rock', 'lizard'): "Rock smashes lizard! You lost!!",
        ('rock', 'rock'): "It's a tie.",

        ('paper', 'rock'): "You won!",
        ('paper', 'spock'): "Paper disproves Spock! You won!",
        ('paper', 'scissors'): "You lost.",
        ('paper', 'paper'): "It's a tie.",

        ('scissors', 'spock'): "Spock smashes scissors! You lost!",
        ('scissors', 'rock'): "Rock smashes scissors!You lost.",
        ('scissors', 'paper'): "Scissors cuts paper! You won!",
        ('scissors', 'scissors'): "It's a tie.",
    }
    weapons = ['rock', 'paper', 'scissors','spock','lizard']
    opp_weapon = weapons[randrange(0, 3)]
    message = game_key[(weapon, opp_weapon)]
    result = {'user_weapon': weapon, 'opponent_weapon': opp_weapon, 'message': message}

    return result