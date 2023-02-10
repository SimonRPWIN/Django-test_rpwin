from django.contrib import admin

# Register your models here.


#进行models注册
from Simontest.models import BookInfo,PeopleInfo

admin.site.register(BookInfo)
admin.site.register(PeopleInfo)