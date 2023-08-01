# Login code
from typing import Any
import os



        
# to add data to file 
def to_add_data():  
    with open('developers.txt','a+') as fptr:
        l1=[i for i in details()]
        fptr.write(l1[0]+","+l1[1]+","+l1[2]+",\n")


# to read overall data from the file

def read_overall():
    name_check_list=set()
    with open('developers.txt','r+') as fptr:
        while True:
            l=fptr.readline()
            if not l:
                break
            l1=l.split(',')
            name_check_list.add(l1[0])
    for i in name_check_list:
        details_by_name(i)
        print()
        

# to read the data from file by student name
def details_by_name(name):
# print()
    with open('developers.txt','r+') as fptr:
        count =0
        total_present=0
        while(True):
        
            l=fptr.readline()
            if not l:
                print("Total Present ",f"{total_present:>2}")
                break
            if l.split(',')[0]==name:
                list1=l.split(',')
                if count==0:
                    print("Name : ",list1[0])
                    print("    :Record:")
                    print('Dates     :','Status')
                    count+=1
                # print(list1[1]," ",list1[2])
                print(f"{list1[1]:<13}","  ",list1[2])
                if list1[2]=='p':
                    total_present+=1


# to add data 
def details():
    name=input("Enter student name :")
    date=input("Enter date in dd/mm/yyyy format :")
    attendance=input("attendance status(p/a) :")
    return (name,date,attendance)

# to delete data
def delete_by_name():
    name=input("Enter the name of the student to delete data permanently or press(no)")
    if(name!='no'):
        tfp=open('tempfile.txt','w')
        with open('developers.txt',"r+") as fptr:
            
                while(True):
                    line=fptr.readline()
                    if not line:
                        
                        break
                    if(line.split(',')[0]!=name):
                            l1=line.split(',')
                            tfp.write(l1[0]+","+l1[1]+","+l1[2]+",\n")
        tfp.close()
        os.remove('developers.txt')
        os.rename('tempfile.txt','developers.txt')

        print("Successfully removed ")
                
# updation in name
def updation_name():
    oldname=input("Enter old name :")
    new_name=input("Enter new name :")
    tfp=open("tempfile.txt",'w')
    with open('developers.txt',"r+") as fp:
        while True:
            line =fp.readline()
            if not line:
                break
            l1=line.split(',')
            if l1[0]==oldname:
                
                tfp.write(new_name+","+l1[1]+","+l1[2]+",\n")
            else:
                tfp.write(l1[0]+","+l1[1]+","+l1[2]+",\n")
    tfp.close()
    os.remove('developers.txt')
    os.rename('tempfile.txt','developers.txt')
    print(" Updated ")

          
## updation in attendence
def updation_in_attendance():
    name=input("Enter the name of the student :")
    date=input("Enter the date(dd/mm/yyyy) :")
    print("If student is absent then it is updated to present or vice versa ")
    tfp=open("tempfile.txt",'w')
    with open('developers.txt',"r+") as fp:
        while True:
            line =fp.readline()
            if not line:
                break
            l1=line.split(',')
            if l1[0]==name and l1[1]==date:
                updated_attendece = 'a' if l1[2]=='p' else 'p'
                tfp.write(l1[0]+","+l1[1]+","+updated_attendece+",\n")
            else:
                tfp.write(l1[0]+","+l1[1]+","+l1[2]+",\n")
    tfp.close()
    os.remove('developers.txt')
    os.rename('tempfile.txt','developers.txt')
    print(" Updated ")    




flag=0
while flag==0:
    print("Select a choice :")
    print("1.SignUp      2.SignIn")
    choice=int(input("Type Here:"))
    if choice==1:
        user_name=input("Enter your user_name :")
        pass_word=input("Enter your password :")

        with open('database.data','a+') as fptr:
            fptr.writelines(user_name+","+pass_word+","+"\n")
    elif choice ==2:
        userid=input("Enter user_name :")
        password=input("Enter password :")

        with open('database.data','r') as fptr:
        
            while True:
                line=fptr.readline()
                if not line:
                    print("Data not found ")
                    break
                if line.split(',')[0] ==userid and line.split(',')[1]==password:
                    print("Logged in successfully ")

                    flag=1
                    break
    
    else:
        print("Enter correct choice")





while(True):
    os.system("cls")
    print("Logged in Successfully")
    print("Enter your choice :")
    print("1.To add student data")
    print("2.To view data of all the students")
    print("3.To view report of particular student")
    print("4.To delete data ")
    print("5.To update the data")
    print("6 To Exit")

    choice=input("\n\nType here :")
    if choice=='1':
        to_add_data()
        input("Enter key to continue ")
        
    elif choice=='2':
        read_overall()
        input("Enter key to continue")
    elif choice=='3':
        name=input("Enter the student name whose attendance you want to search :")
        details_by_name(name)
        input("Enter key to continue ")
    elif choice=='4':
        delete_by_name()
        input("Enter key to continue")
    elif choice=='5':
        print("Press 1 == >Updation in name \nPress 2 ==>Updation in attendance record")
        subchoice=input()
        if subchoice=='1':
            updation_name()
        else:
            updation_in_attendance()
        
        
    elif choice=='6':
        break
































                

            



            


