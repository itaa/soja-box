from flask import request, Flask, jsonify
import time
import os
import soja_md5 as sj
import soja_find as find
import shutil
import soja_zip


# 上传请求参数
upload_request_param_list = ['file_type', 'sign', 'timestamp', 'file_name']
# 不允许上传的文件类型
NOT_ALLOW_FILE_TYPES = ['*.html', '*.htm', '*.js', '*.css', '*.php', '*.py']
basedir = '/Users/itaa/Desktop/'
local_short_file_name = '.zip'
sign_salt = 'sign_salt'



app = Flask(__name__)
@app.route('/upload_zip', methods=['POST'])
def upload_zip():
    # param_dict：存放请求参数
    param_dict = dict.fromkeys(upload_request_param_list, None)
    start_time = time.time()

    file_size = request.content_length

    try:
        # 以表单形式发送数据
        parameter = request.form
        for param in upload_request_param_list:
            param_dict[param] = parameter.get(param)
    except:
        raise Exception


