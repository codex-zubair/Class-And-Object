


class book:
#Parents Class



    #### Instance attribute or Constructor  needs for "MATHOD"
    '''
    This is need for parameter
    of funtion for getting data...

    Example: 
    Robot(parameter:1, parameter:2)

    without this 
    prameter like this

    Robot.name = 'Male Robot'
    Robot.Age = '25'

    '''


    def __init__(self, name, author):

        '''
        by doing this we don't need to do it out side of class
        '''
        self.book_name = name
        self.author_name = author

    
    
    def Book_Details(self):
        
            print("Book name: "+ self.book_name);
            print("author name:" + self.author_name,"\n");

    



class Book_Details(book):
#child Class 1


    def __init__(self, name, author,category, price):

        self.category_type = category
        self.price_of_book = price
        
        book.__init__(self,name, author)


    def Book_Details_More(self):
        print("Book Name: "+self.book_name,"\nAuthor Name: "+self.author_name,"\nBook Category: "+self.category_type,"\nBook Price: "+self.price_of_book,"\n")

#child Class 2
class Book_details2(book):

    def __init__(self, name, author,Rank):

        self.ranking = Rank


        book.__init__(self,name, author)

    def Book_Details_Rank_mathod(self):
        print("Name Of book: "+self.book_name,"\nName of Author: "+self.author_name,"\nRanking: "+self.ranking,"\n")

    


class book_details2_child(Book_details2):

    def __init__(self, name, author, Rank,points):

        self.points = points

        Book_details2.__init__(self,name, author, Rank)


    def book_details2_child_point_print(self):
        print("\nBook Name: " + self.book_name,"\nAuthor: "+ self.author_name,"\nPosition: " +self.ranking,"\npoints: " + self.points)




book_details = book("fairy","By Robert");


Book1 = Book_Details("Robert the junior", "Robert","Story","100")


book_rank = Book_details2("Book 2","obama author","1st")


book_points = book_details2_child("child book","by Taba","1st","100")






book_details.Book_Details()
Book1.Book_Details_More()
book_rank.Book_Details_Rank_mathod()


book_points.book_details2_child_point_print()





class Bird:
    
    def intro(self):
        print("\nThere are many types of birds.")
  
    def flight(self):
        #Given Values for Flight.
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):

    #Same Function with other Given Values.
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        #Same Function with other Given Values.
        print("Ostriches cannot fly.")





obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
  
obj_bird.intro()
obj_bird.flight()
  
obj_spr.intro()
obj_spr.flight()
  
obj_ost.intro()
obj_ost.flight()






# Python program to
# demonstrate private members
  
# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeekssss"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class
class Derived(Base):
    def __init__(self):
  
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)



obj1 = Base()
print(obj1.a)