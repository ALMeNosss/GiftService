from django.db import models

class UserModel (models.Model):
id: models.PositiveIntegerField(unique=True, primary_key=True)
user_name: models.CharField(max_length=50, unique=True)
name: models.CharField(max_length=50)
password: models.CharField(max_length=30) 

class ProductHistoryModel
id: models.PositiveIntegerField(unique=True, primary_key=True)
userid=UserModel.id
count: models.PositiveBigIntegerField()
