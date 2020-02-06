# import calendar
# print(calendar.calendar(2020))

# from calendar import *
# print(month(2020,2))

class P:
	def show(self):
		print("in a parent class")
class C(P):
	def display(self):
		print("in a child class")
obj=C()
obj.show()
obj.display()