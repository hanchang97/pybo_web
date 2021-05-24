import shutil

from flask import Flask, Blueprint, request, render_template, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import json
import boto3

AWS_ACCESS_KEY_ID ="AKIAZDET2MTHTCIVUF2R"
AWS_SECRET_ACCESS_KEY = "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"
AWS_DEFAULT_REGION = "ap-northeast-2"

client_s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         region_name=AWS_DEFAULT_REGION)

response = client_s3.list_buckets() # bucket 목록
print(response)



import os
from flask_cors import CORS

bp = Blueprint('main', __name__, url_prefix='/')   # 블루프린트 객체 생성


def initTest():
    a = 'asdf'
    return a

# s3에 이미지 업로드 test
def S3Test():



    return str('s3 upload!')


#  s3에서 이미지 다운로드
def S3Download():

    return str('s3 download!')

@bp.route('/hello', methods=['GET'])
def hello_pybo():
    return 'Hello, Pybo!!!'

@bp.route('/')
def index():
    return 'Pybo index'

@bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'

@bp.route('/image', methods=['POST'])
def getImage():

    f = request.files['file']
    print('hello')
    filename = secure_filename(f.filename)
    f.save(os.path.join("C:/testImageGet", filename))  # 현재 지정해둔 경로에 받은 이미지 파일 저장
    #f.save(filename)

    # with open(f, 'rb') as ff:
    #     client_s3.upload_fileobj(ff, 'capstonefaceimg', 's3uploadtest.jpg')

    # client_s3.upload_fileobj(
    #     f,
    #     "capstonefaceimg",
    #     ExtraArgs={
    #         "ContentType": f.content_type
    #     }
    # )

    #client_s3.upload_file(Bucket='capstoneimg', Filename=filename, Key = filename)


    return str(f)


# Train 위해서 이미지 받기
# 넘겨받은 그룹, 유저 아이디 값에 따라 폴더 생성해서 저장해보기
@bp.route('/image2', methods=['POST'])
def getImage_File():

    f = request.files['file']  # 트레인용 이미지
    print('hello2')
    filename = secure_filename(f.filename)

    # 그룹, 유저 아이디 값 받기 / form-data 형식
    userId = request.form['userID']
    groupId = request.form['groupID']

    #groupId  = 1  # 어떤 그룹인지
    #userId = 1  # 어떤 유저인지

    # 저장할 경로
    tryPath = "C:/testImageGet/group" + str(groupId) + "/user" + str(userId)

    # 이미 존재하는 경로인지 검사
    try:
        if not os.path.exists(tryPath):
            os.makedirs(tryPath)   # 새로운 경로라면 경로 값에 맞게 새로 생성하고 해당 이미지 저장
    except OSError:
        print("Error : Cannot create directory")  # 이미 존재하는 경로이면 예외 발생 하므로 다음으로 넘어가게 하기 위해 처리

    # os.makedirs("C:/testImageGet/group" + str(groupId) + "/user" + str(userId)) # 지정 경로에 폴더 생성

    #f.save(os.path.join("C:/testImageGet/group" + str(groupId) + '/user' + str(userId), filename))
    f.save(os.path.join("C:/testImageGet/group" + str(groupId) + '/user' + str(userId), "user" + str(userId) + ".jpg"))
    # 생성한 폴더 경로에 받은 이미지 파일 저장

    # groupPath = "C:/testImageGet/group" + str(groupId)

    # 파일명 변경하기
    # os.rename(groupPath + "/" + "user" + str(userId) + "/" + filename,
    #           groupPath + "/" + "user" + str(userId) + "/" + "user" + str(userId) + "testImage.jpg")  # 원하는 파일명으로 변경된다

    return str(filename)


# json 형태로 분석 값 보내주기 test  /  분석 결과 형태에 맞게 보내주면 될듯 - 세영님 분석 결과보고 맞춰보기
# 결과를 언제 보내줘야 하는지??
@bp.route('/testResult', methods=['GET', 'POST'])
def getTestResult():

    # 경로(폴더)와 파일 한번에 지우는 것은 shutil.rmtree(path) 사용해보기
    # 디렉토리 삭제 테스트
    # shutil.rmtree("C:/testImageGet/group1")  # 지정된 디렉토리 및 하위 요소들 포함해서 모두 삭제된다

    # 해당 테스트 이미지의 분석 결과 + 해당 이미지 유저 정보 + 그룹 정보를 json 형태로 반환한다

    return jsonify({
                    "groupName" : "Capstone Design",
                    "userId" : 2,
                    "sleep" : True
                                    })



# 프론트에서 넘어오는 json 형식에 맞춰보기
@bp.route('/image3', methods=['POST'])
def imageTest3():
    req_data = request.json

    for i in req_data['contacts']:
        userId = req_data['contacts'][i]['id']
        print(str(userId))


    return str(req_data['contacts'][0]['id'])



@bp.route('/trainImage', methods=['GET', 'POST'])
def getTrainImage():
    requestData = request.json

    return requestData






# 테스트 이미지 보내고 저장 후 분석 완료되면 그 때 해당 이미지 삭제하기??


# 10명 각각 3장씩 총 30장이 디렉토리 형태로 바로 오는 것인지???


# 이미지 파일은 base64로 인코딩된 상태를
# base64 풀어서 저장하기

