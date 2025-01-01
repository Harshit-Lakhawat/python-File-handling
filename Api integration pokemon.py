import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response)     #gives http response code

    if response.status_code == 200:
        print("data retrieved")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data{response.status_code}")

pokemon_name = "squirtle"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name = {pokemon_info["name"]}")
    print(f"ID = {pokemon_info["height"]}")
    print(f"Height = {pokemon_info["weight"]}")
    print(f"Weight = {pokemon_info["id"]}")
    # Extract and print abilities
    abilities = [ability['ability']['name'] for ability in pokemon_info['abilities']]
    print(f"Abilities = {', '.join(abilities)}")
    # It takes all the ability names in the list (like ["torrent", "rain-dish"]) and 
    # joins them into a single string, separated by commas.
