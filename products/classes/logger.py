class Logger():

  def __init__(self):
    self.logs = []

  def logAdd(self, message):
    self.logs.append(message)