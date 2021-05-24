#ORM 적용하기 위함

import os

BASE_DIR = os.path.dirname(__file__)  # 프로젝트의 루트 디렉토리  = myproject

SQLALCHEMY_DATABASE_URL = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # db 접속 주소
SQLALCHEMY_TRACK_MODIFICATIONS = False  # SQLAlchemy의 이벤트를 처리하는 옵션,  현재 필요하지 않으므로 false 설정


# pybo.db 라는 데이터베이스 파일을 프로젝트의 루트 디렉토리에 저장하는 과정이다