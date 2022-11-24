from flask import Flask, render_template

import sqlite3

import click
from flask import current_app, g

app = Flask(__name__)


def connect_db():
    sql = sqlite3.connect(
        r"C:\Users\jdavo\OneDrive\Documents\GitHub\Food_Tracker\food_log.db"
    )
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, "db"):
        g.db = connect_db()
    return g.db


def get_db():
    if "db" not in g:
        g.db = connect_db

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


@app.route("/food")
def food():
    return render_template("add_food.html")


if __name__ == "__main__":
    app.run(debug=True)
