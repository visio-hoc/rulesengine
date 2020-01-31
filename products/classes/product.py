class Product:
  name = ""
  interest_rate = float()
  disqualified = bool()

  def __init__(self, name: str, interest_rate: float):
    self.name = name
    self.interest_rate = interest_rate

  def __str__(self):
    return f'{self.name}'
