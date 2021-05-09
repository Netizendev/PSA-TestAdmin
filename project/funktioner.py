import sqlite3
from topdf import print_to_pdf

def kallelsedatum_skickabrev():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('''select namn, gata, postnr, postort, kallelsedatum from psa_patient where kallelsedatum = date('now')''')
    dagens_utskick = cur.fetchall()

    for x, y in enumerate(dagens_utskick):
        namn = y[0]
        gata = y[1]
        postnr = y[2]
        postort = y[3]
        datum = y[4]
        adress = [namn, gata, postnr, postort]
        print_to_pdf('ka',adress, datum)
        cur.execute("update psa_patient set kallelsedatum = date('now', '+180 days') where ssn in (Select ssn from psa_patient where ssn not in (select ssn from psa_provsvar))")
        con.commit()
        cur.execute("Update psa_patient set kallelsedatum = date('now', '+180 days') where ssn = (select ssn from (select psa_patient.ssn, psa_patient.kallelsedatum, psa_provsvar.result, psa_provsvar.done from psa_patient INNER JOIN \
        psa_provsvar on psa_provsvar.ssn = psa_patient.ssn where psa_patient.kallelsedatum = date('now') and psa_provsvar.done = 'False' group by psa_patient.ssn having count(psa_provsvar.ssn) <= 4))")
        con.commit()
        cur.execute("Update psa_patient set kallelsedatum = date('now', '+365 days') where ssn = (select ssn from (select psa_patient.ssn, psa_patient.kallelsedatum, psa_provsvar.result, psa_provsvar.done from psa_patient INNER JOIN \
        psa_provsvar on psa_provsvar.ssn = psa_patient.ssn where psa_patient.kallelsedatum = date('now') and psa_provsvar.done = 'False' group by psa_patient.ssn having count(psa_provsvar.ssn) > 4))")
        con.commit()

def kolla_provresultat():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('''select psa_patient.ssn, psa_patient.namn, psa_patient.mail, psa_provsvar.created, \
     psa_patient.gata, psa_patient.postort, psa_patient.postnr, psa_provsvar.result from psa_patient INNER JOIN \
          psa_provsvar on psa_patient.ssn = psa_provsvar.ssn where psa_provsvar.created = date('now')''')
    provsvar_brev = cur.fetchall()

    for x, y in enumerate(provsvar_brev):
        ssn = y[0]
        namn = y[1]
        mail = y[2]
        created = y[3]
        gata = y[4]
        postort = y[5]
        postnr = y[6]
        result = y[7]
        adress = [namn, gata, postnr, postort]
        if result <= 0.1:
            print_to_pdf('ps',adress, created)
        else:
            print_to_pdf('psd',adress, datum)
            cur.execute("Insert or replace into psa_hantera (ssn, name, result) values (?,?,?)", (ssn, namn, result))
            con.commit()
            cur.execute("Update psa_provsvar set done = 'True' where result > 0.1 and created = date('now')")
            con.commit()


