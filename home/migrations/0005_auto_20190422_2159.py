# Generated by Django 2.2 on 2019-04-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190422_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_Img',
            field=models.ImageField(help_text='Enter field doc', upload_to='home/static/img'),
        ),
    ]
