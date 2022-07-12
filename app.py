from flask import Flask, Response, request
import json
import status_code
import file_module
import db_connection
from character import Character
from flask_restx import Resource, Api, Namespace, fields
app = Flask(__name__)

#api = Api(app)
api = Api(
    app,
    version='0.1',
    title="Silicon Project's API Server",
    description="PRP!",
    terms_url="/",
    contact="vivian0304@naver.com",
    license="MIT"
)

parser = api.parser()
parser.add_argument('param', type=int, help='Some param', location='form')
parser.add_argument('in_files', type=FileStorage, location='files')

api.add_namespace(Character, '/character')



# DB 연결


# 스키마 생성
# db_connection.init_collection(db)s

todos = {}
count = 1

Todo = Namespace('Todo')

@Todo.route('')
class TodoPost(Resource):
    def post(self):
        global count
        global todos
        
        idx = count
        count += 1
        todos[idx] = request.json.get('data')
        
        return {
            'todo_id': idx,
            'data': todos[idx]
        }
    def get(self):

        
        return {
            'todo_id': 1,

        }

api.add_namespace(Todo, '/')

'''
# 
# @form-data : file, user_id
#
'''
@app.route('/oringin-video', methods=['POST'])
def oringinVideo():
    try:
        if file_module.single_upload(db, "video_origin"):
    
            # 5-4. 성공 message return
            return Response(
                response=json.dumps(
                    {
                        "message":status_code.fileupload_01_success,
                    }
                ),
                status=200,
                mimetype="application/json"
            )
        
        # 5. 버킷에 파일 저장 실패 시 진행
        else:
            # 5-1. 실패 message return
            return Response(
                response=json.dumps(
                    {
                        "message":status_code.filedownload_02_fail,
                    }
                ),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        
            print("******************")
            print(ex)
            print("******************")

'''
# 
# @form-data : file, user_id
#
'''
@app.route('/modification-video', methods=['POST'])
def modificationVideo():
    try:
        if file_module.single_upload(db, "video_modification"):
    
            # 5-4. 성공 message return
            return Response(
                response=json.dumps(
                    {
                        "message":status_code.fileupload_01_success,
                    }
                ),
                status=200,
                mimetype="application/json"
            )
        
        # 5. 버킷에 파일 저장 실패 시 진행
        else:
            # 5-1. 실패 message return
            return Response(
                response=json.dumps(
                    {
                        "message":status_code.filedownload_02_fail,
                    }
                ),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        
            print("******************")
            print(ex)
            print("******************")

"""
* 단일 파일 다운로드
"""
# @app.route('/filedownload', methods=['GET'])
# def filedownload():
    # s3 = s3_connection()
    #ret =s3_get_object(s3, AWS_S3_BUCKET_NAME, "upload_character/KakaoTalk_20220629_172754042.jpg", "12ssss.png")
    # if file_module.download(s3, db, "upload_character") :
    #     return 'file download successfully'
    # else:
    #     return 'file download fail'


if __name__ == "__main__":
    app.run(port=80, debug=True)