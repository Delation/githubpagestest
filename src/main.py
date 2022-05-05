from browser import document

def show_text(e):
  if e.key == 'Enter':
    document['output'].textContent = dir(e)
  return
  h = {}
  try:
    exec('n = ' + e.target.value, h, None)
    document['output'].textContent = 'The answer is %s' % h['n']
  except:
    pass
  #document['output'].textContent = e.target.value;

document['text'].bind('keypress', show_text)
