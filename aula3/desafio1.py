import random
from pprint import pprint

sorteios = ['sorteio1', 'sorteio2', 'sorteio3']
participates = ['joel', 'jessica', 'maria',
                'cris', 'larissa', 'rafael', 'marcus', 'jhon']

pprint({sorteio: [random.choice(participates)] for sorteio in sorteios})
