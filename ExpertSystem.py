from experta import *

class ExpertSystem(KnowledgeEngine):
    message = ''

    @Rule(Fact(input='cheap'))
    def cheap(self):
        self.message = 'Cascata Do Vinho'

    @Rule(Fact(input='medium'))
    def medium(self):
        self.message = 'Fuxico'

    @Rule(Fact(input='expensive'))
    def expensive(self):
        self.message = 'Barão'

    def result(self):
        return self.message

class WhereToGo(KnowledgeEngine):
    message = ''

    @DefFacts()
    def _initial_action(self):
        yield Fact(action='where-to-go')

    @Rule(Fact(action='where-to-go'),
          Fact(friends='many'),
          Fact(type=W()),
          Fact(budget='cheap'),
          OR(Fact(eat='pf'), Fact(eat='porcao')),
          Fact(watch='telao'),
          Fact(transport='foot'))
    def cascata(self):
        self.message = 'cascata'

    @Rule(Fact(action='where-to-go'),
          Fact(friends='many'),
          OR(Fact(type='alone'), Fact(type='friends')),
          Fact(budget='medium'),
          OR(Fact(eat='burgao'), Fact(eat='porcao')),
          Fact(watch='tv'),
          Fact(transport='foot'))
    def fuxico(self):
        self.message = 'fuxico'

    @Rule(Fact(action='where-to-go'),
          Fact(friends='few'),
          Fact(type='friends'),
          Fact(budget='cheap'),
          OR(Fact(eat='burgao'), Fact(eat='porcao')),
          Fact(watch='telao'),
          Fact(transport='foot'))
    def nova_rep(self):
        self.message = 'nova_rep'

    @Rule(Fact(action='where-to-go'),
          Fact(friends='few'),
          OR(Fact(type='friends'), Fact(type='alone')),
          Fact(budget='expensive'),
          Fact(eat='porcao'),
          Fact(watch='tv'),
          Fact(transport='uber'))
    def pirata(self):
        self.message = 'o pirata'

    @Rule(Fact(action='where-to-go'),
          Fact(friends='many'),
          OR(Fact(type='alone'), Fact(type='friends')),
          Fact(budget='expensive'),
          Fact(eat='porcao'),
          Fact(watch='telao'),
          Fact(transport='uber'))
    def barao(self):
        self.message = 'barão'

    def result(self):
        return self.message
