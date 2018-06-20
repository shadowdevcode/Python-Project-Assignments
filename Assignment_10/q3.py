class Cop:

    def __init__(self, name, age, experience):
       self.name = name
       self.age = age
       self.experience = experience

    def display_details(self):
       print(self.name, "cop", self.age, " years of age is on duty with", self.experience, "years of experience")

    def update_details(self):
       self.name = input("Name of Cop: ")
       self.age = int(input("Enter age of cop: "))
       self.experience = 7

class Mission(Cop):

    def __init(self):
       super(self, mission).__init()

    def add_mission_details(self, mission):
        print("Mission: ", mission)
        print("Cop assigned: ", self.name, "on a mission", mission)


mission = Mission('Sherlock Homes,', 24, 8)

mission.update_details()

mission.add_mission_details('Secret')

mission.display_details()