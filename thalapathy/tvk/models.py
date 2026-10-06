from django.db import models
from django.contrib import admin
class customer_DB(models.Model):
    Name=models.CharField(max_length=10)
    Address=models.TextField()
    Mobile=models.IntegerField()
    Rc_number=models.CharField(max_length=10,primary_key=True)
    DL_Number=models.CharField(max_length=16)
    Vehicle_model=models.CharField(max_length=10)
    Issues=models.TextField()
class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Name","Address","Mobile","Rc_number","DL_Number","Vehicle_model","Issues"]
