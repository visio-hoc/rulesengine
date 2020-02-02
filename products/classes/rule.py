class Rule():
  """
  At the moment this class doesn't do much except return default rules. But 
  I created in case we want to do some pre-processing to rules before they
  were imported. 
  """

  #default rules categories, would normally place this in app settings
  categories = ['credit', 'products', 'states']
  name = ''

  def __init__(self):
    pass

  def _getDefaults(self):
    return self.categories