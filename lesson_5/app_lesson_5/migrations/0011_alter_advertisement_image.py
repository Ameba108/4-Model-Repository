# Generated by Django 4.2.3 on 2023-08-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_5', '0010_alter_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, upload_to='advertisement/', verbose_name='изображение'),
        ),
    ]