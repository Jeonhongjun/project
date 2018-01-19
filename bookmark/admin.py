from django.contrib import admin
from django.contrib import admin
from .models import Question
from .models import Product
from .models import lowshop
from daterange_filter.filter import DateRangeFilter

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('email', 'question', 'User_url', 'created_time') # 리스트에 이 필드들 추가
    list_filter = ['created_time'] # 리스트에 필터 추가
    search_fields = ['email', 'created_time', 'question', 'User_url'] # 검색 필터 추가


admin.site.register(Question, QuestionAdmin)  # 두 번째 인자로 위에 만든 model admin class를 넘긴다.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('email', 'search', 'product_name', 'product_place', 'created_time') # 리스트에 이 필드들 추가
    list_filter = ['created_time'] # 리스트에 필터 추가
    search_fields = ['email', 'search', 'product_name', 'product_place', 'created_time'] # 검색 필터 추가

admin.site.register(Product, ProductAdmin)

class lowshopAdmin(admin.ModelAdmin):
    list_display = ('email', 'lowest', 'created_time') # 리스트에 이 필드들 추가
    list_filter = [('created_time', DateRangeFilter), 'lowest'] # 리스트에 필터 추가
    search_fields = ['email', 'lowest', 'created_time'] # 검색 필터 추가

admin.site.register(lowshop, lowshopAdmin)
# Register your models here.
