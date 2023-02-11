from django.db import models

# Create your models here.

#针对图书，先定义一个书名类
class BookInfo(models.Model): #必须继承父类（Model，系统会自动添加id主键
    name = models.CharField(max_length=10) #定义属性值，也就是字段名
    #添加魔术方法，显示具体的bookinfo_object名
    def __str__(self):
        return self.name


#再定义一个人名类,含有名字和性别两个属性
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    #外键约束，人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
