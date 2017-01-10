import json, urllib


"""
Debug levels:
    Level 0 = Off
    Level 1 = Results only
    Level 2 = Full
"""
GLOBAL_DEBUG = 1

class Debug:
    def __init__(self, definition, data):
        """
        Data:
            0 = String
            1 = Debug level
        """
        if GLOBAL_DEBUG > 0:
            print "::DEBUG BEGIN: {definition}".format(definition=definition)
            
            if type(data[0]) is str:
                if data[1] <= GLOBAL_DEBUG:
                    print "::{data}".format(data=data)
            elif type(data[0]) is list:
                    for line in data:
                        if line[1] <= GLOBAL_DEBUG:
                            print "::{data}".format(data = line)
            
            print "::DEBUG END\n"

def debug_helper(data, level):
    return [data, level]
            
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
        debug_data = []
        
        url_name = urllib.quote(name, safe='')
        a_url = "v1.4/summoner/by-name/"
        s_url = "{self_url}{api_url}{name}?api_key={api_key}".format(self_url=self.url, 
                                                                    api_url=a_url, 
                                                                    name=url_name, 
                                                                    api_key=self.api_key)
        
        response = urllib.urlopen(s_url)
        data = json.loads(response.read())
        
        # Debug data
        debug_data.append(debug_helper("url_name: {data}".format(data = url_name), 2))
        debug_data.append(debug_helper("a_url: {data}".format(data = a_url), 2))
        debug_data.append(debug_helper("s_url: {data}".format(data = s_url), 1))
        Debug("get_summonar_by_name(self, name)", debug_data)
        
        return data[simple_name(name)]['id']

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
    debug_data = []
    
    name = name.replace(" ", "").lower()
    
    debug_data.append(debug_helper("name: {data}".format(data = name), 2))
    Debug("simple_name(name)", debug_data)
    
    return name
                    
riot_api = Riot()
id = riot_api.get_summoner_by_name("SmashBrethren")
print id