_pad        = '_'
_punctuation = ',.!?- '
_letters = 'iɪɛæaoɔuʊʌəɜptkfsθʃhbdgvzðʒmnŋlrywüIjqx'

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")