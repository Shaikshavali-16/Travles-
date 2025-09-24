import mysql.connector as mq
con=mq.connect(host='localhost',password='Shaiksha@93',user='root')


if con.is_connected():
    print("Connected successfully")

cur=con.cursor()
cur.execute("use travels")

while True:
    print('1...... Add Car')
    print('2...... Show Cars')
    print('3...... Available cars')
    print('4...... Rent a Car')
    print('5...... Close Rent Car')
    print('6...... Remove Car')
    print('7...... Exit')
    ch=int(input('Enter Choice ........'))
    if ch==1:
        cn=input('Enter Car name ')
        cm=input('Enter Car Model ')
        cnm=input('Enter Car Number ')
        ct=int(input('Enter Car Type 1/2 1-4Seats 2-7seats'))
        cur.execute('insert into cars(carname,model,Num,Type) values(%s,%s,%s,%s)',(cn,cm,cnm,ct))
        con.commit()
    elif ch==2:
        cur.execute("use travels")
        cur.execute('select carname,model,Type from cars')
        for i in cur:
            print(i)
    elif ch==3:
        print('Available cars.....  ')
        cur.execute('select Num from cars where Num NOT IN (select Num from customer)')
        for i in cur:
            print(i)
    elif ch==4:
        cnum=input('enter car number for rent ')
        rname=input('enter name of customer ')
        pn=input('enter phone number ')
        ad=input('enter address ')
        sm=int(input('enter starting meter reading '))
        ct=int(input('enter car type 1/2 '))
        dm=input('with driver y/n ')
        cur.execute('insert into customer(Num,Name,Phone,Address,Meter,Type,driver) values(%s,%s,%s,%s,%s,%s,%s)',(cnum,rname,pn,ad,sm,ct,dm))
        con.commit()
    elif ch==5:
        num=input('Enter car Number... ')
        my=(num,)
        q2='select Meter from customer where Num=%s'
        cur.execute(q2,my)
        end=int(input('Enter end meter reading... '))
        for i in cur:
            i1=int("".join(map(str,i)))
            rate=end-i1
            print(rate*12)
        q1='delete from customer where Num=%s'
        cur.execute(q1,my)
        con.commit()
    elif ch==6:
        num=input('Enter the car number to close the car....  ')
        my=(num,)
        q1='delete from cars where Num=%s'
        cur.execute(q1,my)
        con.commit()
    elif ch==7:
        break
