class Person:
 def __init__(self,n,a) :
  self.name = n
  self.age = a
 def describe(self):
  print("Name",self.name)
  print("Age",self.age) 
 def __lt__(self,other):
  return self.age < other.age
 def __str__(self) :
  return f"My name is {self.name}. I am {self.age}"
marcon = Person("Marcon",43)
marcon.describe()
print(marcon) 
biden = Person("Bieden", 75)
biden.describe()
print(biden)
print(f"Biden is younger {marcon > biden}")
dat = Person("Dat", 1000)
dat.describe()
print(dat)
print(f"Dat là bố 2 thằng ngu kia ")