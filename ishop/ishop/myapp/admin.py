from django.contrib import admin
from .models import MyUser, Tovar, Purchase, Vozvrat


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'gender', 'email', 'purse', 'birthday')


class TovarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'number')


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'buyer', 'article', 'article_number', 'purchase_date')


class VozvratAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'request_time')


admin.site.register(MyUser)
admin.site.register(Tovar)
admin.site.register(Purchase)
admin.site.register(Vozvrat)