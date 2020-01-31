class Person:
  credit_score = int()
  state = ""

  def __init__(self, credit_score: int, state: str):
    self.credit_score = credit_score
    self.state = state

  def __str__(self):
    return f'{self.credit_score}: {self.state}'
