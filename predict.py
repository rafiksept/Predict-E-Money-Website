import pickle
import math
import warnings
warnings.filterwarnings("ignore")
from babel.numbers import format_currency

def predict_pengeluaran(uang_saku, langganan, sex, home):
    try:
        if sex == 'Laki-Laki':
            sex_boolean = 0
        elif sex == 'Perempuan':
            sex_boolean = 1

        if home == 'Yes':
            home_boolean = 0
        elif home == 'No':
            home_boolean = 1


        ln_uang = math.log(int(uang_saku), math.e)
        ln_langganan = math.log(int(langganan), math.e)


        with open('model_pengeluaran' , 'rb') as f:
            lr = pickle.load(f)


        hasil = lr.predict([[ln_uang, ln_langganan, sex_boolean, home_boolean]])
        result = math.e**hasil

        # name might vary with operating system, refer to the notes below
        if result > 418246.75324675324:
            is_big = True
        else:
            is_big = False
        uang = format_currency(result[0], "IDR", locale="id_ID")

        print("[+] Predicting data Success [+]")
        return [uang, is_big]

    except:
        print("[-] Predicting data Failed [-]")
        return [0,0]


