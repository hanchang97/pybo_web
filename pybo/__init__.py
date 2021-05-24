from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import config


# app = Flask(__name__)  # 플라스크 애플리케이션을 생성 / __name__ 이라는 변수에 모듈명이 담긴다 / 이 파일이 실행되면 pybo.py라는 모듈이 실행
# # __name__ 변수에는 'pybo'라는 문자열 담긴다
#
# # @app.route 는 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
# @app.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'

db = SQLAlchemy()
migrate = Migrate()

def create_app():   #create_app은 플라스크 내부엣 정의된 함수명!! /
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)  # config 파일에 작성한 항목을 app.config 환경변수로 부르기 위함

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)  # db 객체 밖에서 생성하고 create_app 내부에서 초기화 / 다른 모듈에서 불러오기 가능하게 하려고

    #@app.route('/')         #@app.route와 같은 애너테이션으로 매핑되는 함수를 라우트 함수라고 한다
    #def hello_pybo():
    #    return 'Hello, Pybo!!'
    #return app

    # 블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)  #블루프린트 객체 bp 등록 / main_view.py 파일의 블루프린트 객체 bp

    main_views.initTest()

    return app


# 새로운 URL 생길 때 라우트 함수를 create_app 함수 안에 계속 추가해야 하는 불편함 존재
# 블루프린트 클래스를 사용하여 해결해본다
#