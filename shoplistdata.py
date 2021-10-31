import sqlite3;
tablis=tuple();

class shoplist:
    shopnumber=list();
    def unishopno(self,gr):
        cursor.execute('select * from Shoplist;');
        self.shopnumber=cursor.fetchall();
        a=len(self.shopnumber)
        r=list();
        for i in range(a):
            r.append(self.shopnumber[i][1]);
        for i in r:
            if gr==i:
                return True;
        else:
                return False;

    def search(self):
        r=int(input("Enter the Shop number: "));
        t=self.unishopno(r);
        if t:
            cursor.execute("select * from Shoplist where Shopno ={};".format(r));
            shop=cursor.fetchone();
            print('(Shop Name   ,Shop Number , Phone Number )');
            print(shop);
        else:
            print('Shop Number not found!');
        return r;

    def create(self):
        cursor.execute("select name from sqlite_master where type='table'");
        a=cursor.fetchall();
        i=('Shoplist',);
        if i not in a: 
            cursor.execute('create table Shoplist(ShopName varchar(30) not null,Shopno integer not null primary key,Phno integer(10));');
            print('List of Shops Table is created');
        else:
            print('List of Shops Table is already created!');
   
    def insert(self):
        name=input('Enter the Shop name: ');
        sno=int(input('Enter the Shop Number: '));
        pno=int(input('Enter the Phone Number of the Shop : '));
        true=self.unishopno(sno);
        if not(true):
            cursor.execute(f"insert into Shoplist values('{name}',{sno},{pno});");
            cursor.execute('create table _{}(Productno integer primary key not null,Productname char(30) not null, costprice dec(5,2) not null,offerprice dec(5,2) not null,Prodstock integer(4) default 0,Expiry char(11) not null);'.format(sno));
            connection.commit();
        if true:
            print('Shop Number Already Exists!');
            self.insert();

    def update(self):    
        sno=int(input('Enter the Shop Number: '));
        true=self.unishopno(sno);
        if true:
            c=input('Enter:\n\tn for Shop Name\n\tr for Shop Number\np for Phone Number of the Shop\n\tEnter your choice: ');
            if c.lower()=='n':
                name=str(input('Enter the Shop name: '));
                cursor.execute("""update Shoplist set RestName = '{}' where Resno={}""".format(name,sno));
                print('Done!\n');
            if c.lower()=='r':
                newsno=int(input('Enter the new Restaurant Number: '));
                t=self.unishopno(newsno);
                if not t:
                    cursor.execute('update Shoplist set Shopno={} where Shopno={}'.format(newsno,sno));
                    print('Done!\n');
                else:
                    print('The Restaurant Number already exists!');
            if c.lower()=='p':
                p=int(input('Enter the Phone Number : '));
                cursor.execute('update Shoplist set Phno={} where Shopno={}; '.format(p,sno));
                print('Done!\n');
        connection.commit();
        if not(true):
            print("SHOP NUMBER DOESN'T EXIST!")

    def delete(self):
        sno=self.search();
        choice=input('Do you want to proceed?(Y/N) ')
        if choice=='y'or choice=='Y'or choice=='yes'or choice=='Yes':
            cursor.execute("Delete from Shoplist where Shopno = {};".format(sno));  
            connection.commit();
            print('Done!');
    

###MAIN
connection=sqlite3.connect('Food.db');
cursor=connection.cursor();
market = shoplist();
modext=input('Enter Password to Modify the data of list of Shops : ');
if modext.lower()=='password':
    while True:
        samplestring='MENU'
        print(samplestring.center(20,'*'),"\nEnter :");
        print('1. Create table');
        print('2. Insert A Shop Detail');
        print('3. Update A Shop Detail');
        print('4. Delete A Shop Detail');
        print('5. Search A Shop Detail');
        print('6. Exit');
        choice=int(input("\nEnter your choice: "));
        if choice==1:
              market.create();
        if choice==2:
              market.insert();
        if choice==3:
              market.update();
        if choice==4:
              market.delete();
        if choice==5:
              market.search();
        if choice==6:
            print('Program Has Ended!');
            break;

