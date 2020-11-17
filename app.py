from flask import Flask, render_template, request, redirect
import pymysql

conn = pymysql.connect(host='localhost',port=3306,db='pyapp',user='root',passwd='java1004')
print(conn)

#print(conn)
app = Flask(__name__)

#삭제
@app.route("/del_msg", methods=['GET'])
def del_msg():
    msg_id = request.args.get('msg_id')
    cursor = conn.cursor()   
    cursor.execute('delete from msg where msg_id=%s', [msg_id])
    conn.commit()
    return redirect('/')
 
        
# 추가 폼
@app.route("/add_msg", methods=['GET','POST'])
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


@app.route("/msg_update", methods=['POST'])
def msg_update():
    msg_id = request.form('msg_id')
    msg_text = request.form('msg_text')
    cursor = conn.cursor()
    cursor.fetchone('update msg set msg_id=%s, msg_text=%s where msg_id=%s',[msg_id],[msg_text],[msg_id])
    conn.commit()
    return redirect('/')

#수정 if GET msgOne = cursor.fetchone()
#POST update set
@app.route("/msgOne", methods=['GET'])
def one_msg():
    msg_id = request.args.get('msg_id')
    cursor = conn.cursor()
    cursor.execute('select msg_id, msg_text from msg where msg_id=%s',[msg_id])
    conn.commit()
    return render_template('/msgOne.html', msg_id = msg_id)

# 1. msg 목록
@app.route('/',methods=['GET'])
def msg_list():
    cursor=conn.cursor()
    cursor.execute('select msg_id, msg_text from msg')
    msglist=cursor.fetchall()
    print(msglist)
    return render_template('msg_list.html', msglist = msglist)

app.run(host='127.0.0.1',port=80)