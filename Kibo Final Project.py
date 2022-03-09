# Kibo FPWP Final Project
# Put your final project code in this file for submission
# Add the names of the authors, a brief description, and link to your video in the file called 'readme.md'
# Then, you can remove these instruction comments
#beginning
nganyas=[]
passengers=[]
from tabulate import tabulate
import os
from time import sleep
col_names=["NUMBER PLATE","NAME","SACCO","SEATS","PRICE","TIME(MIN)"]
col_names2=["INDEX","MATATU","PASSENGER NAME", "MATATU BOOKED", "SEATS BOOKED", "CONTACT"]
def menu():
    os.system('cls')
    print("**********ROUTE 111*************".center(60))
    print("****MATATU BOOKING SYSTEM****".center(60))
    print("*********************************".center(60))
    print("<<<<<<<<<<WELCOME USERS>>>>>>>>>>".center(60))
    print("")
    print("MENU".center(60))
    print("******".center(60))
    print("[1] VIEW INFORMATION".center(60))
    print("[2] BOOK NGANYA".center(60))
    print("[3] CANCEL BOOKED NGANYA".center(60))
    print("[4] ADMIN".center(60))
    print("[5] EXIT".center(60))
    print("********************************".center(60))
    print("********************************".center(60))
    choice=input("ENTER YOUR CHOICE: ".center(60))
    if choice=='4':
      password()
    elif choice=='1':
       loading()
       show_info()
       input("Press Enter to continue...")
       menu()
    elif choice=='5':
        print("Kindly wait") 
    elif choice=='2':
      loading()
      add_passenger()
    elif choice=='3':
      loading()
      cancel_booking()
    

def first_nganyas():
  addnganya=[]
  addnganya2=[]
  num_plate="KCA711D"
  addnganya.append(num_plate)
  nganya_name="FOXY"
  addnganya.append(nganya_name)
  nganya_sacco="LUMINOUS"
  addnganya.append(nganya_sacco)
  seat_number=42
  addnganya.append(seat_number)
  nganya_fare=100
  addnganya.append(nganya_fare)
  nganya_time=50
  addnganya.append(nganya_time)
  nganyas.append(addnganya)
  addnganya2.append("KDC317A")
  addnganya2.append("MISTY")
  addnganya2.append("ASTRABELL")
  addnganya2.append(41)
  addnganya2.append(90)
  addnganya2.append(60)
  nganyas.append(addnganya2)
def first_passengers():
  first_nganyas()
  addpassenger=[]
  addpassenger2=[]
  nganya_book=0
  seat_book=3
  nganyas[nganya_book][3]=nganyas[nganya_book][3]-seat_book
  passenger_name="Emmy"
  passenger_contact=738568903
  addpassenger.append(nganya_book)
  addpassenger.append(passenger_name)
  addpassenger.append(nganyas[nganya_book][1])
  print(len(nganyas))
  #The above adds the name of the booked matatu to the list
  addpassenger.append(seat_book)
  addpassenger.append(passenger_contact)
  passengers.append(addpassenger)
  nganya_book=1
  seat_book=2
  nganyas[nganya_book][3]=nganyas[nganya_book][3]-seat_book
  passenger_name="Seun"
  passenger_contact=765367534
  addpassenger2.append(nganya_book)
  addpassenger2.append(passenger_name)
  addpassenger2.append(nganyas[nganya_book][1])
  addpassenger2.append(seat_book)
  addpassenger2.append(passenger_contact)
  passengers.append(addpassenger2)
  menu()


def add_nganya():
  addnganya=[]
  num_plate=input("Enter number plate of matatu: ")
  addnganya.append(num_plate)
  nganya_name=input("Enter the name of matatu: ")
  addnganya.append(nganya_name)
  nganya_sacco=input("Enter the SACCO of the matatu: ")
  addnganya.append(nganya_sacco)
  seat_number=int(input("Enter number of seats in matatu: "))
  addnganya.append(seat_number)
  nganya_fare=int("Enter fare per passenger: ")
  addnganya.append(nganya_fare)
  nganya_time=int(input("Enter transit time: "))
  addnganya.append(nganya_time)
  nganyas.append(addnganya)
  print("INFO SUCCESSFULLY SAVED IN SYSTEM")
  input("Press Enter to continue...")
  menu()

def show_info ():
  print(tabulate(nganyas,headers=col_names,showindex="always")) 
  
def delete_nganya():
  show_info()
  choice=int(input("Which matatu do you wish to remove from the system?"))
  if choice>len(nganyas):
    print("Index too high")
    os.system('cls')
    delete_nganya()
  else:
    nganyas.pop(choice)
    print("NGANYA SUCCESSFULLY REMOVED FROM SYSTEM")
    input("Press Enter to continue...")
    
def add_passenger():
  show_info()
  addpassenger=[]
  nganya_book=int(input("What is the index of the matatu you want to book? "))
  addpassenger.append(nganya_book)
  if nganya_book>len(nganyas):
    print("Index too high")
    add_passenger()
  seat_book=int(input("How many seats do you want to book? "))
  if seat_book>nganyas[nganya_book][3]:
    print("Sorry, we do not have that many available seats")
  else:
    nganyas[nganya_book][3]=nganyas[nganya_book][3]-seat_book
    #The above subtracts the seats booked from the available seats
  passenger_name=input("Kindly input your name: ")
  passenger_contact=int(input("Kinldy input your mobile number: "))
  addpassenger.append(passenger_name)
  addpassenger.append(nganyas[nganya_book][1])
  #The above adds the name of the booked matatu to the list
  addpassenger.append(seat_book)
  addpassenger.append(passenger_contact)
  passengers.append(addpassenger)
  print("SEATS SUCCESSFULLY BOOKED!")
  input("Press Enter to continue...")
  menu()

def cancel_booking():
  pass_cancel=input("Kindly enter your name: ")
  cancel_contact=int(input("Kindly enter your phone number: "))
  cancel_matatu=int(input("What is the index of the nganya you booked: "))
  chuja=0
  #Below, we check whether the phone number entered 
  #exists in each list in list passengers
  #if found, the initially booked seats are added to the currently
  #unbooked seats for the nganya initially booked
  #we store the number of seats in index 3 of 
  #both nganyas and passengers
  for passenger in passengers:
    for contact in passenger:
      if contact==cancel_contact:
        nganyas[cancel_matatu][3]+=passengers[chuja][3]
        passengers.pop(chuja)
        loading()
        print("SEAT SUCCESSFULLY REVOKED")
        input("Press Enter to continue...")
    chuja+=1
    #Chuja checks the specific index in list passengers 
    #where the number of seats booked is stored in the third index
    #And then, the specific index, represented by chuja, is popped
    #out
    
  menu() 

  
  
  #if seat_book
def admin():
  loading()
  breakline="=================================================================="
  print(breakline.center(60))
  print("********************MATATU BOOKING SYSTEM*******************".center(60))
  print(breakline.center(60))
  print("")
  print("<<<<<<<<<<<<<<<WELCOME ADMIN>>>>>>>>>>>>>>>".center(60))
  print("")
  print("************************************".center(60))
  print("||      CHOOSE YOUR OPERATION     ||".center(60))
  print("||--------------------------------||".center(60))
  print("||      [1] VIEW PASSENGERS       ||".center(60))
  print("||      [2] ADD NGANYA            ||".center(60))
  print("||      [3] DELETE NGANYA         ||".center(60))
  print("||      [4] BACK                  ||".center(60))
  print("||                                ||".center(60))
  print("************************************".center(60))
  print(breakline.center(60))
  choice=input("ENTER YOUR CHOICE: ".center(60))
  if choice=='1':
    print(tabulate(passengers,headers=col_names2,showindex=True))
    input("Press Enter to continue...")
    admin()
  elif choice=='2':
    add_nganya()
    admin()
  elif choice=='3':
    delete_nganya()
    admin()
  elif choice=='4':
    menu()

def password():
  PASSWORD="KIBO2022"
  trial=input("ENTER PASSWORD TO ACCESS ADMIN::  ")
  if trial==PASSWORD:
    admin()
  else:
    print("WRONG PASSWORD!")
    input("Press Enter to continue...")
    menu()
def loading():
  print("PROCESSING")
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  print(".")
  sleep(1)
  os.system("cls")
#THIS IS THE ONLY FUNCTION THAT IS EXECUTED ON RUN
first_passengers()

  