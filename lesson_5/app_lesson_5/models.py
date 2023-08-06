from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Advertisement(models.Model):
    title=models.CharField('Заголовок',max_length=128)
    description=models.TextField('Описание')
    price=models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction=models.BooleanField('Торг',help_text='Укажите True, если торг уместен')
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date_time(self):
        from django.utils import  timezone
        if self.created_date.date() == timezone.now().date():
            created_time= self.created_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>',created_time
            )
        
        return self.created_date.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description='Дата обновления')
    def updated_date_time(self):
        from django.utils import  timezone
        if self.update_date.date() == timezone.now().date():
            updated_time= self.update_date.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;">Сегодня в {}</span>',updated_time
            )
        
        return self.update_date.strftime('%d.%m.%Y в %H:%M:%S')

    
    class Meta:
        db_table='advertisements'

    def __str__(self):
        return f'id={self.id} title={self.title} price={self.price}'
    
