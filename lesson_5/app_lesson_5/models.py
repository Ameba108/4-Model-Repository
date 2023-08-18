from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

User=get_user_model()

class Advertisement(models.Model):
    title=models.CharField('Заголовок',max_length=128)
    description=models.TextField('Описание')
    price=models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction=models.BooleanField('Торг',help_text='Укажите True, если торг уместен')
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    user= models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, default=1)
    image= models.ImageField('изображение', upload_to='advertisement/', blank=True, null=True)

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
    
    @admin.display(description='фото')
    def image_tag(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"',url=self.image.url
            )
        else:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"',url='/static/img/adv.png'
            )

    
    class Meta:
        db_table='advertisements'

    def __str__(self):
        return f'id={self.id} title={self.title} price={self.price}'
    
