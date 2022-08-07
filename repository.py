from db import db, Pengeluaran

def show_all_data():
    return Pengeluaran.query.all()

def add_data(name, sex, home, langganan, income, pengeluaran):
    try:
        data = Pengeluaran(name = name, sex = sex, home=home, langganan=int(langganan), income = int(income), pengeluaran = pengeluaran)
        db.session.add(data)
        db.session.commit()
        print("[+] Processing Data Success [+]")
        return True
    except:
        print("[-] Processing Data Failed [-]")
        return False






