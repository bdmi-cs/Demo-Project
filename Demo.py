import mysql.connector as sql
conn=sql.connect(host='localhost',user='bdmi',password='bdmi123',database='school')
c1=conn.cursor()

def Cur_Date():
    from datetime import date
    today = date.today() 
    return (str(today.day)+"/"+str(today.month)+"/"+str(today.year))


def print_table(table):
    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 3)
        for i in range(len(table[0]))
    ]
    row_format = "".join(["{:<" + str(longest_col) + "}" for longest_col in longest_cols])
    for row in table:
        print(row_format.format(*row))


def clrscr():
    import os
    os.system('CLS')

def Login():
    print()
    value_1=value_2=""
    user=input('User Name : ')
    user=user.upper()
    c1.execute("select * from account_details where User_Name like '" + user + "'")
    datas=c1.fetchall()
    #print("ok",datas)
    for i in datas:
        value_1=i[0]
        value_2=i[1]

    #print(user, value_1)
    if user==value_1.upper():
        password=input('Password : ')
        password=password.upper()
        if password==value_2:
            print()
            print('Login successfull')
            return 1

    print("Wrong Login Details")            
    return 0

        
def Add_Medi():
    print("Enter Medicine Detials")
    c=int(input("Enter medicine code: "))
    n=input("Enter medicine name: ")    
    p=float(input("Enter medicine price: "))
    g=p*0.05
    tp=p+g
    cn=input("Enter Company Name: ")
    dt_m=input("Enter Date of Manufacture(dd/mm/yyyy): ")
    dt_e=input("Enter Date of Expiry(dd/mm/yyyy): ")
    q=0

    query="insert into medicines_details(medicine_name,medicine_code,price,gst,total_cost,company_name,dt_manuf,dt_exp,qty)values('{}',{},{},{},{},'{}','{}','{}',{})".format(n,c,p,g,tp,cn,dt_m,dt_e,q)
    c1.execute(query)
    conn.commit()
    print("Record added successfully....")
    

def Purchase_Medi():
    mc=(input("Enter medicine code: "))
    c1.execute("select * from medicines_details where medicine_code like '" + mc + "'")
    datas=c1.fetchall()
        
    if (datas):
        q=int(input("Enter Quantity: "))
        np=str(int(datas[0][8])+q)
        #print(type(np), np)
        c1.execute("update medicines_details set qty="+np+" where medicine_code like '" + mc + "'")
        conn.commit()
    else:
        print("\n\t***Medicine details are not available. Add medicine details in the database...")
    

def Search():
    while(True):
        #clrscr()
        print("\n************************* SEARCH MENU ************************")
        print("\n 1. Search Medicine Details by Name")
        print("\n 2. Search Medicine Details by code")
        print("\n 3. List of Medicine Details")
        print("\n 4. Back to Main Menu")
        
        ch=int(input("\n Enter your choice(1-4): "))
        print("\n*****************************************************")
        if ch==1:
            m=input("Enter Medicine Name: ")
            Search_Medi_Name(m)
            pk=input("\n\tPress any key to continue......")
        elif ch==2:
            c=input("Enter Medicine Code: ")
            Search_Medi_Code(c)
            pk=input("\n\tPress any key to continue......")
        elif ch==3:
            Search_Medi_Details()
            pk=input("\n\tPress any key to continue......")
        elif ch==4:
            break


    

    
def Search_Medi_Name(m_name):
    c1.execute("select * from medicines_details where medicine_name like '" + m_name + "'")
    datas=c1.fetchall()
    if (datas):
        print("Medicine details: \n")
        print("Code               : ",datas[0][0])
        print("Name               : ",datas[0][1])
        print("Price              : ",datas[0][2])
        print("GST                : ",datas[0][3])
        print("Price(with gst)    : ",datas[0][4])
        print("Company Name       : ",datas[0][5])
        print("Date of Manufacture: ",datas[0][6])
        print("Date of Expire     : ",datas[0][7])
        print("Quantity           : ",datas[0][8])      
    else:
        print("\nRecord not found.....")    

def Search_Medi_Code(m_c):
    c1.execute("select * from medicines_details where medicine_code like '" + m_c + "'")
    datas=c1.fetchall()
    if (datas):
        print("Medicine details: \n")
        print("Code               : ",datas[0][0])
        print("Name               : ",datas[0][1])
        print("Price              : ",datas[0][2])
        print("GST                : ",datas[0][3])
        print("Price(with gst)    : ",datas[0][4])
        print("Company Name       : ",datas[0][5])
        print("Date of Manufacture: ",datas[0][6])
        print("Date of Expire     : ",datas[0][7])
        print("Quantity           : ",datas[0][8])      
    else:
        print("\nRecord not found.....")

def Search_Medi_Details():
    c1.execute("select * from medicines_details")
    datas=c1.fetchall()
    
    if (datas):
        l=len(datas)
        for i in range(l):
            rec=[]
            r=[]
            r.append(str(datas[i][0]))
            r.append(str(datas[i][1]))
            r.append(str(datas[i][2]))
            rec.append(r)
            print(rec)
            print_table(rec)
    else:
        print("\nRecord not found.....")


        

def Add_Customer():
    print("***********************ADD CUSTOMER****************************")
    
    print("Input Customer Detials")
    c=int(input("Enter Customer Code: "))
    n=input("Enter Customer Name: ")
    age=int(input("Enter Customer Age: "))
    a=input("Enter Customer Address: ")
    pn=int(input("Enter Customer Mobile Number: "))
    dn=input("Enter Doctor Name: ")

    query="insert into customers_details(cust_code,cust_name,age,address,mobile_number,doctor_name)values({},'{}',{},'{}',{},'{}')".format(c,n,age,a,pn,dn)
    
    c1.execute(query)
    conn.commit()
    print("Record added successfully....")
    
def Search_Cust(c_name):
    c1.execute("select * from customers_details where cust_name like '" + c_name + "'")
    datas=c1.fetchall()
    if (datas):
        print("Customer details: \n")
        print("Code         : ",datas[0][0])
        print("Name         : ",datas[0][1])
        print("Age          : ",datas[0][2])
        print("Address      : ",datas[0][3])
        print("Mobile Number: ",datas[0][4])
        print("Doctor Name  : ",datas[0][5])
    else:
        print("\nRecord not found")    


 
'''
Modules of Medical Shop Management System:

    Login: Using this module user enters user name and password and the system checks whether it is valid. If it is valid user can log in, otherwise invalid user name and password message is displayed.
    Purchase: This module allows purchasing medicines from the supplier.
        It contains fields such as batch number, manufacture date, expiry date, company name, etc.
        
    Sales module: This module consists of customer sales information. When sale is made proper
                    fields in the sale form should be filled such as patient name, address,
                    doctor’s name, medicine details etc.
        
    Stock module: This module manages the inventory. Stock is updated when purchase, sale or
        replace is made.
    Medicine: This module consists of information of medicines available in the Medical.
    
    Organize: This module allows the user to store medicine in an organized manner. So that the distributor can find the required medicines effortlessly.
    Employee: Using this module the user can add employee name, update his details and generate
    payrolls with great ease.
    Report generation: Using this module user can generate different kinds of reports
                        such as sales details, purchase details, etc.

'''

def Bill_Generate():
    #record=[]
    record=[["Code", "Medicine Name", "Price","Quantity", "Total Price"],["----","-------------","-----","--------","-----------"]]
    total_amt=0.0
    flag=0
    
    print("\n\t\tBill Generate ")
    c=(input("\nEnter Customer code: "))
    c1.execute("select * from customers_details where cust_code like '" + c + "'")
    datas=c1.fetchall()
    if (datas):
        #print("Yes, Details",datas[0][0], datas[0][1])
        while(True):
            mc=input("\nEnter Medicine Code: ")
            c1.execute("select * from medicines_details where medicine_code like '" + mc + "'")
            rs=c1.fetchall()
            if rs:
                #print("Y", rs[0][1], rs[0][4],rs[0][8])
                q=int(input("Enter Quantity: "))
                nq=rs[0][8]-q
                
                if (nq>=0):
                    #print("Stock Available")
                    flag=1
                    row=[]
                    c1.execute("update medicines_details set qty="+str(nq)+" where medicine_code like '" + mc + "'")
                    conn.commit()

                    cur_dt=Cur_Date()
                    #print(cur_dt)
                    c=int(c)
                    mc=int(mc)
                    pr=rs[0][4]
                    tot_pr=q*pr
                    total_amt=total_amt+tot_pr
                    c1.execute("insert into sale(date,m_code,c_code,qty,price,total_price)values('{}',{},{},{},{},{})".format(cur_dt,mc,c,q,pr,tot_pr))
                    #c1.execute(v_sql_insert)
                    conn.commit()
                    row.append(mc)
                    row.append(rs[0][1])
                    row.append(pr)
                    row.append(q)
                    row.append(tot_pr)
                    record.append(row)
                    
                else:
                    print("\n\t\tOut of stock.....")                
            else:
                print("\n\tMedicine Not Avialable.... Try Again\n")
            ch=input("Do you wnat to continue(Y/N): ")
            if ch.upper()=="N":
                break

        #print("Bill Generated........")

        if flag==1:
            print("Please wait.. your bill generating.....")
            print("\n****************** BILL *********************\n")
            print("Customer Code: ",c)
            print("Customer Name: ",datas[0][1])
            print("Customer Address: ",datas[0][3])
            print("Customer Mobile Nomber: ",datas[0][4])
            print("************************************************\n")

            print_table(record)
            print("\n\t\t Total amount to pay: ",total_amt)
    else:
        print("Customer Code not found...... Try Again!!!!!!")
    

def Report():
    while(True):
        #clrscr()
        print("\n************************* REPORT MENU ************************")
        print("\n 1. Sales Details")
        print("\n 2. Purchase Details")
        print("\n 3. Stock")
        print("\n 4. Back to Main Menu")
        
        ch=int(input("\n Enter your choice: "))
        print("\n*****************************************************")
        if ch==1:
            pk=input("\n\tPress any key to continue......")
        elif ch==2:
            print("2")
            pk=input("\n\tPress any key to continue......")
        elif ch==3:
            print("3")
            pk=input("\n\tPress any key to continue......")
        elif ch==4:
            break

def Update_Data():
    while(True):
        #clrscr()
        print("\n************************* UPDATE MENU ************************")
        print("\n 1. Update Customer Details")
        print("\n 2. Update Medicine Details")
        print("\n 3. Back to Main Menu")
        
        ch=int(input("\n Enter your choice(1-3): "))
        print("\n*****************************************************")
        if ch==1:
            pk=input("\n\tPress any key to continue......")
        elif ch==2:
            print("2")
            pk=input("\n\tPress any key to continue......")
        elif ch==3:
            break

    
    
###### MAIN METHOD #######

while(True):
    val=Login()
    if val==1:
        break

print(Cur_Date())
while(True):
        clrscr()
        
        print("\n************************* MAIN MENU ************************")
        print("\n 1. Add Medicine")
        print("\n 2. Purchase Medicine")
        print("\n 3. Search Medicine")
        print("\n 4. Add Customer")
        print("\n 5. Search Customer Details")
        print("\n 6. Bill Generate")
        print("\n 7. Report")
        print("\n 8. Update Data")
        print("\n 9. Exit")
        ch=int(input("\n Enter your choice(1-9): "))
        print("\n*****************************************************")
        if ch==1:
            Add_Medi()
            pk=input("\n\tPress any key to continue......")
        elif ch==2:
            Purchase_Medi()
            pk=input("\n\tPress any key to continue......")    
        elif ch==3:
            Search()
        elif ch==4:
            Add_Customer()
            pk=input("\n\tPress any key to continue......")
        elif ch==5:
            cn=input("Enter Customer Name: ")
            Search_Cust(cn)
            pk=input("\n\tPress any key to continue......")
        elif ch==6:
            Bill_Generate()
            pk=input("\n\tPress any key to continue......")
        elif ch==7:
            Report()
            #pk=input("\n\tPress any key to continue......")
        elif ch==8:
            Update_Data()
            #pk=input("\n\tPress any key to continue......")
        elif ch==9:
            print("Thank you!!!!!")
            break
        else:
            print("Wrong choice. Enter any number between 1 - 9")
            pk=input("\n\tPress any key to continue......")

conn.close()
        
