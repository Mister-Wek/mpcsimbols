prefix = '!s'
def mpcsimbols_s(args):
  return ' '

def mpcsimbols_t(args):
  return '	'

def mpcsimbols_p(args):
  return '§'

def mpcsimbols_i(args):
  return '∞'

def mpcsimbols_lq(args):
  return '«'

def mpcsimbols_rq(args):
  return '»'

def mpcsimbols_c(args):
  return '©'

def mpcsimbols_e(args):
  e_en = {'duck':'🦆', 'tree':'🌳', 'palm_tree':'🌴', 'evergreen_tree':'🌲', 'snowflake':'❄️', 'snowman':'☃️'}
  e_ru = {'утка':'🦆', 'дерево':'🌳', 'пальма':'🌴', 'ёлка':'🌲', 'снежинка':'❄️', 'снеговик':'☃️'}
  r = ''
  for simbol in args:
    if simbol in e_en:
      r += e_en[simbol]
    elif simbol in e_ru:
      r += e_ru[simbol]
  return r

funcs = {'s':mpcsimbols_s, 't':mpcsimbols_t, 'p':mpcsimbols_p, 'i':mpcsimbols_i, 'lq':mpcsimbols_lq, 'rq':mpcsimbols_rq, 'c':mpcsimbols_c, 'e':mpcsimbols_e}
  
