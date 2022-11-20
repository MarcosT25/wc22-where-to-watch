from experta import *

class WhereToGo(KnowledgeEngine):
    message = ''

    @DefFacts()
    def _initial_action(self):
        yield Fact(action='where-to-go')

    @Rule(Fact(action='where-to-go'),
          Fact(people=W()),
          Fact(party=W()),
          Fact(budget=W()),
          NOT(Fact(food='burguer')),
          Fact(watch='bigTv'),
          Fact(transport=W()))
    def cascata(self):
        self.message = 'cascata'

    @Rule(Fact(action='where-to-go'),
          Fact(people=W()),
          OR(Fact(party='alone'), Fact(party='friends')),
          NOT(Fact(budget='cheap')),
          NOT(Fact(food='plate')),
          Fact(watch='tv'),
          Fact(transport=W()))
    def fuxico(self):
        self.message = 'fuxico'

    @Rule(Fact(action='where-to-go'),
          Fact(people='few'),
          Fact(party='friends'),
          Fact(budget=W()),
          NOT(Fact(food='plate')),
          Fact(watch='bigTv'),
          Fact(transport=W()))
    def nova_rep(self):
        self.message = 'nova_rep'

    @Rule(Fact(action='where-to-go'),
          NOT(Fact(people='lot')),
          OR(Fact(party='friends'), Fact(party='alone')),
          OR(Fact(budget='expensive'), Fact(budget='veryExpensive')),
          OR(NOT(Fact(food='plate'), Fact(food='burguer'))),
          Fact(watch='tv'),
          Fact(transport='car'))
    def pirata(self):
        self.message = 'o pirata'

    @Rule(Fact(action='where-to-go'),
          Fact(people='lot'),
          OR(Fact(party='alone'), Fact(party='friends')),
          OR(Fact(budget='expensive'), Fact(budget='veryExpensive')),
          OR(NOT(Fact(food='plate'), Fact(food='burguer'))),
          Fact(watch='bigTv'),
          Fact(transport='car'))
    def barao(self):
        self.message = 'barão'

    def result(self):
        return self.message
