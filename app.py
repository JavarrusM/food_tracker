from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect(
        r"C:\Users\jdavo\OneDrive\Documents\GitHub\Food_Tracker\food_log.db"
    )
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if "db" not in g:
        g.db = connect_db()

    return g.db


@app.teardown_appcontext
def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/view")
def view():
    return render_template("day.html")


@app.route("/food", methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        form = request.form

        name = form['food-name'].title()
        carbohydrates = int(form['carbohydrates'])
        protein = int(form['protein'])
        fat = int(form['fat'])
        
        calories = protein * 4 + carbohydrates * 4 + fat * 9

        db = get_db()
        db.execute('insert into food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)', \
            [name, protein, carbohydrates, fat, calories])
        db.commit()

    return render_template("add_food.html")


if __name__ == "__main__":
    app.run()
