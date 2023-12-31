import getpass
import sqlite3
connection=sqlite3.connect('hospital.db')
cursor=connection.cursor()
error=1
from os import system, name
def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')
cursor.execute("""select count(name) from sqlite_master where type='table' and name='doctor'""")
result = cursor.fetchone()
if result is not None and result[0] == 0:
    cursor.execute("""CREATE TABLE doctor ( 
    d_id number primary key, 
    dnamedfirst VARCHAR2(20), 
    dnamedlast VARCHAR2(30), 
    password varchar2(20) not null,
    speciality varchar2(40) not null,
    shift varchar2(10) not null,
    phone number(10) not null);""")
cursor.execute("""select count(name) from sqlite_master where type='table' and name='doctor'""")
result = cursor.fetchone()
if result is not None and result[0] == 0:
    cursor.execute("""CREATE TABLE patient_details ( 
    pd_id number primary key, 
    pdnamedfirst VARCHAR2(20), 
    pdnamedlast VARCHAR2(30), 
    password varchar2(20) not null,
    pdconsultant varchar2(40) not null,
    pdhissue varchar2(10) not null,
    pddoa date not null,
    pddob date not null,
    pdage number(10) not null,
    pdcontact number(10) not null );""")
cursor.execute("""select count(name) from sqlite_master where type='table' and name='patient_details'""")
result = cursor.fetchone()
if result is not None and result[0] == 0:
    cursor.execute("""CREATE TABLE patient ( 
    p_id number primary key, 
    pfirst VARCHAR2(20), 
    pdlast VARCHAR2(30), 
    City varchar2(20) not null,
    DOB date not null,
    age number not null,
    DOA date not null,
    number number(10) not null);""")
    cursor.execute("""CREATE TABLE virus ( 
    p_id number not null, 
    dname VARCHAR2(20) primary key,
    vname VARCHAR2(20), 
    treatment VARCHAR2(50), 
    symptoms varchar2(50) not null);""")
    cursor.execute("""CREATE TABLE bacteria ( 
    p_id number not null, 
    dname VARCHAR2(20) primary key,
    bname VARCHAR2(20), 
    treatment VARCHAR2(50), 
    symptoms varchar2(50) not null);""")
    cursor.execute("""CREATE TABLE injury ( 
    p_id number not null, 
    iname VARCHAR2(20) primary key,
    idiagnosis VARCHAR2(50), 
    type varchar2(50) not null);""")
    cursor.execute("""insert into patient values(101,'Mohit','Nayak','Banglore','15-March-2001',18,'08-December-2020',9078435952)""")
    cursor.execute("""insert into patient values(102,'Anikiat','Saraf','Kolkata','22-Dec-2000','19','15-Feb-2020',9674825476)""")
    cursor.execute("""insert into patient values(103,'Rishank','Pratik','Orissa','22-Dec-2001','18','19-Nov-2015',9117854569)""")
    cursor.execute("""insert into patient values(104,'Risav','Jana','Nepal','06-Jan-2001',18,'25-Oct-2010',7854963284)""")
    cursor.execute("""insert into patient values(105,'Wilson','Vidyut','Mumbai','23-Nov-2001',18,'23-Nov-2005',7854129645)""")
    cursor.execute("""insert into patient values(106,'Dinesh','Sharma','Rajasthan','23-Feb-2000',20,'23-Feb-2020',8476423858)""")
    cursor.execute("""insert into virus values(003,'Ebola','Ebov','Oxygen Therapy, IV Fluids','Muscle Pain, Fever, Bleeding')""")
    cursor.execute("""insert into virus values(005,'Measles','Paramyxo','Vitamin A','Cough, Skin Rash')""")
    cursor.execute("""insert into bacteria values(001,'TB','Mycobacterium','Antibiotics','Cough and Sneezes')""")
    cursor.execute("""insert into bacteria values(006,'Cholera','Vibrio','IV Fluids, Antibiotics','Seizures, Diarrhoea')""")
    cursor.execute("""insert into injury values(002,'Hair line Fracture','Plaster, Pain Killer','Toe Fracture')""")
    cursor.execute("""insert into injury values(004,'bullet wound','Removal of Bullet','Wound')""")
    print("Databse created successfully")
result = cursor.fetchone()
if result is not None and result[0] == 0:
    cursor.execute("""CREATE TABLE patient_report ( 
    pr_id number primary key, 
    prnamed VARCHAR(20),  
    prdob date not null,
    prage number not null,
    prpno number (10) not null,
    pbloodgrp varchar(20),
    pgender varchar(20),
    prdoa date not null,
    prhissue varchar2(10) not null,
    prprtest varchar2(40) not null,
    prpdone varchar2(40) not null,
    prmedicines varchar2(60) not null,
    paddyn varchar2(20) not null,
    prdays  number not null);""")
result = cursor.fetchone()
if result is not None and result[0] == 0:
    cursor.execute("""CREATE TABLE feedback ( 
    f_id number primary key, 
    fnamed VARCHAR(100), 
    fcity VARCHAR(20),
    fdof date not null,
    feedback  VARCHAR(2000) not null);""")

else:
    e=1
    while e!=0:
        e=int(input("1.Doctor's Sign In\n2. Create a New Doctor Account\n3.Patient's Sign In \n4.New registration"))
        if e==2:
            did=int(input('\nEnter id - '))
            dnf=input('Enter first name - ')
            dnl=input('Enter last name - ')
            pas=input('Enter password - ')
            spec=input('Enter speciality - ')
            shf=input('Enter working shift - ')
            ph=int(input('Enter phone number - '))
            cursor.execute("""insert into doctor values(?,?,?,?,?,?,?)""",(did,dnf,dnl,pas,spec,shf,ph))
            screen_clear()

        if e == 4:
                pdid=int(input('\nEnter id - '))
                pdfn=input('Enter first name - ')
                pdln=input('Enter last name - ')
                pas1=input('Enter password - ')
                pdcon=input('Enter the consultant name - ')
                pdhi=input('Enter the health issue - ')
                pdda=input('Enter the date of admission - ')
                pddb=input('Enter the date of birth - ')
                pdage=int(input('Enter the age - '))
                ph1=int(input('Enter phone number - '))
                cursor.execute("""insert into patient_details values(?,?,?,?,?,?,?,?,?,?)""", (pdid,pdfn,pdln,pas1,pdcon,pdhi,pdda,pddb,pdage,ph1))
                screen_clear()

        elif e==1:
            while error==1:
                i=input("\nEnter your ID - ")
                p=input("Enter your Password - ")
                cursor.execute("""select count(d_id) from doctor where d_id=(?)""",(i,))
                if cursor.fetchone()[0]==1:
                    cursor.execute("""select count(password) from doctor where password=?""",(p,))
                    if cursor.fetchone()[0]==1:
                        print("\nSign in successful!")
                        screen_clear()
                        error=0
                        e=0
                        r=1
                        cursor.execute("""select d_id,dnamedfirst,dnamedlast,speciality,shift,phone from doctor where d_id=(?)""",(i,))
                        for row in cursor.fetchall():
                           print("ID -",row[0],"  Name -",row[1], row[2],"  Speciality -",row[3],"\nShift -",row[4],"  Phone Number -",row[5])
                        while r!=0:
                           print("\n1. View Patient details\n2. Add a New Patient\n3. patient's treatment report\n4.Delete Patient Details\n0. Exit")
                           r=int(input())
                           if r==1:
                              access=input("\nEnter Patient ID:- ")
                              cursor.execute("""select count(*) from patient where p_id=(?)""",(access,))
                              if cursor.fetchone()[0]!=0:
                                 cursor.execute("""select * from patient where p_id=(?)""",(access,))
                                 print("\nPatient Details - ")
                                 for row in cursor.fetchall():
                                    print("Id: ", row[0])
                                    print("First Name: ", row[1])
                                    print("Last Name: ", row[2])
                                    print("City: ", row[3])
                                    print("Date of Birth: ", row[4])
                                    print("Age: ", row[5])
                                    print("Date of Admission: ", row[6])
                                 print("\nDiagnosis Report - ")
                                 cursor.execute("""select count(*) from virus where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""select * from virus where p_id=(?)""",(access,))
                                    for row in cursor.fetchall():
                                       print("Id: ", row[0])
                                       print("Disease Name: ", row[1])
                                       print("Virus Name: ", row[2])
                                       print("Treatment: ", row[3])
                                       print("Symptoms: ", row[4])
                                    print("\n")
                                 cursor.execute("""select count(*) from bacteria where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""select * from bacteria where p_id=(?)""",(access,))
                                    for row in cursor.fetchall():
                                       print("Id: ", row[0])
                                       print("Disease Name: ", row[1])
                                       print("Bacteria Name: ", row[2])
                                       print("Treatment: ", row[3])
                                       print("Symptoms: ", row[4])
                                    print("\n")
                                 cursor.execute("""select count(*) from injury where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""select * from injury where p_id=(?)""",(access,))
                                    for row in cursor.fetchall():
                                       print("Id: ", row[0])
                                       print("Injury Name: ", row[1])
                                       print("Diagnosis Name: ", row[2])
                                       print("Type: ", row[3])
                                    print("\n")
                              else:
                                 print("Incorrect Patient id")
                           elif r==2:
                              pid=int(input('\nEnter id - '))
                              pnf=input('Enter first name - ')
                              pnl=input('Enter last name - ')
                              pcity=input('Enter city - ')
                              pdob=input('Enter date of birth - ')
                              page=int(input('Enter age - '))
                              pdoa=input('Enter date of admission - ')
                              pnum=int(input('Enter phone number - '))
                              cursor.execute("""insert into patient values(?,?,?,?,?,?,?,?)""",(pid,pnf,pnl,pcity,pdob,page,pdoa,pnum))
                              print("\n1. Virus\n2. Bacteria\n3. Injury")
                              m=int(input())
                              if m==1:
                                 dname=input("\nEnter disease name - ")
                                 bname=input("Enter virus name - ")
                                 treatment=input("Enter treatment - ")
                                 symptoms=input("Enter symptoms - ")
                                 cursor.execute("""insert into virus values(?,?,?,?,?)""",(pid,dname,bname,treatment,symptoms))
                              elif m==2:
                                 dname=input("\nEnter disease name - ")
                                 bname=input("Enter bacteria name - ")
                                 treatment=input("Enter treatment - ")
                                 symptoms=input("Enter symptoms - ")
                                 cursor.execute("""insert into bacteria values(?,?,?,?,?)""",(pid,dname,bname,treatment,symptoms))
                              elif m==3:
                                 iname=input("\nEnter injury name - ")
                                 idiag=input("Enter diagnosis - ")
                                 itype=input("Enter injury type - ")
                                 cursor.execute("""insert into injury values(?,?,?,?)""",(pid,iname,idiag,itype))
                              print("\nPatient Added")
                              connection.commit()
                           elif r==3:
                               tid=input("patient id: ")
                               tname=input("Name of the patient: ")
                               tdob=input("Date of birth: ")
                               tage=input("age of the patient: ")
                               tphno=int(input("phone number: "))
                               tbg=input("Blood group: ")
                               tgen=input("Gender of the patient: ")
                               tdoa=input("Date of the admission: ")
                               tis=input("Health issue of the patient: ")
                               tpre=input("tests prescribed: ")
                               tdone=input("tests done: ")
                               tmed=input("medicines are:  ")
                               tadd=input("Is there a need to get admitted(Y/N): ")
                               tdays=input("No of the days to be admitted: ")
                               cursor.execute("""insert into patient_report values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",(tid,tname,tdob,tage,tphno,tbg,tgen,tdoa,tis,tpre,tdone,tmed,tadd,tdays))
                           elif r==4:
                              access=input("\nEnter Patient ID:- ")
                              cursor.execute("""select count(*) from patient where p_id=(?)""",(access,))
                              if cursor.fetchone()[0]!=0:
                                 cursor.execute("""delete from patient where p_id=(?)""",(access,))
                                 cursor.execute("""select count(*) from virus where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:2

                                 cursor.execute("""delete from virus where p_id=(?)""",(access,))
                                 cursor.execute("""select count(*) from bacteria where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""delete from bacteria where p_id=(?)""",(access,))
                                 cursor.execute("""select count(*) from injury where p_id=(?)""",(access,))
                                 if cursor.fetchone()[0]!=0:
                                    cursor.execute("""delete from injury where p_id=(?)""",(access,))
                              else:
                                 print("Incorrect Patient id Patient does not exist")
                              print("\nPatient Deleted")
                              connection.commit()
                           elif r==0:
                              break
                    else:
                        print("Incorrect passoword. Please retry ")
                else:
                    print("Incorrect User ID. Please retry ")
            break
        elif e==2212:
            cursor.execute("""select * from doctor""")
            print(cursor.fetchall())
            cursor.execute("""select * from virus""")
            print(cursor.fetchall())
            cursor.execute("""select * from bacteria""")
            print(cursor.fetchall())
            cursor.execute("""select * from injury""")
            print(cursor.fetchall())
            break

        elif e==3:

            error =1
            while error==1:
              i1 = input("\nEnter your ID - ")
              p1= input("Enter your Password - ")
              cursor.execute("""select count(pd_id) from patient_details where pd_id=(?)""", (i1,))
              if cursor.fetchone()[0] == 1:
                  cursor.execute("""select count(password) from patient_details where password=?""", (p1,))
                  if cursor.fetchone()[0] == 1:
                      print("\nSign in successful!")
                      screen_clear()
                      error = 0
                      e = 0
                      r = 1
                      cursor.execute("""select pd_id,pdnamedfirst,pdnamedlast,pdconsultant,pdhissue,pddoa,pddob,pdage,pdcontact from patient_details where pd_id=(?)""", (i1,))
                      for row in cursor.fetchall():
                         print("ID -", row[0], "  Name -", row[1], row[2], "  consultant-", row[3], "\nhealth issue -", row[4]," Date of admission -", row[5],"\nDate of birth -",row[5],"\nage -",row[6],"\nContact number -",row[7])
                      while r!=0:
                         print("\n1. view the treatment report\n2. feedback\n0. Exit")
                         r = int(input())
                         if r==1:
                            access = input("\nEnter the  ID:- ")
                            cursor.execute("""select count(*) from patient_report where pr_id=(?)""", (access,))
                            if cursor.fetchone()[0] != 0:
                                cursor.execute("""select * from patient_report where pr_id=(?)""", (access,))
                                print("\nPatient Details - ")
                                for row in cursor.fetchall():
                                    print("Patient Id: ", row[0])
                                    print("Patient Name: ", row[1])
                                    print("DOB: ", row[2])
                                    print("age ", row[3])
                                    print("contact number: ", row[4])
                                    print("blood group: ", row[5])
                                    print("gender: ", row[6])
                                    print("date of admission: ", row[7])
                                    print("health issue: ", row[8])
                                    print("prescribed tests: ", row[9])
                                    print("tests done: ", row[10])
                                    print("medicines: ", row[11])
                                    print("is there a need to get admitted: ", row[12])
                                    print("No of days admitted: ", row[13])
                            else:
                                print("Incorrect passoword. Please retry ")
                         if r==2:
                            fid = int(input('\nEnter id - '))
                            fnn = input('Enter name - ')
                            frcity = input('Enter city - ')
                            fdof = input('Enter date of feedback - ')
                            feed = input('Enter your feedback - ')
                            cursor.execute("""insert into feedback values(?,?,?,?,?)""",(fid, fnn, frcity, fdof, feed))
                         if r==0:
                          break
              else:
                  print("Incorrect User ID. Please retry ")
            break
        elif e == 2212:
            cursor.execute("""select * from patient_details""")
            print(cursor.fetchall())
            cursor.execute("""select * from patient_report""")
            print(cursor.fetchall())
            cursor.execute("""select * from feedback""")
            print(cursor.fetchall())
            break

connection.commit()
connection.close()
print("")
def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

try:
    sqliteCon = sqlite3.connect('hospital.db')
    backupCon = sqlite3.connect('hospital_backup.db')
    with backupCon:
        sqliteCon.backup(backupCon, pages=1, progress=progress)
    print("backup successful")
except sqlite3.Error as error:
    print("Error while taking backup: ", error)
finally:
    if(backupCon):
        backupCon.close()
        sqliteCon.close()
