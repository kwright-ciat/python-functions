class Cup(object):
  def __init__(self,size,color,full):
    ''' Creates object "constructor" method '''
    self.size = size
    self.color = color
    self.full = full
  
  def fillcup(self):
    ''' mutator method '''
    self.full = 1

  def emptycup(self):
    self.full = 0

  def cupstatus(self):
    ''' accessor method '''
    if self.full:
      print("full cup")
    else:
      print("empty cup")

mycup = Cup("large", "blue", 1)
mycup.cupstatus()
mycup.emptycup()
mycup.cupstatus()
mycup.fillcup()
mycup.cupstatus()

