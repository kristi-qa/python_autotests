import requests
URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'd2e547d69c488772098bae0d233095e1'
HEADER = {'Content-Type' :'application/json', 'trainer_token':TOKEN}
body_pokemons = {
    "name": "Перчик",
    "photo_id": 36
}
body_pokemons_name = {
    "pokemon_id": "44324",
    "name": "Бруно",
    "photo_id": 36
 }
body_pokeball = {
    "pokemon_id": "44324"
}

'''response_create = requests.post(url= f'{URL}pokemons', headers = HEADER, json= body_pokemons )
print(response_create.text)'''

'''response_name = requests.put(url= f'{URL}pokemons', headers = HEADER, json= body_pokemons_name )
print(response_name.text)'''

response_pokeball = requests.post(url= f'{URL}trainers/add_pokeball', headers = HEADER, json= body_pokeball )
print(response_pokeball.text)