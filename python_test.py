import os

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.values())
print(car["brand"])

jobName = 'Test'

if os.path.exists(os.path.join(os.getcwd(), jobName+'.cae')):
  print("exists")
else:
  print("don't exists" )