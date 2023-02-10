# Django-test_rpwin

# Django基础搭建
1. import Redis
2. create virtu envi and install Django
3. create django project：(django-admin startproject webapp)
4. powershell - cd webapp - to enter the correct folder and type: (python manage.py runserver)
5. create a single app（建立多个子应用进行模块分割） - cd webapp - enter: (python manage.app startapp Simontest)
6. 注册app到project中：找到根目录下settings.py，找到installed apps，手动添加app名字进去（这里是Simontest）；
7. 代码在models.py中写
8. 建立完models之后，要进行模型迁移：指令：a):python manage.py makemigrations; b):python manage.py migrate. (一定要完成第六步注册，才能迁移),迁移之后，数据表在sqlite3中。
9. 我安装了sqlite插件查看sql表，不知道还有什么其他方式通过VS查看。
10. VS code中ctrl+shift+P,选择sqlite - new query - 单击右键 use database - select * from Simontest_表名. (表格式可以在VS code左边路径list中最下面的sqlite explorer中看到)
11. 通过 python manage.py runserver进入网页，手动添加URL：/admin 测试链接

# Django 站点管理
1. 执行完上述第11步后，需要输入用户名和密码，此时，进入在powershell中输入：python manage.py createsuperuser （创建超级管理员）
2. 操作完后获取到创建的用户名和密码。pengp - abc12345，完后进行网页中登录操作
3. 进行数据库注册：进入Simontest中的admin.py,根据admin.py中我的注释改完，重启Django，刷新界面，即可看到PeopleInfo和Book Info两张表
4. 在网页中添加book info表，加入三国演义和西游记，此时显示为bookinfo_object，如果要更改显示为书名，需要进入models.py. 然后添加魔术方法__str__, 详细见models.py中注释
5. 定义试图函数：