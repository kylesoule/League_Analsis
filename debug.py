"""DEBUG CONSTANTS"""
GLOBAL_DEBUG_LEVEL = 2
CRITICAL = 1
ERROR = 2
WARNING = 3

class Debug:
    messages = {}
    LOCAL_DEBUG_LEVEL = GLOBAL_DEBUG_LEVEL
    
    def __init__(self, debug_level=LOCAL_DEBUG_LEVEL):
        """
        Initializes Debug class with an optional level.
        """
        self.LOCAL_DEBUG_LEVEL = debug_level
    
    def add_msg(self, function, message, level):
        """
        Add message to Debug queue.
        
        Args:
            function: Calling function name
            message: Debug message
            level: Priority level
        """
        if function not in self.messages: 
            self.messages[function] = []

        self.messages[function].append([message, level])
    
    def print_msg(self, function, level=None):
        """
        Prints and clears Debug queue.
        
        Args:
            function: Calling function messages to print
            OPTIONAL level: Defaults to LOCAL_DEBUG_LEVEL
        """
        if level is None: level = self.LOCAL_DEBUG_LEVEL
        
        if function in self.messages:
            for message in self.messages[function]:
                if message[1] <= level:
                    print "::({level}) {func} -> {data}".format(level=message[1], func=function, data=message[0])
            self.messages.pop(function)
        else:
            print "::Function '{func}' does not exist!".format(func=function)

dbg = Debug()
dbg.add_msg("func", "This is a test1", 2)
dbg.add_msg("func", "This is not a test1", 1)
dbg.add_msg("func", "This is not a test2", 3)

dbg.print_msg("func")
dbg.print_msg("func")