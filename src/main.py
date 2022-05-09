from browser import document

if document.cookie:
  document['user_out'].textContent = 'Welcome back, %s' % document.cookie[5:]

def save_user(e):
  if not e.key == 'Enter':
    return
  document.cookie = "user=%s" % e.target.value
  document['user_out'].textContent = 'Saved your username, %s' % e.target.value

def show_text(e):
  if not e.key == 'Enter':
    return
  h = {}
  try:
    exec('n = ' + e.target.value, h, None)
    document['output'].textContent = 'The answer is %s' % h['n']
  except:
    pass
  #document['output'].textContent = e.target.value;

document['text'].bind('keypress', show_text)


document['user_in'].bind('keypress', show_text)
