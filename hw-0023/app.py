import sqlite3
import datetime
from flask import Flask, request, render_template


conn = sqlite3.connect('word_test.db')
cursor = conn.cursor()
try:
    cursor.execute(
        'create table message (id integer primary key,name varchar(64),mail varchar(64),word text,time_at datetime)')
except Exception as e:
    print("数据表已存在")

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    cursor.execute('select * from message')
    mess = cursor.fetchall()
    return render_template('form.html',mess=mess)


@app.route('/update', methods=['POST'])
def update():
    name = request.form['name']
    mail = request.form['mail']
    word = request.form['word']
    # 生成当前时间
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M:%S')

    if(name and mail and word):
        cursor.execute('insert into message (name,mail,word,time_at) values(?,?,?,?)', [
                       name, mail, word, now])

        conn.commit()

        return 'success'
    return "不能为空"


@app.route('/view', methods=["GET"])
def view():
    cursor.execute('select * from message')
    mess = cursor.fetchall()
    return render_template('view.html',mess=mess)


if __name__ == '__main__':
    app.run()
