


###Creating a Classs
class Robot:
    
#### have to add in every method "Self" when we are working in Class
    def introduce_self(self):

        print("my name is " + self.name)
        print("Age = "+ self.Age);



Robot1 = Robot()
Robot2 = Robot()


Robot1.name = 'Male Robot'
Robot1.Age = '25'



Robot2.name = 'Female Robot'
Robot2.Age = '20'


Robot1.introduce_self()
Robot2.introduce_self()



##############################################################


class Robot_version_2:
    
####Constructor....
    def __init__(self, Name, Age):

        self.NameX = Name
        self.AgeX = Age


#### have to add in every method "Self" when we are working in Class
    def introduce_self(self):

        print("my name is " + self.NameX)
        print("Age = "+ self.AgeX);


Robot3 = Robot_version_2('First Robot', '22')
Robot4 = Robot_version_2('Second Robot', '26')


Robot3.introduce_self()
Robot4.introduce_self()





        