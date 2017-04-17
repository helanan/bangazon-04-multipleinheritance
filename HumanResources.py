##
class FullTime():
  """Describes full-time employees"""

  def __init__(self):
    self.hours_per_week = 40

class PartTime():
  """Describes part-time employees"""

  def __init__(self):
    self.hours_per_week = 24

class HumanResources(Employee, FullTime):
  """Describes human resources employees"""

  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name) # super is Employee
    FullTime.__init__(self)
