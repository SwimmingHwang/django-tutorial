

## Django project template

1. python startapp app_name
1. INSTALLED_APPS에 앱 추가
1. python manage.py migrate
    - DB migrate 실행
    - django default db 생성
1. 필요한 model 작성
1. python manage.py makemigrations polls
    - 모델 변경 사항을 migrate 할 준비
1. python manage.py migrate
    - 추가한 모델과 관련된 테이블 생성
    
    
---
1.  관리자 생성
```
$ python manage.py createsuperuser
```