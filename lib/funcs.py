prefix = '!s'
def mpcsymbols_s():
  return ' '

def mpcsymbols_t():
  return '	'

def mpcsymbols_p():
  return '§'

def mpcsymbols_i():
  return '∞'

def mpcsymbols_lq():
  return '«'

def mpcsymbols_rq():
  return '»'

def mpcsymbols_c():
  return '©'

def mpcsymbols_e(args):
  e_en = {'duck':'🦆', 'tree':'🌳', 'palm_tree':'🌴', 'evergreen_tree':'🌲', 'snowflake':'❄️', 'snowman':'☃️', '🎉':'party_popper'}
  e_ru = {'утка':'🦆', 'дерево':'🌳', 'пальма':'🌴', 'ёлка':'🌲', 'снежинка':'❄️', 'снеговик':'☃️', '🎉':'хлопушка', 'романия':'🟩⬜🟦'}
  r = ''
  for simbol in args:
    if simbol in e_en:
      r += e_en[simbol]
    elif simbol in e_ru:
      r += e_ru[simbol]
  return r

funcs = {'s':mpcsymbols_s, 't':mpcsymbols_t, 'p':mpcsymbols_p, 'i':mpcsymbols_i, 'lq':mpcsymbols_lq, 'rq':mpcsymbols_rq, 'c':mpcsymbols_c, 'e':mpcsymbols_e}
  
