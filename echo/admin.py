# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Node, Line, Device, Employee, OggInfo, CompareCount

#对NodeAdmin进行个性化配置
class NodeAdmin(admin.ModelAdmin):
    #在list页面上显示指定的字段
    list_display = ('node_name','node_address','node_signer')
    #在编辑、新增页面上排除node_signer的选项
    exclude = ('node_signer',)
    #对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.node_signer = str(request.user)
        obj.save()

class LineAdmin(admin.ModelAdmin):
    #在编辑、新增页面上排除line_signer的选项
    exclude = ('line_signer',)
    #对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.line_signer = str(request.user)
        obj.save()

class DeviceAdmin(admin.ModelAdmin):
    #在编辑、新增页面上排除device_signer的选项
    exclude = ('device_signer',)
    #对保存函数进行更改，将登录用户设置为登记人
    def save_model(self, request, obj, form, change):
        obj.device_signer = str(request.user)
        obj.save()

class OggInfoAdmin(admin.ModelAdmin):
    #在编辑、新增页面上排除device_signer的选项
    list_display = ('ogginfo_prov','ogginfo_type','ogginfo_host','ogginfo_status','ogginfo_detail','ogginfo_diskspace','ogginfo_tablespace','ogginfo_delay','ogginfo_suspend','ogginfo_createtime')

class CompareCountAdmin(admin.ModelAdmin):
    #在编辑、新增页面上排除device_signer的选项
    list_display = ('comparecount_prov','comparecount_type','comparecount_tab','comparecount_src','comparecount_dst','comparecount_diff','comparecount_date')


admin.site.register(Node,NodeAdmin)
admin.site.register(Line,LineAdmin)
admin.site.register(Employee)
admin.site.register(Device,DeviceAdmin)
admin.site.register(OggInfo,OggInfoAdmin)
admin.site.register(CompareCount,CompareCountAdmin)
