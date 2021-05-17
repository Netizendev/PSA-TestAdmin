import sqlite3
from topdf import print_to_pdf
import datetime

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
        adress = [namn, gata, postnr]
        adress[-1] = str(adress[-1]) + " " + postort
        print_to_pdf('ka',adress, datum)
        cur.execute("update psa_patient set kallelsedatum = date('now', '+180 days') where ssn in (Select ssn from psa_patient where ssn not in (select ssn_id from psa_provsvar))")
        con.commit()
        cur.execute("Update psa_patient set kallelsedatum = date('now', '+180 days') where ssn = (select ssn from (select psa_patient.ssn, psa_patient.kallelsedatum, psa_provsvar.result, psa_provsvar.done from psa_patient INNER JOIN \
        psa_provsvar on psa_provsvar.ssn_id = psa_patient.ssn where psa_patient.kallelsedatum = date('now') and psa_provsvar.done = 'False' group by psa_patient.ssn having count(psa_provsvar.ssn_id) <= 4))")
        con.commit()
        cur.execute("Update psa_patient set kallelsedatum = date('now', '+365 days') where ssn = (select ssn from (select psa_patient.ssn, psa_patient.kallelsedatum, psa_provsvar.result, psa_provsvar.done from psa_patient INNER JOIN \
        psa_provsvar on psa_provsvar.ssn_id = psa_patient.ssn where psa_patient.kallelsedatum = date('now') and psa_provsvar.done = 'False' group by psa_patient.ssn having count(psa_provsvar.ssn_id) > 4))")
        con.commit()

def kolla_provresultat():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('''select psa_patient.ssn, psa_patient.namn, psa_patient.mail, psa_provsvar.created, \
     psa_patient.gata, psa_patient.postort, psa_patient.postnr, psa_provsvar.result from psa_patient INNER JOIN \
          psa_provsvar on psa_patient.ssn = psa_provsvar.ssn_id where psa_provsvar.created = date('now')''')
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
        adress = [namn, gata, postnr]
        adress[-1] = str(adress[-1]) + " " + postort
        if result <= 0.1:
            print_to_pdf('ps',adress, created)
        else:
            print_to_pdf('psd',adress, created)
            cur.execute("Insert or replace into psa_hantera (ssn, name, result) values (?,?,?)", (ssn, namn, result))
            con.commit()
            cur.execute("Update psa_provsvar set done = 'True' where result > 0.1 and created = date('now')")
            con.commit()

def kolla_antal_provsvar():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    data = cur.execute("select namn, postort, postnr, gata from psa_patient where ssn in (SELECT ssn_id FROM psa_provsvar where done = 'False' group by ssn_id having count(ssn_id) = 10)")
    
    for x, y in enumerate(data):
        namn = y[0]
        postort = y[1]
        postnr = y[2]
        gata = y[3]
        adress = [namn, gata, postnr]
        adress[-1] = str(adress[-1]) + " " + postort
        dag = datetime.date.today()
        dag = str(dag.strftime('%d-%m-%y'))
        print_to_pdf('10',adress, dag)

    cur.execute("Update psa_provsvar set done = 'True' where ssn_id in (SELECT ssn_id FROM psa_provsvar where done = 'False' group by ssn_id having count(ssn_id) = 10)")
    con.commit()



# con = sqlite3.connect('db.sqlite3')
# cur = con.cursor()
# cur.execute('Insert or replace into psa_hantera (ssn, name, result) values (6810034931, "JUlia", 3)')
# con.commit()
