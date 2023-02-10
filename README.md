# Django-test_rpwin

1. import Redis
2. create virtu envi and install Django
3. create django project：(django-admin startproject webapp)
4. powershell - cd webapp - to enter the correct folder and type: (python manage.py runserver)
5. create a single app - cd webapp - enter: (python manage.app startapp Simontest)
6. 注册app到project中：找到根目录下settings.py，找到installed apps，手动添加app名字进去；
7. 代码在models.py中写
8. 建立玩models之后，要进行模型迁移：指令：a):python manage.py makemigrations; b):python manage.py migrate. (一定要完成第六步注册，才能迁移)
9. 