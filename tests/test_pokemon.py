import requests
import pytest

token = 'e1ed9e9c1c33e72ee99d4ddfd7b5141d'

def test_get_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_trainer_name_json():
    response = requests.get('https://pokemonbattle.me:9104/trainers', 
                            params = {'trainer_id' : 3517 })
    assert response.json()['trainer_name'] == 'IAMTRAINERMZFKA'