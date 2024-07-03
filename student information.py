class student_info:
    def __init__(self, name,roll_no,course) :
        self.name = name
        self.roll_no = roll_no
        self.course = course
    
    def myfunc(self):
        print( self.name,self.roll_no,self.course)
        
S1= student_info("Akash", 1 ,"BCA")
S1.myfunc()

        