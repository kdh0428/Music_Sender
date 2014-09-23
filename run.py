# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask,url_for,redirect,request,g,session,render_template,jsonify,send_file,flash,make_response
from functools import wraps
from datetime import datetime,timedelta
import md5,random,string,os
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'develop'
FILE_PATH = '/home/kimdonghyeon/Music/NaverMusic/'

@app.route('/music')
def music_send():
    return send_file(sys.argv[1])

@app.route('/music/<filename>')
def music_download(filename):
    if '..' in filename[0:2]:
        return 'rejected'
    return send_file(FILE_PATH+filename)


@app.route('/music_down/<filename>')
def music_down(filename):
    if '.' in filename[0:2]:
        'rejected'
    return send_file(FILE_PATH+filename,as_attachment=True)
@app.route('/')
def music_html():
    return render_template('send.html',musics = os.listdir(FILE_PATH))

if __name__ == '__main__':
    app.debug=False
    app.run('0.0.0.0',6648)

    
