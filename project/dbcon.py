import sqlite3

def kolla_antal_provsvar():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()

    # cur.execute("update psa_provsvar set done = 'False' where id = 26")
    data = cur.execute("SELECT ssn FROM psa_provsvar where done = 'False' group by ssn having count(ssn) = 10")
    data = data.fetchall()

    print("\nDessa personer skall ha fortsatt provtagning via vårdcentral: \n")

    for row in data:
        print(row)
        cur.execute("update psa_provsvar set done = 'True' where ssn = ?", row)
    print("")
    con.commit()

def main():
    kolla_antal_provsvar()
    
if __name__ == "__main__":
    main()
