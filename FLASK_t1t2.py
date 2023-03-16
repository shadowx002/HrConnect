from flask import Flask, render_template
from utils.csv_operations import CSVProcessor
from task_one import task_1
from task_two import task_2

app = Flask(__name__)
t2_data = task_1()
t2_data = task_2()


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/task_one")
def t1():
    return render_template("task_one.html", data=task_1())


@app.route("/task_two")
def t2():
    return render_template("task_two.html", data=t2_data)
