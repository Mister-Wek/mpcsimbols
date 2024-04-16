prefix = '!s'
def mpcsymbols_s(args):
  return ' '

def mpcsymbols_t(args):
  return '	'

def mpcsymbols_p(args):
  return '§'

def mpcsymbols_i(args):
  return '∞'

def mpcsymbols_lq(args):
  return '«'

def mpcsymbols_rq(args):
  return '»'

def mpcsymbols_c(args):
  return '©'

def mpcsymbols_e(args):
  e_en = {'duck':'🦆', 'tree':'🌳', 'palm_tree':'🌴', 'evergreen_tree':'🌲', 'snowflake':'❄️', 'snowman':'☃️'}
  e_ru = {'утка':'🦆', 'дерево':'🌳', 'пальма':'🌴', 'ёлка':'🌲', 'снежинка':'❄️', 'снеговик':'☃️'}
  r = ''
  for simbol in args:
    if simbol in e_en:
      r += e_en[simbol]
    elif simbol in e_ru:
      r += e_ru[simbol]
  return r

funcs = {'s':mpcsymbols_s, 't':mpcsymbols_t, 'p':mpcsymbols_p, 'i':mpcsymbols_i, 'lq':mpcsymbols_lq, 'rq':mpcsymbols_rq, 'c':mpcsymbols_c, 'e':mpcsymbols_e}
  
