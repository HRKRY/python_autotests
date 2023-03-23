import requests

token = 'e1ed9e9c1c33e72ee99d4ddfd7b5141d'

response0 = requests.post('https://pokemonbattle.me:9104/trainers/reg', headers = {'Content-type' : 'application/json'},
                         json = {'trainer_token': token, 'email':'iamqwerty@kkllkk.ru','password':'PokemonsPass123'})
print(response0.text)

response1 = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers = {'Content-type' : 'application/json'},
                         json = {'trainer_token': token})
print(response1.text)

response2 = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-type' : 'application/json', 'Trainer_token':token},
                         json = {'name':'PyTestPokemon','photo':'https://dolnikov.ru/pokemons/albums/003.png'})
print(response2.text)

response3 = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-type' : 'application/json', 'Trainer_token':token},
                         json = {'pokemon_id':'6713','name':'NewNameToPyTestPokemon','photo':'https://dolnikov.ru/pokemons/albums/005.png'})
print(response3.text)

response4 = requests.post('https://pokemonbattle.me:9104//trainers/add_pokeball', headers = {'Content-type' : 'application/json', 'Trainer_token':token},
                         json = {'pokemon_id':'6713'})
print(response4.text)