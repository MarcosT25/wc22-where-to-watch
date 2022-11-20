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
          Fact(people='lot'),
          Fact(party=W()),
          Fact(budget='cheap'),
          OR(Fact(food='plate'), Fact(food='portion')),
          Fact(watch='bigTv'),
          Fact(transport='foot'))
    def cascata(self):
        self.message = 'cascata'

    @Rule(Fact(action='where-to-go'),
          Fact(people='lot'),
          OR(Fact(party='alone'), Fact(party='friends')),
          Fact(budget='medium'),
          OR(Fact(food='burguer'), Fact(food='portion')),
          Fact(watch='tv'),
          Fact(transport='foot'))
    def fuxico(self):
        self.message = 'fuxico'

    @Rule(Fact(action='where-to-go'),
          Fact(people='few'),
          Fact(party='freinds'),
          Fact(budget='cheap'),
          OR(Fact(food='burguer'), Fact(food='portion')),
          Fact(watch='bigTv'),
          Fact(transport='foot'))
    def nova_rep(self):
        self.message = 'nova_rep'

    @Rule(Fact(action='where-to-go'),
          Fact(people='few'),
          OR(Fact(party='friends'), Fact(party='alone')),
          Fact(budget='expensive'),
          Fact(food='portion'),
          Fact(watch='tv'),
          Fact(transport='car'))
    def pirata(self):
        self.message = 'o pirata'

    @Rule(Fact(action='where-to-go'),
          Fact(people='lot'),
          OR(Fact(party='alone'), Fact(party='friends')),
          Fact(budget='expensive'),
          Fact(food='portion'),
          Fact(watch='bigTv'),
          Fact(transport='car'))
    def barao(self):
        self.message = 'barão'

    def result(self):
        return self.message
