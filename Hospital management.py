import mysql.connector as mscon
db=input("Do you have database ? (y/n)=")
mydb=" "
mycursor=" "
if (db=='n'):
    mydb=mscon.connect(host='localhost',user="root",password="1111")
    mycursor=mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS hospital")
    mycursor.execute("create database hospital")
    mycursor=mydb.cursor()
    mydb = mscon.connect(host='localhost', user="root", password="1111",database="hospital")
    print("Database created successfully....")
    mycursor = mydb.cursor()
    mycursor.execute('''create table doctors (DOC_id int(5) primary key,
    DOC_Name char(20),department varchar(10),NOOFOPDDays  int(3))''')
    print("patient table created sucessfully...........")
    mycursor.execute('''create table patient (patient_id int(5) primary key,
    patient_Name char(20),patient_gender char(1),patient_Age int(3),BED_NO int(5))''')
    print("patient table created sucessfully...........")
    mycursor.execute('''create table covid_test (patient_id int(5), patient_Name char(20),Dofsample date null,
    result char(15))''')
    print("covid_test table created sucessfully.........")

    
if (db=='y'):
    mydb = mscon.connect(host='localhost', user="root", password="1111", database="hospital")
    print("Database is Open For Other Opertion")
while (True):
    mycursor = mydb.cursor()
    mycursor.execute("show tables")
    myresult = mycursor.fetchall()
    print("Tables in database .......")
    for x in myresult:
        print(x[0])
    mydb.commit()
    table=input("Enter name of table to perform task or enter (q) for quite =")
    
    if table == 'doctors':
        while (True):
            con = input("Do you want to continue in doctor table (y/n)==")
            if con == 'y':
                while (True):
                    print("1.Add Record")
                    print("2.Display All Record")
                    print("3.Search doctor by DOC_id")
                    print("4.Delete doctor by DOC_id")
                    print("5.Update doctor by DOC_id")
                    print("6.Exit")

                    choice = int(input("Enter Choice ="))
                    if (choice == 6):
                        break
                    elif (choice == 1):
                        print("Enter Detail of doctor.......")
                        i = input("Enter DOC_id of doctor     =")
                        n = input("Enter Name of doctor     =")
                        g = input("Enter Department of doctor    =")
                        a = input("Enter number of opd      =")
                        
                        sql = '''insert into doctors(DOC_id,DOC_Name,department,NOOFOPDDays)
                        values(%s,%s,%s,%s)'''
                        val = (i, n, g, a, )
                        mycursor = mydb.cursor()
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print(
                            "**************{    Record     save      }************")
                    elif (choice == 2):
                        mycursor = mydb.cursor()
                        mycursor.execute("select*from doctors")
                        myresult = mycursor.fetchall()
                        print(
                            "DOC_id \t DOC_Name \t department \t NOOFOPDDays ")
                        for x in myresult:
                            print(x[0], "\t", x[1], "         \t", x[2],"         \t",x[3])
                        mydb.commit()
                    elif (choice == 3):
                        i1 = input("Enter DOC_id of doctor whose record you are looking for = ")
                        mycursor = mydb.cursor()
                        mycursor.execute("select*from doctors where DOC_id =" + i1)
                        myresult = mycursor.fetchall()
                        t = mycursor.rowcount
                        if (t != 0):
                            print(
                            "DOC_id \t DOC_Name \t department \t NOOFOPDDays ")
                        for x in myresult:
                            print(x[0], "\t", x[1], "         \t", x[2],"         \t",x[3])
                           
                        if (t != 0):
                            print(
                                "*********{Record found successfully....}***************")
                        else:
                            print("********{Invalid DOC_id {No such DOCTOR with this  DOC_id}********* ")
                        mydb.commit()
                    elif (choice == 4):
                        i1 = input("Enter DOC_id of doctor whose record you want to delete = ")
                        mycursor = mydb.cursor()
                        mycursor.execute("delete from doctors where DOC_id =" + i1)
                        myresult = mycursor.fetchall()
                        t = mycursor.rowcount
                        if (t != 0):
                            print(
                                "*********{Record deleted successfully....}***************")
                        else:
                            print(
                                "*********{Invalid DOC_id {No such doctor with this  doc_id}********* ")
                    elif (choice == 5):
                        up = input(
                            "what things you want to update \n1.doctor Name(n),\n2.department(d),\n3.do of opd (p),\nENTER YOUR CHOICE =")
                        if (up == 'n'):
                            i1 = input("Enter DOC_id of Doctor whose name you want to update= ")
                            newrecord = input("Enter new name   =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE doctors SET DOC_name = ''' + '"' + newrecord + '"' + ''' WHERE DOC_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid DOC_id {No such doctor with this  DOC_id}***** ")
                        elif (up == 'd'):
                            i1 = input("Enter DOC_id of doctor whose department you want to update= ")
                            newrecord = input("Enter new department =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE doctors SET department = ''' + '"' + newrecord + '"' + ''' WHERE doc_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid DOC_id {No such doctor with this  DOC_id}***** ")
                        elif (up == 'P'):
                            i1 = input("Enter DOC_id of doctor whose number of opd days you want to update= ")
                            newrecord = input("Enter new number of opd days =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE doctors SET NOOFOPDDays = ''' + newrecord + ''' WHERE DOC_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid doc_id {No such doctor with this  doc_id}***** ")
                        
                        mydb.commit()
            else:
                break
    if table == 'patient':
        while (True):
            con = input("Do you want to continue in patient table (y/n)==")
            if con == 'y':
                while (True):
                    print("1.Add Record")
                    print("2.Display All Record")
                    print("3.Search doctor by DOC_id")
                    print("4.Delete doctor by DOC_id")
                    print("5.Update doctor by DOC_id")
                    print("6.Exit")

                    choice = int(input("Enter Choice ="))
                    if (choice == 6):
                        break
                    elif (choice == 1):
                        print("Enter Detail of patient.......")
                        i = input("Enter patient_id of patient     =")
                        n = input("Enter Name of patient     =")
                        g = input("Enter gender of patient    =")
                        a = input("Enter age  of patient      =")
                        b=input("Enter bed_no of patient      =")
                        
                        
                        sql = '''insert into patient()
                        values(%s,%s,%s,%s,%s)'''
                        val = (i, n, g, a,b )
                        mycursor = mydb.cursor()
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print(
                            "**************{    Record     save      }************")
                    elif (choice == 2):
                        mycursor = mydb.cursor()
                        mycursor.execute("select*from patient")
                        myresult = mycursor.fetchall()
                        print(
                            " patient_id \t  patient_Name \t  patient_gender \t  patient_Age \t BED_NO ")
                        for x in myresult:
                            print(x[0], "           \t", x[1], "              \t", x[2],"               \t",x[3],"\t",x[4])
                        mydb.commit()
                    elif (choice == 3):
                        i1 = input("Enter patient_id of patient whose record you are looking for = ")
                        mycursor = mydb.cursor()
                        mycursor.execute("select*from patient where patient_id =" + i1)
                        myresult = mycursor.fetchall()
                        t = mycursor.rowcount
                        if (t != 0):
                            print(
                            " patient_id \t  patient_Name \t  patient_gender \t  patient_Age \t BED_NO ")
                            for x in myresult:
                                print(x[0], "           \t", x[1], "              \t", x[2],"               \t",x[3]," \t",x[4])
                        if (t != 0):
                            print(
                                "*********{Record found successfully....}***************")
                        else:
                            print("********{Invalid patient_id {No such patient with this  patient_id}********* ")
                        mydb.commit()
                    elif (choice == 4):
                        i1 = input("Enter patient_id of patient whose record you want to delete = ")
                        mycursor = mydb.cursor()
                        mycursor.execute("delete from patient where patient_id =" + i1)
                        myresult = mycursor.fetchall()
                        t = mycursor.rowcount
                        if (t != 0):
                            print(
                                "*********{Record deleted successfully....}***************")
                        else:
                            print(
                                "*********{Invalid patient_id {No such patient with this  patient_id}********* ")
                    elif (choice == 5):
                        up = input(
                            "what things you want to update \n1.patient Name(n),\n2.patient gender(g),\n3.patient age (a),\n4.BED no(b),\nENTER YOUR CHOICE =")
                        if (up == 'n'):
                            i1 = input("Enter patient_id of patient whose name you want to update= ")
                            newrecord = input("Enter new name   =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE patient SET patient_Name = ''' + '"' + newrecord + '"' + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such patientwith this  patient_id}***** ")
                        elif (up == 'g'):
                            i1 = input("Enter patient_id of patient whose  gender you want to update= ")
                            newrecord = input("Enter new gender of patient =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE patient SET patient_gender = ''' + '"' + newrecord + '"' + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such patient with this  patient_id}***** ")
                        elif (up == 'a'):
                            i1 = input("Enter patient_id of patient whose age you want to update= ")
                            newrecord = input("Enter new age of patient =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE patient SET patient_Age = ''' + newrecord + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such patient with this  patient_id}***** ")
                        elif (up == 'b'):
                            i1 = input("Enter patient_id of patient whose BED_NO you want to update= ")
                            newrecord = input("Enter new BED_NO of patient =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE patient SET BED_NO = ''' + newrecord + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such patient with this  patient_id}***** ")
                        
                        mydb.commit()
            else:
                break
    if table == 'covid_test':
        while (True):
            con = input("Do you want to continue in covid_test table (y/n)==")
            if con == 'y':
                while (True):
                    print("1.Add Record")
                    print("2.Display All Record")
                    print("3.Search record  by patient_id")
                    print("4.Delete record by patient_id")
                    print("5.Update record by patient_id")
                    print("6.Exit")

                    choice = int(input("Enter Choice ="))
                    if (choice == 6):
                        break
                    elif (choice == 1):
                        print("Enter Details .......")
                        i = input("Enter patient_id of patient     =")
                        n = input("Enter Name of patient     =")
                        g = input("Enter Date of sample wheather sampe taken (yyyy/mm/dd)    =")
                        a = input("Enter result of test      =")
                        
                        sql = '''insert into covid_test(patient_id,patient_Name,Dofsample,result)
                        values(%s,%s,%s,%s)'''
                        val = (i, n, g, a, )
                        mycursor = mydb.cursor()
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print(
                            "**************{    Record     save      }************")
                    elif (choice == 2):
                        mycursor = mydb.cursor()
                        mycursor.execute("select*from covid_test")
                        myresult = mycursor.fetchall()
                        print(
                            " patient_id \t  patient_Name \t Dofsample \t result ")
                        for x in myresult:
                            print(x[0], "       \t", x[1], "     \t", x[2],"\t",x[3])
                        mydb.commit()
                    elif (choice == 3):
                        i1 = input("Enter patient_id of patient whose record you are looking for = ")
                        mycursor = mydb.cursor()
                        mycursor.execute("select*from covid_test where patient_id =" + i1)
                        myresult = mycursor.fetchall()
                        t = mycursor.rowcount
                        if (t != 0):
                            print(
                            " patient_id \t  patient_Name \t Dofsample \t result ")
                            for x in myresult:
                                print(x[0], "      \t", x[1], "     \t", x[2],"\t",x[3])
                            mydb.commit()
                           
                        if (t != 0):
                            print(
                                "*********{Record found successfully....}***************")
                        else:
                            print("********{Invalid patient_id {No such record with this  patient_id}********* ")
                        mydb.commit()
                    elif (choice == 4):
                        i1 = input("Enter patient_id of patient whose record you want to delete = ")
                        mycursor = mydb.cursor()
                        mycursor.execute("delete from covid_test where patient_id =" + i1)
                        myresult = mycursor.fetchall()
                        t = mycursor.rowcount
                        if (t != 0):
                            print(
                                "*********{Record deleted successfully....}***************")
                        else:
                            print(
                                "*********{Invalid patient_id {No such patient with this  patient_id}********* ")
                    elif (choice == 5):
                        up = input(
                            "what things you want to update \n1.patient Name(n),\n2.Date of sample(d),\n3.result (r),\nENTER YOUR CHOICE =")
                        if (up == 'n'):
                            i1 = input("Enter patient_id of patient whose name you want to update= ")
                            newrecord = input("Enter new name   =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE covid_test SET patient_Name = ''' + '"' + newrecord + '"' + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such record with this  patient_id}***** ")
                        elif (up == 'd'):
                            i1 = input("Enter patient_id of patient whose date of sample you want to update= ")
                            newrecord = input("Enter new date of sample  =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE covid_test SET Dofsample  = ''' + '"' + newrecord + '"' + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such record with this  patient_id}***** ")
                        elif (up == 'r'):
                            i1 = input("Enter patient_id of patient covid test result you want to update= ")
                            newrecord = input("Enter new result of covid test =")
                            mycursor = mydb.cursor()
                            sql = '''UPDATE covid_test SET result = ''' + newrecord + ''' WHERE patient_id =''' + i1
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            t = mycursor.rowcount
                            if (t != 0):
                                print(
                                    "***********{updated successfully.....}**********")
                            else:
                                print(
                                    "*******{Invalid patient_id {No such record with this  patient_id}***** ")
                        
                        mydb.commit()
            else:
                break
    if table== 'q':
        print("exit sucessfully")
        break

    