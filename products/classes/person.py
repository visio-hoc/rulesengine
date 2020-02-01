class Person:
  credit_score = int()
  state = ""
  debtToIncome = float()
  currentlyEmployed = bool
  currentIncome = int()

  def __init__(self, credit_score: int, state: str):
    self.credit_score = credit_score
    self.state = state

  def setIncome(self, currentlyEmployed: bool, currentIncome: int, debtToIncome: float):
    self.debtToIncome = debtToIncome
    self.currentlyEmployed = currentlyEmployed
    self.currentIncome = currentIncome

  def __str__(self):
    return f'{self.credit_score}: {self.state}'
