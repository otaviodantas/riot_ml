from handle_env import load

import os
import requests
from typing import Dict, List

load()

class RiotAPI(object):
    HEADER = {'X-Riot-Token': os.environ.get('API_KEY')}

    def get_puuid_by_name(player_name: str) -> str:
        """
        Método é responsável por captar o puuid por meio unicamente pelo
        nome do jogador. O puuid é um Id único usado como parâmetros para
        outros métodos.

        Args:
            player_name (str): Nome do usuário no League of Legends

        Returns:
            str: retorna o puuid único do jogador 
        """        

        try:
            r = requests.get(os.environ.get('BASE_URL') + 
                            os.environ.get('MATCH_BY_NAME') + 
                            player_name, 
                            headers=RiotAPI.HEADER)
            return r.json()['puuid']
        except Exception as e:
            return e
    

    def get_gameid_by_puuod(puuid: str, begin_index: int=None) -> Dict:
        """
        Este método busca na API da Riot as partidas jogadas pelo dono 
        do puuid passado como parâmetro.

        Args:
            puuid (str): Id único do jogador, obtido em get_puuid_by_name
            begin_index (int, optional): Parâmetro equivalente à página,
            para acessar o próximo lote de partidas, basta passar o 
            ultimo beginIndex recebido da última chamada do método. 
            Defaults to None.

        Returns:
            Dict:
            {
                'begin_index': str,
                'list_gameid': List[str]
            }
        """
        cache: Dict = {
            'begin_index': '',
            'gamesid': [],
        }

        try:
            string_conc = (os.environ.get('BASE_URL') +
                           os.environ.get('MATCH_BY_IDGAME') +
                           puuid)
            if begin_index:
                string_conc += f'?beginIndex={begin_index}' 

            r = requests.get(string_conc, headers=RiotAPI.HEADER)

            for i in r.json()['matches']:
                cache['gamesid'].append(i['gameId']) 
            cache['begin_index'] = r.json()['endIndex']

            return cache

        except Exception as e:
            return e


    def get_info_match(gameid: int):
        try:
            # TODO: implementar https://developer.riotgames.com/apis#match-v4/GET_getMatch
            ...
        except:
            ...