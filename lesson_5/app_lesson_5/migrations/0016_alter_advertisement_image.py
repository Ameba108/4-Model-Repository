# Generated by Django 4.2.3 on 2023-08-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lesson_5', '0015_alter_advertisement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='advertisement/', verbose_name='изображение'),
            preserve_default=False,
        ),
    ]