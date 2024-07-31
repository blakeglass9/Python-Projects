import splite3

conn = splite3.connect('test.db')

with conn:
    our = conn.cursor()
    our.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT
        col_fname TEXT
        col_lname TEXT
        col_email TEXT
        )")
    conn.commit()
conn.close

conn = sqlite3.connect('test.db')

with conn:
    our = conn.cursor()
    our.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
                ('Sarah', 'Jones', 'sjones@gmail.com'))
    our.execute("INSERT INTO tbl_persons(col_fname, col_lnamem col_email) Values (?,?,?)", \
                ('Sally', 'May', 'sallymay@gmail.com'))
    our.execute("INSERT INTO tbl_persons(col_fname, col_lnamem col_email) Values (?,?,?)", \
                ('kevin', 'bacon', 'kbacon@rocketmail.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname, col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: ()\nLast Name: ()\nEmail: ()".format(item[0],item[1], i)
    print(msg)
        


