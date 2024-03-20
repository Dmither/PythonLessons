class Celsius:
  def __init__(self, temperature = 0):
    self.temperature = temperature

  def to_fahrenheit(self):
    return (self._temperature * 1.8) + 32
  
  @property
  def temperature(self):
    return self._temperature
  
  @temperature.setter
  def temperature(self, value):
    if value < -273.15:
      raise ValueError("Temperature below -273.15 is not possible")
    self._temperature = value
  
human = Celsius()
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = 37
print(human.temperature)
print(human.to_fahrenheit())
