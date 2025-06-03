# JSON -> JavaScript Object Notation (extensão .json)
# é uma estrutura de dados que permite a serialização de objetos em texto simples,
# para facilitar a transmissão de dados através da rede, APIs web ou outros meios
# de comunicação. O JSON suporta os seguintes tipos de dados:
# NÚMEROS: podem ser inteiros ou flutuante, como 42 ou 3.14;
# STRINGS: são cadeias de caracteres, como "nome" ou "1234"
#   as strings devem ser envolvidas por aspas duplas;
# BOOLEANOS: são valores verdadeiro (true) ou falso (false);
# ARRAYS: são listas ordenadas de valores, como [1, 2, 3] ou ["abc", "def", "gh"];
# OBJETOS: são conjuntos de pares chave/valor {"nome": "Rei", "idade": 31};
# NULL: é um valor especial que representa ausência de valor

# Ao converter de Python para JSON:
# Python      ->    JSON
# dict        ->    object
# list, tuple ->    array
# str         ->    string
# int, float  ->    number
# True        ->    true
# False       ->    false
# None        ->    null

import json
from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
}
'''

#passando para py
filme: Movie = json.loads(string_json)
pprint(filme)
print(filme['characters'])
print()

#passando para json
print(json.dumps(filme, ensure_ascii=False, indent=2))
