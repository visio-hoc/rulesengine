class Rules():
  categories = ['credit', 'products', 'states']

  def __init__(self):
    pass

  def _getDefaults(self):
    ret = {}
    for cat in self.categories:
      ret.update({cat: {}})

    return ret