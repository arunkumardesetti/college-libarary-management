import MySQLdb as db
def getconnection():
    global conn
    conn = db.connect("localhost","root","","project")
    conn.autocommit(True)

def book_registration(title,subject,author):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("INSERT INTO books(title,subject,author,status) values('%s','%s','%s','available')"%(title,subject,author))
        if c.rowcount > 0:
            return 1
        else:
            return 0
    except Exception,e:
        print e
    finally:
        conn.close()

def emp_registration(name,department,doj,salary,id,password):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM login where lid='%s'"%(id))
        rcount = c.fetchall()
        for i in rcount:
            if i[0]== 0:
                c.execute("INSERT INTO login values('%s','%s','%s','employee')"%(id,password,name))
                c.execute("INSERT INTO emp_detail values('%s','%s','%s','%s','%s')"%(id,name,department,doj,salary))
                if c.rowcount > 0:
                    return 1
                else:
                    return 2
            else:
                return 3
    except Exception,e:
        print e
    finally:
        conn.close()


def stu_registration(name, department, sem, batch, roll, password):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM login where lid='%s'"%(roll))
        rcount = c.fetchall()
        for i in rcount:
            if i[0]== 0:
                c.execute("INSERT INTO login values('%s','%s','%s','student')"%(roll,password,name))
                c.execute("INSERT INTO stu_detail values('%s','%s','%s','%s','%s')"%(roll,name,department,sem,batch))
                if c.rowcount > 0:
                    return 1
                else:
                    return 2
            else:
                return 3
    except Exception,e:
        print e
    finally:
        conn.close()



def login(id,password):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM login where lid='%s' and password='%s'"%(id,password))
        result = c.fetchall()
        for x in result:
            return x[0]
    except Exception,e:
        print e
    finally:
        conn.close()



def delete_book(id):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM books where bid='%s'"%(id))
        rcount = c.fetchall()
        for i in rcount:
            if i[0] == 1:
                c.execute("DELETE FROM books WHERE bid='%s'"%(id))
                if c.rowcount > 0:
                    return 1
                else:
                    return 0
            elif i[0] == 0:
                return 2
    except Exception,e:
        print e
    finally:
        conn.close()

def view_all_books():
    getconnection()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM books")
        rows = c.fetchall()
        return rows
    except Exception, e:
        print e
    finally:
        conn.close()

def search_book(sub):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM books where subject='%s'"%(sub))
        rows = c.fetchall()
        if len(rows)==0:
            return 0
        else:
            return rows
    except Exception, e:
        print e
    finally:
        conn.close()


def issue(id,roll):
    getconnection()
    try:
        c = conn.cursor()
        d = conn.cursor()
        e = conn.cursor()
        c.execute("SELECT COUNT(*) FROM books WHERE bid='%s'"%(id))
        rcount = c.fetchall()
        d.execute("SELECT COUNT(*) FROM stu_detail WHERE rollno='%s'"%(roll))
        rcount1 = d.fetchall()
        e.execute("SELECT status from books where bid='%s'"%(id))
        rcount2 = e.fetchall()
        for i in rcount:
            if i[0] == 0:
                return 2
        for i in rcount1:
            if i[0] == 0:
                return 3
        for i in rcount2:
            if i[0] == "unavailable":
                return 4
        else:
            c.execute("INSERT INTO issue_detail values('%s','%s')"%(id,roll))
            c.execute("UPDATE books SET status='unavailable' WHERE bid='%s'"%(id))
            if c.rowcount > 0:
                return 1
    except Exception,e:
        print e
    finally:
        conn.close()


def return_book(id,roll):
    getconnection()
    try:
        c = conn.cursor()
        c.execute("DELETE FROM issue_detail WHERE bid='%s' and issue_to='%s'"%(id,roll))
        if c.rowcount > 0:
            c.execute("UPDATE books SET status='available' WHERE bid='%s'" % (id))
            return 1
        else:
            return 0
    except Exception,e:
        print e
    finally:
        conn.close()
