from flask import  render_template, request
from db import Pengeluaran, db, app
from repository import add_data, show_all_data
from predict import predict_pengeluaran

# db.create_all()

@app.route('/', methods=['POST','GET'])
def home():
    predict = 0
    validasi = True

    if request.method == 'POST':
        name = request.form['name']
        sex = request.form['sex']
        home = request.form['home']
        income = request.form['income']
        langganan = request.form['langganan']
        

        predict = predict_pengeluaran(income, langganan, sex, home)

        validasi = add_data(name, sex, home, langganan, income, predict[0])
        
        
        return render_template("homev2.html", predict = predict[0], is_big = predict[1], validasi=validasi)


    return render_template("homev2.html", predict = predict, validasi=validasi)


@app.route('/about')
def about():
    return render_template("about.html")




