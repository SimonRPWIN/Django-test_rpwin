# Redis使用

1.	安装包解压，保存名字为Redis在C盘.
2.	Cmd运行redis-server.exe redis.windows.conf
3.	另一个cmd运行redis-cli.exe -h 127.0.0.1 -p 6379

# 基本redis操作指令：
1.	设置变量 set
2.	查看获取变量get
3.	设置过期时间：setex +名字 +时间 +值； 例如：setex img 100 abcd
4.	查看还有多久有效期：ttl +变量名，例如：ttl img
5.	查所有数据：keys *
6.	同时设置多个变量：mset 名字 值 名字 值，例如：mset a 1 b 2
7.	同时获取多个变量：mget
8.	手动给一个变量设置过期时间： expire 名字 时间
9.	查看数据格式：type 名字
10.	删除变量 del 名字
11.	哈希数值设置：hset person name simon
                 Hset person age 30
12.	获取哈希变量值：hget，例如：hget person age （需要两个key都写进去）
13.	查哈希所有的key：hkeys person
14.	查哈希所有的值：hvals person
15.	哈希删除：hdel person
16.	更改哈希值：hset person age 20
17.	列表变量赋值：lpush +名字（从左往右添加）
18.	列表变量查看：lrange +名字 0 -1
19.	同理，从右边插入数据到列表：rpush
20.	列表删除含有相同数值的变量：lrem 名字 + count（正数从左+几个；0全删）+ 删除的数字
21.	Set可以增删 不能修改，增加集合（set）类型变量：sadd + 名字 + 成员
     例如：sadd class China
22.	查看set集合数据：smembers class
23.	删除set成员：srem class China
24.	有序集合（zset）添加数据：zdd +集合名字 +score（权重，用于排序）+ 值
25.	获取zset数据：zrange + 集合名字 + start（0）+end（-1）
26.	移除数据：zrem + 集合名字 + 值


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
2. 操作完后获取到创建的用户名和密码。rpwin - abc12345，完后进行网页中登录操作
3. 进行数据库注册：进入Simontest中的admin.py,根据admin.py中我的注释改完，重启Django，刷新界面，即可看到PeopleInfo和Book Info两张表
4. 在网页中添加book info表，加入三国演义和西游记，此时显示为bookinfo_object，如果要更改显示为书名，需要进入models.py. 然后添加魔术方法__str__, 详细见models.py中注释
5. 定义试图函数：进入Simontest - views.py，此时类似于Flask中定义@app.route的各种URL路径，具体格式见views.py。接收和返回（request和response）
6. 进入project中的urls.py，添加导入simontest app中的views中的路径函数index。这里必须导包和添加路径path。
7. 当子应用数目太多时，可以在子应用文件夹中手动新建一个py文件，取名为urls.py。把工程project文件夹中的urls.py中路径移到子应用urls文件中。同样需要导包path和index。同时，要在工程文件夹的urls中添加子应用urls路径(需要导包include)。此时，url的路径变成工程中url+子应用url。例如：http://127.0.0.1:8000/simontest/index/。！！！此步骤相当于把所有的url路径根据不同的app进行分组，然后一起添加到工程的urls文件中。
tips：如果不需要/simontest显示，则把path设置为空字符''。

# Django 网页模板创建和渲染
1. templates文件夹必须在最外层中建立。（这里为最外层的webapp）templates 中加入相应的url路径的html
2. 创建完html之后，回到工程文件夹中的settings.py，找到templates列表变量。找到DIRS列表进行templates添加。'DIRS': [BASE_DIR / 'templates']
3. 修改对应的simontest小程序中的views index函数中的返回值。改成return render，和FLASK类似。return render(request, 'Simontest/index.html')
tips: 注意这里的render的第二个参数是html的名字，不是路径。其中第三个参数context类似于flask中的变量，传入html后可以通过{{}}调用。
4. 图片：新建static文件夹，在工程setting中添加staticfiles_DIR,即可访问

# 将数据库从sqlite改成mysql
1. 进入settings的database列表.engine中sqlite改成mysql,再添加host,port,user,password,schema name etc
2. 改好后,系统报错: 此时需要再powershell中手动添加pip install mysqlclient.
3. 需要在虚拟环境下安装,同时安装pip install pymysql
4. 此时必须重新进行数据迁移 migrate: python manage.py migrate,此时将丢失之前创建的书名和人名. 这之前在mysql中需要有这个名字的库

# Django操作
1. 根据mysql的表,更改子应用的models中的类,然后migrate,可以看到mysql中添加完成相应的database结构
2. class Meta用于改mysql中的表名
3. 建立mysql中数据库的数据,手动随意添加insert
4. powershell中打开 python manage.py shell
5. 输入 from Simontest.models import BookInfo 然后输入 BookInfo.objects.all(), 即可看到bookinfo表中所有内容

# ORM更删改查
1. 增加数据:使用objects.create,写好的代码可以直接在shell中查看
2. 例如在views中写好如下代码:
    - from Simontest.models import BookInfo,PeopleInfo
    - BookInfo.objects.create(
        - name='测试入门',
        - pub_date = '2020-1-1',
        - readcount = 100,)
    - 在shell中运行之后,mysql中自动添加这本书.
3. 修改数据: 类似增加,代码:BookInfo.objects.filter(id=5).update(name='爬虫入门'),同样在shell中运行
4. 删除数据: BookInfo.objects.get(id=5).delete()或者get换成filter也行
5. 查询数据: 
    - 5.1 get查询:
        - 单一数据:book = BookInfo.objects.get(id=1) 这种方法查询如果数据不存在会抛出异常,可使用try except: 例
            - try:
                - book = BookInfo.objects.get(id=7)
            - except BookInfo.DoesNotExist:
                - print('结果不存在')
        - 多个数据:books = BookInfo.objects.all()
        - 查询数据数量: books = BookInfo.objects.all().count()
    - 5.2 filter过滤查询:
        - 单一使用get
        - 多个使用filter
        - 多个之外数据exclude
        - 例: BookInfo.objects.filter(name__contains='天') ----- 查询包含某个字段的数据
            - BookInfo.objects.filter(name__endswith='天') ----- 查询以...结尾的
            - BookInfo.objects.filter(name__isnull=True) ----- 查询为空的
            - BookInfo.objects.filter(name__in=['天','地']) ----- 查询是否存在多个中的某一个
            - BookInfo.objects.filter(id__gt=3) -----   查询大于id 3的
            - BookInfo.objects.filter(id__lt=3) -----   查询小于 3的
            - 大于等于是gte,小于等于是lte,查询不等于时用exclude方法
            - BookInfo.objects.filter(pub_year__year=1990) -----查询某一年数据
    - 5.3 两个条件查询:例如 commentcount大于readcount
        - ！首先需要导包: from django.db.models import F
            - BookInfo.objects.filter(readcount__gte=F('commentcount'))
    - 5.4 并且查询，例如：id>3 并且count小于20：
        - BookInfo.objects.filter(id__gt=3).filter(readcount__lt=20)
        - 或者可以写成：BookInfo.objects.filter(id__gt=3,readcount__lt=20)
    - 5.5 或者查询 Q查询：
        - ！首先需要导包：from django.db.models import Q
        - 语法：BookInfo.objects.filter(Q(id__gt=3)|Q(readcount__lt=20))
        - tips: 或者使用|，并且使用&，
        - 非语句查询：BookInfo.objects.filter(~Q(id__gt=3))
    - 5.6 聚合函数查询：
        - ！首先导包：from django.db.models import Sum,Max,Min,Avg,Count
        - BookInfo.objects.aggregate(Sum('readcount'))
    - 5.7 排序查询：
        - BookInfo.objects.all().order_by('readcount') - 升序
        - BookInfo.objects.all().order_by('-readcount') - 降序
    - 5.8 一对多两张表关联查询：
        - book = BookInfo.objects.get(id=1)
        - book.peopleinfo_set.all()
        - 查询id为1的书的所有人物信息。
    - 5.9 多对一两表关联查询：
        - person = PeopleInfo.objects.get(id=1)
        - person.book.name 查书
        - person.book.pub_date 查时间...etc
        - 查id为1的人物对应的书籍信息。
    - 5.10 两张表过滤查询：给几个例子
        - BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
        - BookInfo.objects.filter(peopleinfo__description__contains='六')

        - PeopleInfo.objects.filter(book__name='天龙')
        - PeopleInfo.objects.filter(book__name__contains='天')

# Django 中接收和请求HttpRequest和HttpResponse
1. urls文件中path可以用占位符：例如：path('index/<create_id>/',create), 此时在views中create()里需要传参create_id。
    - 验证用户输入的路径是否正确：
        - a. 可以通过视图函数里添加if不同的正则判断返回页面。导入正则 import re，使用re.match()方法。
        - b, 可以如下：path('index/<int:create_id>/',create)，使id输入必须为整数。这之前必须导包：from django.urls import converters。
            - b.2，如果需要自定义转换器，例如int换成手机验证。则需要导包：from django.urls.converters import register_converter
            - 同时定义一个class类。copy int的类进行复写，加入相应的正则。手机正则：'1[3-9]\d{9}'。
            - 最后 register_converter(新的类名，'方法名')。
2. 获取get请求的字符串，例如：?id=3。使用request.GET,如果Querydict字典中同一个key对应多个values，则不使用key.get('XX')方法，而用key.getlist('XX')。
3. 获取POST请求表单数据，使用request.POST接收。如果遇到403报错，需要去settings里找到middleware，找到csrf注释掉。
4. JSON数据必须使用双引号，不能用单引号。
5. 获取POST请求的JSON数据，不能使用request.POST,而要用request.body,并且需要对JSON数据进行decode处理,然后通过JSON的loads指令转成python字典：
    这里需要导包JSON
    - body = request.body
    - body_str = body.decode()
    - import json
    - body_dict = json.loads(body_str)
6. 接收html请求头信息：request.META
7. 