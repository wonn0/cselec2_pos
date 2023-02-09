#accepts S<NP><VP>
grammar = {
    'S': [('NP', 'VP')],
    'NP': [('Det', 'N')],
    'VP': [('V', 'NP')],
    'Det': [('the',), ('a',)],
    'N': [('cat',), ('dog',)],
    'V': [('runs',), ('is',)]
}