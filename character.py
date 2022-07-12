from flask import Flask, Response, request
import json
import status_code
import file_module
import db_connection
from flask_restx import Resource, Api, Namespace
from flasgger.utils import swag_from

Character = Namespace(
    name="Character",
    description="Character CRUD를 작성하기 위해 사용하는 API.",
)

'''
# 
# @form-data : file, user_id
#
'''
#@app.route('/character', methods=['POST'])
@Character.route('')
@Character.doc(responses={200: 'Success'})
@Character.doc(responses={500: 'Failed'})
class CharacterPost(Resource):
    #@Character.doc(params)
    #@Character.expect(params)
    def post():
        
        '''
        Upload file stream
        ---
        tags:
          -tools
        consumes: [
              "multipart/form-data"
            ]
        parameters:
          -in: formData
            name: file
            type: file 
            required: true
            description: upload a image file 
        '''
        try:
            db = db_connection.db_connection()
            f = request.files['file']
            # 1. 버킷에 파일 저장
            if file_module.single_upload(f, db, "upload_character"):
                
                # 1-1. 성공 message return
                return Response(
                    response=json.dumps(
                        {
                            "message":status_code.fileupload_01_success,
                        }
                    ),
                    status=200,
                    mimetype="application/json"
                )
            
            # 1. 버킷에 파일 저장 실패 시 진행
            else:
                # 1-1. 실패 message return
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