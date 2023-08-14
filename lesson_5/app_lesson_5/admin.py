from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html

class AvertisementAdmin(admin.ModelAdmin):
    list_display=['title','description','price','auction','created_date_time','updated_date_time','image_tag']
    actions=['set_auction_as_false','set_auction_as_true']
    list_filter=['price']
    fieldsets=(
        ('Общее',{
            'fields':('title','description','image'),
            'classes':['collapse'],
        }),
        ('Финансы',{
            'fields':('price','auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='убрать возможность торга')
    def set_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    
    @admin.action(description='добавить возможность торга')
    def set_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    
    @admin.display(description='Изображение')
    def image_tag(self,obj):
        return format_html('<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.image.url))


admin.site.register(Advertisement,AvertisementAdmin)