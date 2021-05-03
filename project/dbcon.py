import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
till_vc_list = []
data = cur.execute("SELECT ssn FROM psa_provsvar where done = 'True' group by ssn having count(ssn) = 2")
data = data.fetchall()

for row in data:
    till_vc_list.append(row)
    print(row)
    cur.execute("update psa_provsvar set done = 'False' where ssn = ?", row)

con.commit()