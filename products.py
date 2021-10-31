#Shoplistdata is imported in this file
import sqlite3;
tablis=list();
h2=int();
shopno=list();
shopn=list();
connect=sqlite3.connect('Food.db')
cur=connect.cursor();
def tbchk(tname):
    if tname in tablis:
        return False;
    else:
        print('Enter valid table name ');
        return True;   


def create():
    import shoplistdata;
    h1=shoplistdata.shoplist();
    h2=h1.search();
    cursor.execute('select ShopName from Shoplist where Shopno={}'.format(h2));
    h3=cursor.fetchone();
    tblst();
    a='_'+str(h2);
    if a not in tablis:   
        cursor.execute('create table _{}(Productno integer primary key not null,Productname char(30) not null, costprice dec(5,2) not null,offerprice dec(5,2) not null,Prodstock integer(4) default 0,Expiry char(11) not null);'.format(h2));
        
        #cursor.execute('create table Cust{} (Custname char(30) not null,Cusid integer primary key, Deletime time(0) not null,Phno integer(10))'.format(h2));
        shopno.append(h2);
        shopn.append(h3);
    else:
        print('Table is already created!');
        print('Please proceed with the other options');

def tblst():
    global tablis;
    cursor.execute("select name from sqlite_master where type ='table'; ");
    tl=cursor.fetchall();
    n=len(tl);
    tablis=list();
    shopn=list();
    prodno=str();
    for i in range(n):
    #    reno=tl[i][0];
    #for j in reno:
    #       if j =='1' or j== '2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9' or j=='0':
    #           menno+=j;
     tablis.append(tl[i][0]);
        #cursor.execute('select RestName from Restlist where Resno={};'.format(int(menno)));
        #resn.append(cursor.fetchone());
    #print('(Table name, Restaurant Name)')
    #for i in tablis:
     #   print(i,resn[tablis.index(i)]);

def uniprodno(gr,b):
    cursor.execute('select *  from {}; '.format(b));
    productnumber=cursor.fetchall();
    a=len(productnumber);
    r=list();
    for i in range(a):
        r.append(productnumber[i][0]);
    for i in r:
        if gr==i:
            return True;
    else:
            return False;

def display():
    tblst();
    cur.execute('select * from ShopList;')
    row = cur.fetchall();
    print('Shop Name, Shop Number, Phone Number');
    for i in row:
        print(i);
    a=int(input('Please enter the Shop Number: '));
    sch =(a,)         
    cur.execute("select * from _{};".format(a));
    print('(Product Name , Product Number , Actual Price , Offer Price , Quantity Available , Expiry Date)');
    row= cur.fetchall();
    for i in row:
        print(i);
    
def insert():
    tblst();
    for i in tablis:
        print(i);
    a=input('Please enter the table name : ');
    cho=tbchk(a);
    if cho:
         insert();
    else:
        name=input('Please enter the Product name : ');
        pno=int(input('Please enter the Product Number : '));
        true=uniprodno(pno,a);
        if not(true):
            c=int(input('Please enter the Original Price: '));
            o=int(input('Please enter the Offer Price: '));
            tn=int(input('Please enter the Quantity Available : '));
            e = input('Please enter the Expiry Date (DD/MM/YYYY)');
            cursor.execute("insert into {} values(?,?,?,?,?,?);".format(a),(pno,name,c,o,tn,e));
            connection.commit();
        if true:
            print('Product Number Already Exists!');
            insert();

def update():
    tblst();
    a=input('Enter the table name: ');
    cho=tbchk(a);
    if  cho:
         update();
    pno=int(input('Please enter the Product Number: '));
    true=uniprodno(pno,a);
    if true:
        c=input('Please enter the corresponding letter for changing:\nn for Product Name\nr for Product number\nt for Original Price\no for Offer Price\ne for Stock\nf for Expiry Date\nEnter your choice: ');
        if c=='n':
            name=input(('Please enter the Product Name: '));
            cursor.execute("update {} set Productname = '{}' where Productno={};".format(a,name,pno));
        if c=='r':
            newpno=int(input('Please enter the new Product Number: '));
            t=unimeno(newpno,a);
            if not t:
                cursor.execute("""update {} set Productno = {} where Productno={}""".format(a,newpno,pno));
            if t:
                print('Product Number already exists! ');
        if c=='t':
            t=int(input('Please enter the Original Cost Price : '));
            cursor.execute("""update {} set costprice = {} where Productno={}""".format(a,t,pno));
        if c=='o':
            t=int(input('Please enter the Selling Price : '));
            cursor.execute("""update {} set offerprice = {} where Productno={}""".format(a,t,pno));
        if c=='e':
            e=int(input('Please enter the Stock : '));
            cursor.execute("""update {} set Prodstock = {} where Productno={}""".format(a,e,pno));
        if c=='f':
            e=input('Please enter the Expiry Date(DD/MM/YYYY) : ');
            cursor.execute('update {} set Expiry ={} where Productno = {} '.format(a,e,pno));
        connection.commit();
    if not(true):
        print("PRODUCT NUMBER DOESN'T EXIST!")

def delete():
    a,pno=search();
    choice=input('Do you want to proceed?(Y/N) ')
    if choice=='y'or choice=='Y'or choice=='yes'or choice=='Yes':
        cursor.execute("Delete from {} where Productno = {};".format(a,pno));
        connection.commit();
        print('Deleted!');
    else:
        print('Not Deleted');

###MAIN
connection=sqlite3.connect('Food.db');
cursor=connection.cursor();
tname=cursor.fetchone();
while True:
        print("MENU:\nPlease enter :");
        print('1. Insert  A   Product Detail');
        print('2. Update  A   Product Detail');
        print('3. Delete  A   Product Detail');
        print('4. Display All Product Details');
        print('5. Exit');
        choice=int(input("\nPlease enter your choice: "));
        if choice==0:
              create();
        if choice==1:
              insert();
        if choice==2:
              update();
        if choice==3:
              delete();
        if choice==4:
              display();
        if choice==5:
            print('Program Has Ended!');
            break;
connection.close();
