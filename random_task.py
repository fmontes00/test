from random import choice

thems = ['strings', 'functions', 'lists', 'tuples',
 'iterating lists', 'dictionaries', 'sets',
  'nested_collections&loops', 'libraries',
   'modules&packages', 'map', 'filter', 'reduce', 
   'list_comprehension', 'exceptions', 'OOP_methods',
    'class_attributes', 'hasattr', 'getattr', 'setattr',
    'magic_methods', 'inherence', 'polymorphism', 
    'file_managment', ]

def select_random(list_of_thems):
    elem = choice(list_of_thems)
    return elem

print(select_random(thems))

