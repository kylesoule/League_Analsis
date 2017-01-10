"""DEBUG CONSTANTS"""
GLOBAL_DEBUG_LEVEL = 2
CRITICAL = 1
ERROR = 2
WARNING = 3
INFORMATION = 4

class Debug:
    messages = {}
    LOCAL_DEBUG_LEVEL = GLOBAL_DEBUG_LEVEL
    
    def __init__(self, debug_level=LOCAL_DEBUG_LEVEL):
        """
        Initializes Debug class with an optional level.
        """
        self.LOCAL_DEBUG_LEVEL = debug_level
        
    #def __exit__(self):
    #    function = "SYSERR"
    #
    #    if function in self.messages:
    #        for message in self.messages[function]:
    #            print "::({level}) {func} -> {var}: {data}".format(level=message[2], func=function, var=message[0], data=message[1])
    
    def add_msg(self, function, variable, message, level):
        """
        Add message to Debug queue.
        
        Args:
            function: Calling function name
            message: Debug message
            level: Priority level
        """
        if function not in self.messages: 
            self.messages[function] = []

        self.messages[function].append([variable, message, level])
    
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
                if message[2] <= level:
                    print "::({level}) {func} -> {var}: {data}".format(level=message[2], func=function, var=message[0], data=message[1])
            self.messages.pop(function)
        else:
            print "::Function '{func}' does not exist!".format(func=function)
        
    def report_error(self, message):
        """
        Prints a simplified error message.
        """
        print "\n\n::ERROR: {data}\n\n".format(data=message)