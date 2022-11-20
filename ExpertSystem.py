from experta import *

class Budget(Fact):
    """Info about the traffic light."""
    pass

class ExpertSystem(KnowledgeEngine):
    message = ''

    @Rule(Budget(input='cheap'))
    def cheap(self):
        self.message = 'Cascata Do Vinho'

    @Rule(Budget(input='medium'))
    def medium(self):
        self.message = 'Fuxico'

    @Rule(Budget(input='expensive'))
    def expensive(self):
        self.message = 'Barão'

    def result(self):
        return self.message