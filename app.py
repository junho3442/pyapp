from flask import Flask, render_template, request, redirect
import pymysql

conn = pymysql.connect(host='localhost',port=3306,db='pyapp',user='root',passwd='java1004')
print(conn)

#print(conn)
app = Flask(__name__)

#수정 if GET msgOne = cursor.fetchone()
#POST update set

#삭제
@app.route("/del_msg", method=['GET'])
def del_msg():
    msg_id = request.args.get('msg_id')
    cursor = conn.cursor()   
    cursor.execute('delete from msg where msg_id=%s', [msg_id])
    conn.commit()
    return redirect('/')
 
        
# 추가 폼
@app.route("/add_msg", method=['GET','POST'])
def add_msg():
    if request.method == 'GET':
        return render_template('add_msg.html')
    elif request.method == 'POST':
        msg_text = request.form['msg_text']
        #db 입력
        cursor = conn.cursor()
        cursor.execute('insert into msg(msg_text) values(%s)',[msg_text])
        conn.commit()
        return redirect('/')


# 1. msg 목록
@app.route('/',methods=['GET'])
def msg_list():
    cursor=conn.cursor()
    cursor.execute('select msg_id, msg_text from msg')
    msglist=cursor.fetchall()
    print(msglist)
    return render_template('msg_list',msglist = msglist)

app.run(host='127.0.0.1',port=80)