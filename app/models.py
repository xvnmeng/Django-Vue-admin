from django.db import models

# Create your models here.
# 编写项目的类别和对象（数据库操作、页面操作等）
# 用户类

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

# class Publisher1(models.Model):
#     uid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=64)
 
 
# # 书籍的类
# class Book(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=64)
#     publisher = models.ForeignKey(to=Publisher)  # Django中创建外键联表操作
 
 
# # 作者的类
# class Author(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=64)
#     # 一个作者可以对应多本书，一本书也可以有多个作者，多对多，在数据库中创建第三张表
#     book = models.ManyToManyField(to=Book)
