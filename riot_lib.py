import json, urllib2, sys
import debug as Debugger

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
            
    def get_recent_games_by_id(self, id):
        """
        Retrieve a list of the last 10 games by summoner ID.
        
        Args:
            id: Summoner ID
        
        Returns:
            List of game IDs
            
        See Also:
            https://developer.riotgames.com/api/methods#!/1207/4679
        """
        games = []
        a_url = "v1.3/game/by-summoner/"
        s_url = "{self_url}{api_url}{id}/recent?api_key={api_key}".format(self_url=self.url,
                                                                   api_url=a_url,
                                                                   id=id,
                                                                   api_key=self.api_key)
        
        response = urllib2.urlopen(s_url)
        data = json.loads(response.read())
        
        # Debug data
        dbg.add_msg("get_recent_games_by_id(self, id)", "a_url", a_url, 4)
        dbg.add_msg("get_recent_games_by_id(self, id)", "s_url", s_url, 4)
        dbg.print_msg("get_recent_games_by_id(self, id)")
        
        try:
            for game in data["games"]:
                games.append(game["gameId"])
            return games
        except:
            dbg.report_error("No games found!")
            sys.exit()
        

dbg = Debugger.Debug(Debugger.INFORMATION)
riot_api = Riot()
id = riot_api.get_summoner_by_name("SmashBrethren")
games = riot_api.get_recent_games_by_id(id)

for game in games:
    print game