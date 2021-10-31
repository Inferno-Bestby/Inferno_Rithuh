import sqlite3;
from datetime import datetime;
from datetime import timedelta;
tot=float(0);
lisres=list();
lisresno=list();
omn=list();
omnc=list();
omncn=list();
con=sqlite3.connect('Food.db');
cur=con.cursor();
cur.execute('select ShopName from Shoplist;');
a=cur.fetchall();
resch=int();
menlis=list();

def menlist():
    cur.execute('select Shopno from Shoplist;');
    menlis=cur.fetchall();
    return menlis;
    
def menchk(menname):
    if menname in menlis:
        return False;
    else:
        print('Please enter valid Product Number ! ');
        return True;   


def rlist():
    k=1;
    print('List Of Shops:');
    print('Shop       ','Shop Number');
    for i in a:
        string=str(i);
        n=len(string);
        j=str();
        for m in range(2,n-3):
            j+=string[m];
        print(j.ljust(17,' '),k);
        lisres.append(j);
        lisresno.append(k);
        k+=1;
def menu(resch):
    cur.execute('select Productno,Productname,costprice, offerprice, Expiry from _{} ;'.format(resch));
    mlist=cur.fetchall();
    print('\nMENU'.center(20));
    print('(Product Number  ,Food Name , Actual Price, Offer price, Expiry Date)');
    print(*mlist,sep='\n');
    mench(resch);
    
def mench(resch):
    global tot;
    q=int(input('Enter the Product Number : '));
    cur.execute('select Productname,costprice, offerprice, Prodstock, Expiry from _{} where Productno={}'.format(resch,q));
    n=int(input( 'Enter the number to be ordered : '));
    d=cur.fetchone();
    mn=d[0];
    mc=d[1];
    mo=d[2];
    qn=d[3];
    if n<=qn:
        print('Food : {}\nCost per quantity : {}\nQuantity : {}'.format(mn,mo,n));
        cont=input('Enter Yes to continue : ');
        if cont.lower()=='yes' or cont.lower()=='y':
            cur.execute('update _{} set Prodstock={} where Productno={}'.format(resch,qn-n,q));
            tot+=mo*n;
            omn.append(mn);
            omnc.append(mo);
            omncn.append(n);
    else:
        print(' Sorry, the quantity not available!Available quantity = ',qn);
        
def bill(resch):
    print('BILL')
    print('FOOD ITEMS'.center(20),'COST PER QUANTITY '  ,"  NUMBER OF ITEMS  ", "COST");
    for i in range(len(omn)):
        print(str(omn[i]).ljust(20),"Rs.",omnc[i],'               ',omncn[i],"               Rs.",omnc[i]*omncn[i]);
    print('\nTOTAL =  '.ljust(60),tot);
    print('~'*50);
    
def  custdetails(resch):
    cuname=input('Enter your name : ');
    cuph=int(input('Enter your Phone Number : '));
    now = datetime.now()
    dt=datetime.now()+timedelta(minutes=30)
    #cur.execute('insert into Cust{} values(?,null,?,?)'.format(resch),(cuname,dt,cuph));
    #cur.execute('select Phno from Shoplist where Shopno ={}'.format(resch))
    #phone=cur.fetchall();
    #ph1=str(phone[0]);
    #ph3=list(ph1).remove(',')
    #ph2=str(ph3);
    print('Your Order Has Been Successfully Placed!');
    print('Expected time of delivery =  ',dt);
    print('The Seller will contact you soon.');
    #print('Restaurant Phone Number = ',ph2)

def search(resch):
    cons=[];
    sm=input('Enter the Product Name : ');
    cur.execute('select Productno,Productname from _{}'.format(resch));
    qw=cur.fetchall();
    mlist=list();
    a=str();
    for j in qw:
        mlist.append(j[1]);
    for k in mlist:
        a=str(k);
        for l in range(min(len(sm),len(a))):
            if a[l] in sm:
                a.replace(a[l],'$');
        cons.append(a.count('$'));
    re=cons.index(max(cons));
    cur.execute('select Productno,Productname,costprice, offerprice, Expiry from _{} where Productno={}'.format(resch,re+1) );
    a=cur.fetchone();
    print('Product Number, Product Name, Original Price, Offer Price, Expiry Date');
    print(a)
    comm=input('Is this the food you were looking at ? (Y/N)  ');
    if comm.lower()=='y' or comm.lower()=='yes':
        mench(resch);
    else:
        print('Sorry! Your desired search could not be matched ! ');

 #MAIN
print('\nWELCOME TO BESTBY!');
menlis = menlist();
rlist();
while True:
    shopch=int(input('Enter the Shop Number : '));
    sch =(shopch,)
    if sch in menlis:
            cur.execute('select ShopName from Shoplist where Shopno={}'.format(shopch));
            print('Shop Selected : ',cur.fetchone());
            confirm=input('Do you want to continue with this Shop?(Y/N)');
            if confirm.lower()=='y'or confirm.lower()=='yes':
                inputs=int(input('ENTER\n1. FOR PRODUCT LIST\n2. TO SEARCH A FOOD: '));
                if inputs==0:
                        import products;
                if inputs==1:
                    while True:
                        menu(shopch);
                        ch = input('Do you want to continue buying more products? (Y/N )')
                        if not(ch.lower()=='y' or ch.lower()=='yes'):
                            break;
                    inp=input('Do you want to display the bill and place your order ? (Y/N ) ');
                    if inp.lower()=='y' or inp.lower()=='yes':
                        bill(shopch);
                        custdetails(shopch);
                        break;
                if inputs==2:
                    search(shopch);
            else:
                rlist();
            print('THANK YOU FOR CHOOSING BESTBY!');

            break;
    else:
     print('Enter a valid Shop Number !');
