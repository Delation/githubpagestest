from browser import document

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
