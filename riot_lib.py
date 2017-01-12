import json, urllib2, sys
import debug as Debugger

RATE_LIMIT = 500    # per 10 minutes
WAIT_TIME = ((600.0 / RATE_LIMIT) + 0.5)

"""
TODO:
    IMPLEMENT A RATE LIMITER ON ALL CALLS!
"""

class Riot:
    api_key = "fb86f255-edcf-4b8f-ba07-8b0f675c8b51"
    url = "https://na.api.pvp.net/api/lol/na/"
    
    def simple_name(self, name):
        """
        Converts a summoner username to a Riot simplified name.
        
        Args:
            name: Summoner name
        
        Returns:
            Simplified name
        
        Operations:
            Removes spaces
            Converts to lowercase
        """
        name = name.replace(" ", "").lower()
    
        # Debug data    
        dbg.add_msg("simple_name(name)", "name", name, 4)
        dbg.print_msg("simple_name(name)")
        
        return name
    
    def get_summoner_by_name(self, name):
        """
        Retrieve summoner ID from the name.
        
        Args:
            name: Summoner name
        
        Returns:
            Summoner ID
        
        See Also:
            https://developer.riotgames.com/api/methods#!/1208/4684
        """
        url_name = urllib2.quote(name, safe='')
        a_url = "v1.4/summoner/by-name/"
        s_url = "{self_url}{api_url}{name}?api_key={api_key}".format(self_url=self.url, 
                                                                    api_url=a_url, 
                                                                    name=url_name, 
                                                                    api_key=self.api_key)
        
        response = urllib2.urlopen(s_url)
        data = json.loads(response.read())
        
        # Debug data
        dbg.add_msg("get_summonar_by_name(self, name)", "url_name", url_name, 4)
        dbg.add_msg("get_summonar_by_name(self, name)", "a_url", a_url, 4)
        dbg.add_msg("get_summonar_by_name(self, name)", "s_url", s_url, 4)
        dbg.print_msg("get_summonar_by_name(self, name)")
        
        try:
            return data[self.simple_name(name)]['id']
        except:
            dbg.report_error("Summoner name not found!")
            sys.exit()
            
    def get_recent_game_data_by_summoner_id(self, id):
        """
        Retrieve a list of the last 10 games by summoner ID.
        
        Args:
            id: Summoner ID
        
        Returns:
            List of game IDs
            
        See Also:
            https://developer.riotgames.com/api/methods#!/1207/4679
        """
        a_url = "v1.3/game/by-summoner/"
        s_url = "{self_url}{api_url}{id}/recent?api_key={api_key}".format(self_url=self.url,
                                                                   api_url=a_url,
                                                                   id=id,
                                                                   api_key=self.api_key)
        
        response = urllib2.urlopen(s_url)
        data = json.loads(response.read())
        
        # Debug data
        dbg.add_msg("get_recent_game_data_by_summoner_id(self, id)", "a_url", a_url, 4)
        dbg.add_msg("get_recent_game_data_by_summoner_id(self, id)", "s_url", s_url, 4)
        dbg.print_msg("get_recent_game_data_by_summoner_id(self, id)")
        
        try:
            return data
        except:
            dbg.report_error("No games found!")
            sys.exit()
    
    def get_champion_name_by_id(self, championId):
        """
        Returns a full list of champions by ID.
        
        Args:
            id: Champion ID
        
        Returns:
            Champion name
            
        See Also:
            https://developer.riotgames.com/api/methods#!/1055/3622
        """
        static_url = "https://global.api.pvp.net/api/lol/static-data/na/"
        a_url = "v1.2/champion/"
        s_url = "{static_url}{api_url}{id}?api_key={api_key}".format(static_url=static_url,
                                                                     api_url=a_url,
                                                                     id=championId,
                                                                     api_key=self.api_key)
        
        # Debug data
        dbg.add_msg("get_champion_name_by_id(self, championId)", "static_url", static_url, 4)
        dbg.add_msg("get_champion_name_by_id(self, championId)", "a_url", a_url, 4)
        dbg.add_msg("get_champion_name_by_id(self, championId)", "s_url", s_url, 4)
        dbg.print_msg("get_champion_name_by_id(self, championId)")
        
        try:
            response = urllib2.urlopen(s_url)
            data = json.loads(response.read())
            return data["name"]
        except:
            return "Champion not found!"
    
    def get_full_champion_list(self):
        """
        Returns a complete list of all champions by ID.
        
        Returns:
            Champion ID
            Name
        
        See Also:
            https://developer.riotgames.com/api/methods#!/1055/3633
        https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key=fb86f255-edcf-4b8f-ba07-8b0f675c8b51
        """
        champions = []
        static_url = "https://global.api.pvp.net/api/lol/static-data/na/"
        a_url = "v1.2/champion/"
        s_url = "{static_url}{api_url}?api_key={api_key}".format(static_url=static_url,
                                                                 api_url=a_url,
                                                                 api_key=self.api_key)
        
        response = urllib2.urlopen(s_url)
        data = json.loads(response.read())
        
        # Debug data
        dbg.add_msg("get_full_champion_list(self)", "static_url", static_url, 4)
        dbg.add_msg("get_full_champion_list(self)", "a_url", a_url, 4)
        dbg.add_msg("get_full_champion_list(self)", "s_url", s_url, 4)
        dbg.print_msg("get_full_champion_list(self)")
        
        for champIdName in data["data"]:
            champion = data["data"][champIdName]
            champions.append([champion["id"], champion["name"]])
        
        return champions
        

dbg = Debugger.Debug(Debugger.WARNING)
riot_api = Riot()

champions = riot_api.get_full_champion_list()

for champion in champions:
    print("{id}\t{name}".format(id=champion[0], name=champion[1]))



"""
id = riot_api.get_summoner_by_name("SmashBrethren")
games = riot_api.get_recent_game_data_by_summoner_id(id)
"""


"""
seedId = games["summonerId"]
for game in games["games"]:
    players = []
    gameId = game["gameId"]
    
    if game["stats"]["team"] == 100:
        if game["stats"]["win"] == True:
            winner = 100
        else:
            winner = 200
    else:
        if game["stats"]["win"] == True:
            winner = 200
        else:
            winner = 100
    
    print("Winner of {gameId} is {winner}:".format(gameId=gameId, winner=winner))
    
    players.append([game["teamId"], game["championId"], seedId])
    for player in game["fellowPlayers"]:
        players.append([player["teamId"], player["championId"], player["summonerId"]])
    
    for player in players:
        print("\t{t}\t{c}\t{s}".format(t=player[0], c=player[1], s=player[2]))
"""