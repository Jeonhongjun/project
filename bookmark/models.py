from django.db import models


class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    bookmark_name = models.CharField(max_length=100)
    bookmark_url = models.CharField(max_length=255)
    bookmark_desc = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.bookmark_id) + "-" + self.bookmark_name + "-" + self.bookmark_url(max_length=100)
# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    search = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.product.id) + "-" + seslf.image + "-" + self.bookmark_url(max_length=100)


