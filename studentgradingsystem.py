#STUDENT GRADING SYSTEM
sturec={}
def Addrecord():
      print("so you want to add a record in the grade record!!")
      name=input("What's the student name? :- ")
      print("Nice!! now enter the grades of the student...")
      print("REMEMBER!!! grades should be enter in space separated fashion..")
      print("Order of filling subject wise is (english, hindi, maths, science, social science)")
      grades=list(map(int,input("enter the grades of the student:- ").strip().split(" ")))[:5]
      sturec[name]=grades
      print("Great!! student record saved successfully!!")


def RemRecord():
  remname=input("Name the student whose record have to be removed:- ")  
  sturec.pop(remname,"record doesn't exist for this student!!") 

def AvgGrades():
  avgstu=input("Name the student whose grade's average to be taken:- ")
  if sturec:
    avg=sum(sturec[avgstu])/len(sturec[avgstu])
    print("average of the record of student:- ",avg)
  else:
    print("Invalid operation!!")


def guide():
   s='''operations:-
             1) For creating a student grade record press 1
             2) For removing a student grade record press 2
             3) For calculating average grade of the student press 3
             4) For displaying student record press 4
             5) To exit press 5'''
   print(s)
   opcmd = int(input("Which command you want to give:- "))
   if opcmd==1:
          Addrecord()
          guide()
   elif opcmd==2:
     if sturec:
       RemRecord()
       guide()
     else:
       print("record doesn't exist!!")
       guide()

   elif opcmd==3:
     AvgGrades()
     guide()
   elif opcmd==4:
     print(sturec)  
     guide()
   elif opcmd==5:
     exit()  

u_name="medicaps"
u_pass="123456"
success=False
def login():
    uname=input("enter your name: ")
    upass=input("enter your password: ")
    if uname==u_name and upass==u_pass:
        success=True
        print("you have logged in successfully!!")
        guide()
    else:
        print("invalid credentials!!")
        login()
login()        
