class Animal:

   def animal_attributes(self, no_of_legs):
       print("Animals have ", no_of_legs, " legs")

#Inheriting class Animal

class Tiger(Animal):

   def tiger_atrributes(self, nutrition):
       print("Tiger is ", nutrition)

#Creating Objects and calling them

tiger = Tiger()
tiger.animal_attributes(4)
tiger.tiger_atrributes('carnivores')

