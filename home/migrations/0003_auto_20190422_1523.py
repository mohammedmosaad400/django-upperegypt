# Generated by Django 2.2 on 2019-04-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190422_1454'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['news_Title', 'news_Img', 'news_Content']},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='newsContent',
            new_name='news_Content',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='newsImg',
            new_name='news_Img',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='newsTitle',
            new_name='news_Title',
        ),
        migrations.AddField(
            model_name='news',
            name='news_Date',
            field=models.DateField(blank=True, help_text='Enter the date', null=True),
        ),
    ]
