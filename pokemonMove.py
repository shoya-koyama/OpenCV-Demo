import requests

def get_pokemon_moves(pokemon_name):
    # PokeAPIのURL
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    # PokeAPIからデータを取得
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"{pokemon_name}のデータは存在しません"
    
    data = response.json()
    
    # ポケモンの技リストを取得
    moves = [move['move']['name'] for move in data['moves']]
    
    return moves

def get_pokemon_series(pokemon_name):
    # PokeAPIのURL
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    # PokeAPIからデータを取得
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"{pokemon_name}のデータは存在しません"
    
    data = response.json()
    
    # ポケモンの登場するゲームシリーズリストを取得
    series = [game['version']['name'] for game in data['game_indices']]
    
    return series

# 例として、Pikachuの技を取得
pokemon_name = "Pikachu"
# moves = get_pokemon_moves(pokemon_name)
# print(f"{pokemon_name}の技:")
# for move in moves:
#     print(move)

series = get_pokemon_series(pokemon_name)
print(f"{pokemon_name}の出現シリーズ:")
for game in series:
    print(game)
