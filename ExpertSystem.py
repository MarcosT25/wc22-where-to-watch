from experta import *

class WhereToGo(KnowledgeEngine):
    message = ''

    @DefFacts()
    def _initial_action(self):
        yield Fact(action='where-to-go')

    @Rule(Fact(action='where-to-go'),
          Fact(people=W()),
          Fact(budget=W()),
          NOT(Fact(food='burguer')),
          Fact(watch='bigTv'),
          Fact(transport='foot'))
    def cascata(self):
        self.message = 'cascata'

    @Rule(Fact(action='where-to-go'),
          Fact(people=W()),
          NOT(Fact(budget='cheap')),
          NOT(Fact(food='plate')),
          Fact(watch='tv'),
          Fact(transport='foot'))
    def fuxico(self):
        self.message = 'fuxico'

    @Rule(Fact(action='where-to-go'),
          Fact(people=W()),
          Fact(budget=W()),
          NOT(Fact(food='plate')),
          Fact(watch='bigTv'),
          Fact(transport='foot'))
    def nova_rep(self):
        self.message = 'novarep'

    @Rule(Fact(action='where-to-go'),
          NOT(Fact(people='lot')),
          OR(Fact(budget='expensive'), Fact(budget='veryExpensive')),
          OR(NOT(Fact(food='plate'), Fact(food='burguer'))),
          Fact(watch='tv'),
          Fact(transport='car'))
    def pirata(self):
        self.message = 'pirata'

    @Rule(Fact(action='where-to-go'),
          Fact(people=W()),
          OR(Fact(budget='expensive'), Fact(budget='veryExpensive')),
          OR(NOT(Fact(food='plate'), Fact(food='burguer'))),
          Fact(watch='bigTv'),
          Fact(transport='car'))
    def barao(self):
        self.message = 'barao'

    def result(self):
        return self.message
