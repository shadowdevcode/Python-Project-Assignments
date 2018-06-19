class Animal:
   def animal_attributes(self,legs):
       print("Animals have ", legs, " legs")

#Inheriting class Animal

class Tiger(Animal):
   def tiger_atrributes(self, nutrition):
       print("Tiger is ",nutrition)
#Creating Objects and calling them
tig=Tiger()
tig.animal_attributes(4)
tig.tiger_atrributes('carnivores')

