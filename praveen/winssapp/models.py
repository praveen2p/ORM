from django.db import models
from django.contrib import admin
class Book_DB(models.Model):
    bookno=models.IntegerField(primary_key=True);
    authorname=models.CharField(max_length=20);
    bookname=models.CharField(max_length=50);
    version=models.IntegerField();
    pageno=models.IntegerField();
class Book_DBAdmin(admin.ModelAdmin):
    list_display=("bookno","authorname","bookname","version","pageno");

