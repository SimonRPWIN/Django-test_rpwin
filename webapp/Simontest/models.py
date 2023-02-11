from django.db import models

# Create your models here.

#针对图书，先定义一个书名类
class BookInfo(models.Model): #必须继承父类（Model，系统会自动添加id主键
    name = models.CharField(max_length=10, unique=True) #定义属性值，也就是字段名
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'

    #添加魔术方法，显示具体的bookinfo_object名
    def __str__(self):
        return self.name


#再定义一个人名类,含有名字和性别两个属性
class PeopleInfo(models.Model):
    gender_choice = (
        (1,'male'),
        (2,'female')
    )

    name = models.CharField(max_length=10, unique=True) 
    gender = models.SmallIntegerField(choices=gender_choice,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)
    #外键约束，人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Peopleinfo'
        verbose_name = '人物管理'

    def __str__(self):
        return self.name
