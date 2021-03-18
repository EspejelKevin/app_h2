from flask import Flask, redirect, url_for, render_template, request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'mysecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'km05010002'
app.config['MYSQL_DB'] = 'dietas'
mysql = MySQL(app)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/adidas', methods=['POST', 'GET'])
def adidas():
    if request.method == 'POST':
        username = request.form['username']
        password = int(request.form['password'])
    
        if username != "kevin" or password != 123:
            flash("Username or password incorrect")
            return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM alimentos')
    data = cursor.fetchall()
            
    return render_template('mainpage.html', diets = data)

@app.route('/registration_form', methods = ['POST'])
def form():
    if request.method == 'POST':
        name_foods = request.form['food-name']
        protein = request.form['protein']
        carbs = request.form['carbs']
        units = request.form['units']
        name_drinks = request.form['drink-name']
        amount_drink = request.form['quantity-drink']
        
        for name_food in name_foods:
            if name_food == '1':
                food = "Eggs"
            elif name_food == '2':
                food = "Fruits"
            elif name_food == '3':
                food = "Fish"
            elif name_food == '4':
                food = "Chicken"
            elif name_food == '5':
                food = "Yoghurt"
            elif name_food == '6':
                food = "Salad"
            elif name_food == '7':
                food = "Turkey toast"
        
        for name_drink in name_drinks:
            if name_drink == '1':
                drink = "Water"
            elif name_drink == '2':
                drink = "Fruit water"
            elif name_drink == '3':
                drink = "Ginger beer"
            elif name_drink == '4':
                drink = "Chia water"
            elif name_drink == '5':
                drink = "Fruit juice"
            elif name_drink == '6':
                drink = "Milk"
            
            
        datos = food, protein, carbs, units, drink, amount_drink

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO alimentos (NOMBRE, PROTEINA, CARBS, UNIDADES, BEBIDA, CANTIDAD_BEBIDA) VALUES (%s, %s, %s, %s, %s, %s)", datos)
        mysql.connection.commit()

        flash("¡Food successfully saved!")
        return redirect(url_for('adidas'))

@app.route('/edit_record/<int:id>')
def get_record(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f'SELECT * FROM alimentos WHERE ID = {id}')
    data = cursor.fetchall()

    return render_template('updatediet.html', diet = data[0])

@app.route('/update_record/<int:id>', methods = ['POST'])
def update_record(id):
    if request.method == 'POST':
        name_foods = request.form['food-name']
        protein = request.form['protein']
        carbs = request.form['carbs']
        units = request.form['units']
        name_drinks = request.form['drink-name']
        amount_drink = request.form['quantity-drink']
        
        for name_food in name_foods:
            if name_food == '1':
                food = "Eggs"
            elif name_food == '2':
                food = "Fruits"
            elif name_food == '3':
                food = "Fish"
            elif name_food == '4':
                food = "Chicken"
            elif name_food == '5':
                food = "Yoghurt"
            elif name_food == '6':
                food = "Salad"
            elif name_food == '7':
                food = "Turkey toast"
        
        for name_drink in name_drinks:
            if name_drink == '1':
                drink = "Water"
            elif name_drink == '2':
                drink = "Fruit water"
            elif name_drink == '3':
                drink = "Ginger beer"
            elif name_drink == '4':
                drink = "Chia water"
            elif name_drink == '5':
                drink = "Fruit juice"
            elif name_drink == '6':
                drink = "Milk"

        data = food, protein, carbs, units, drink, amount_drink, id

        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE alimentos
            SET NOMBRE = %s, PROTEINA = %s, CARBS = %s, UNIDADES = %s, BEBIDA = %s, CANTIDAD_BEBIDA = %s
            WHERE ID = %s
        """, data)

        mysql.connection.commit()

        flash("¡Food succesfully updated!")
        return redirect(url_for('adidas'))

@app.route('/delete_record/<int:id>')
def delete_record(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f'DELETE FROM alimentos WHERE ID = {id}')
    mysql.connection.commit()
    
    flash("¡Food successfully removed!")
    return redirect(url_for('adidas'))