from django.db import models


class Question(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, null=True)
    question = models.CharField(max_length=100)
    User_url = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(int(self.bookmark_id)-int(1)) + "-" + self.question + "-" + self.User_url
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, null=True)
    search = models.CharField(max_length=255, null=True)
    product_price = models.CharField(max_length=255, null=True)
    product_place = models.CharField(max_length=255, null=True)
    product_name = models.CharField(max_length=255, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_price + "-" + self.product_place + "-" + self.product_name


