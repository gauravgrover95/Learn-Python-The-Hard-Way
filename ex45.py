
class Animal():

	def __init__(self, name):

		self.name = name

	def speak(self):
		print "check me out.. I am speaking"

## ?? Dog is-a class of Animal
class Dog(Animal):

	def __init(self, name):
		## ?? Dog has-a name
		self.name = name

	def speak(self):
		print "Bow Bow!"

## ?? Cat is-a class of superclass Animal
class Cat(Animal):

	def __init(self, name):
		## ?? Cat has-a name
		self.name = name

	def speak(self):
		print "Meow...... Meow"

## ?? Person is-a class of superclass object
class Person(object):
	def __init__(self, name):
		## ?? Person has-a name
		self.name = name


		## Person has-a pet of some kind
		self.pet = None

	def speak(self):

		print "Hi my name is " + self.name + ". Happy to see you"

## ?? Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):

		## ?? hmm what is this strange magic
		super(Employee, self).__init__(name)

		## ?? Employee has-a salary
		self.salary = salary

	def speak(self):
		print "Good Morning Sir, my name is", self.name
# TBN very carefully: the name of the method and the data member can not be same.
# It creates confusion for the interpretter, It starts calling the data member and gives the TypeError
# that this data member is not callable
	def my_salary(self):
		# print 120000
		print "My salary is", self.salary

class Fish(object):
	pass

## ?? Salmon is-a Fish
class Salmon(Fish):
	pass

## ?? Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a dog
rover = Dog("Rover")

## ?? satan is-a Cat
satan = Cat("Satan")

## ?? mary is-a object of Person
mary = Person("Mary")

## ?? frank is-a Employee which has-a salary of 120000
frank = Employee("Frank", 120000)


## ?? frank has-a pet , which is an object, rover
frank.pet = rover

## ?? flipper is-a object of Fish
flipper = Fish()

## ?? crouse is-a object of Salmon
crouse = Salmon()

## ?? harry is-a object of Halibut
harry = Halibut()

print ""

print "This is me speaking as Person:"
gaurav = Person("Gaurav")
gaurav.speak()

print ""

print "This is me speaking as an Employee:"
gaurav = Employee("Gaurav Grover", 120000)
gaurav.speak()
gaurav.my_salary()

# bruno = Dog("Bruno")
# bruno.speak()

# mayank is the object of many classes
mayank = [Person("Mayank"), Animal("Mayank")]