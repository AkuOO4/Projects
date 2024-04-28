import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1999',database='vps')
cur = conn.cursor()
print("=========================WELCOME TO YOLA'S CAR SERVICE========================")
def scar():
    print("SLNO, CARNAME, RATE/DAY, DATE  OF TAKING THE CAR")
    cur.execute('select slno,carname,rate,takedate from rentcar')
    b=cur.fetchall()
    for x in b:
        print(x)
def rentcar():
    
    from datetime import date
    tdate=date.today()

    a=input("                    Enter the name of car: ")
    b=input("                   Enter your name: ")
    c=int(input("             Enter phonenumber: "))
    cur.execute("update rentcar set status='notavailable' where carname='"+a+"'")
    cur.execute("update rentcar set reciever='"+b+"' where carname='"+a+"'")
    cur.execute("update rentcar set phoneno='"+str(c)+"' where carname='"+a+"'")
    cur.execute("update rentcar set takedate='"+str(tdate)+"' where carname='"+a+"'")
    conn.commit()
    print("thankyou for taking the car:",a)

def rcar():
    from datetime import date
    from datetime import timedelta
    rdate=date.today()
    a=input("                 enter name  of car:")
    cur.execute("select takedate from rentcar where carname='"+a+"'")
    b=cur.fetchall()
    x=b[0]
    y=x[0]
    cur.execute("select rate from rentcar where carname='"+a+"'")
    c=cur.fetchall()
    g=c[0]
    h=g[0]
    conn.commit()
    d=rdate-y
    print("today's date is ",date.today())
    
    i= int(input("how many days the car was with you"))
    
    print("amount to pay Rs.",i*h)
    
    print("thank you for returning the car",a)



def acar():
   
    a=input("                enter name of car         :")
    cur.execute("select max(slno) from rentcar")
    c=cur.fetchall()
    d=c[0]
    e=d[0]+1
    f=input("enter the rate of car/day")
    cur.execute("insert into rentcar (slno,carname,rate)  values ("+str(e)+",'"+a+"','"+str(f)+"') ")   
    conn.commit()
    print("DATA ADDED SUCCESFULLY")

def avcar():
     cur.execute("select slno,carname,rate from rentcar where status='available'")    
     x=cur.fetchall()
     conn.commit()
     for i in x:
         print(i)
        
def menu():
    print("          SHOWROOM         ")
    c='yes'
   
    while c=='yes':
    
        print("                  1.SHOW CARS")
        print("                   2.TAKE CARS")
        print("                   3.RETURN CARS")
        print("                   4.ADD CARS")
        
        print("                  5.SHOW AVAILABLE CARS")
        print()
        print()
        choice=int(input("                   enter the choice:"))
        
        if choice==1:
            scar()
        elif choice==2:
            rentcar()
        elif choice==3:
            rcar()
        elif choice==4:
            acar()
       
        elif choice==5:
             avcar()
       
        else:
            print ("exit")
            break
        print()
        print()
        c=input("do you want to continue or not(yes or no):")
    else : print("Thank You")
    
menu()  