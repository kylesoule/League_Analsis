import json, urllib
import debug as Debugger

class Riot:
    api_key = "fb86f255-edcf-4b8f-ba07-8b0f675c8b51"
    url = "https://na.api.pvp.net/api/lol/na/"
    
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
        
        url_name = urllib.quote(name, safe='')
        a_url = "v1.4/summoner/by-name/"
        s_url = "{self_url}{api_url}{name}?api_key={api_key}".format(self_url=self.url, 
                                                                    api_url=a_url, 
                                                                    name=url_name, 
                                                                    api_key=self.api_key)
        
        response = urllib.urlopen(s_url)
        data = json.loads(response.read())
        
        # Debug data
        dbg.add_msg("get_summonar_by_name(self, name)", "url_name", url_name, 4)
        dbg.add_msg("get_summonar_by_name(self, name)", "a_url", a_url, 4)
        dbg.add_msg("get_summonar_by_name(self, name)", "s_url", s_url, 4)
        dbg.print_msg("get_summonar_by_name(self, name)")
        
        return data[self.simple_name(name)]['id']

    def simple_name(name):
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

dbg = Debugger.Debug(Debugger.INFORMATION)
riot_api = Riot()
id = riot_api.get_summoner_by_name("SmashBrethren")
print id