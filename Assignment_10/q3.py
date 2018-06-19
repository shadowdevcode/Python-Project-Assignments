class Cop:
   def __init__(self,name,experience,):
       self.name=name
       self.experience=experience
   def display_details(self):
       print(self.name,"cop is on duty with",self.experience,"years of experience")
   def update_details(self):
       self.name='Sherlock'
       self.experience=7
class Mission(Cop):
   def __init(self):
       super(Mission,self).__init()
   def display_mission(self,mission):
       print("The active mission is",mission)

   def assign_cop(self,mission):
       print(self.name,"has been assigned",mission)
mission=Mission('Sherlock',4)
mission.display_mission('Secret')
mission.display_details()
mission.assign_cop('Secret')