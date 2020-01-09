class Member:
  def __init__(self, name, phoneNumber, mRef, status):
    self.name = name
    self.phoneNumber = phoneNumber
    self.mRef = mRef
    self.status = status

  def memberInfo(self):
    return (self.name + " / " + self.phoneNumber + " / " + self.status) + "\n"