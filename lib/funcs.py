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

def mpcsimbols_emoji(args):
  emoji_en = {'duck':'🦆', 'tree':'🌳', 'palm_tree':'🌴', 'evergreen_tree':'🌲', 'snowflake':'❄️'}
  emoji_ru = {'утка':'🦆', 'дерево':'🌳', 'пальма':'🌴', 'ёлка':'🌲', 'снежинка':'❄️'}
  r = ''
  for simbol in args:
    if simbol in emoji_en:
      r += emoji_en[simbol]
    elif simbol in emoji_ru:
      r += emoji_ru[simbol
  return r

funcs = {'s':mpcsimbols_s, 't':mpcsimbols_t, 'p':mpcsimbols_p, 'i':mpcsimbols_i, 'lq':mpcsimbols_lq, 'rq':mpcsimbols_rq, 'c':mpcsimbols_c, 'emoji':mpcsimbols_emoji}
  
