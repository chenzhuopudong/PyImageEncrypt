

class logs:

    DEBUG = 4
    MINOR = 2
    def __init__(self, log_level):
        self.inner_log_level = log_level

    def debug_log(self,strings):
        if(self.inner_log_level<self.DEBUG):
            print(strings)

    def minor_log(self, strings):
        if (self.inner_log_level < self.MINOR):
            print(strings)
