# Generated by Django 2.2 on 2019-05-02 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20190502_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='complaint',
            options={'ordering': ['Complaint_title', 'Complaint_writer', 'Complaint_writer_id', 'Complaint_writer_phone', 'Complaint_email', 'Complaint_date', 'Complaint_content', 'Complaint_reply'], 'verbose_name': 'شكاوى المواطنين', 'verbose_name_plural': 'شكاوى المواطنين'},
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='Complaint_replay',
            new_name='Complaint_reply',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Complaint_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 2, 11, 9, 8, 939952), help_text='التاريخ', null=True, verbose_name='الوقت والتاريخ'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 2, 11, 9, 8, 939952), help_text='التاريخ', null=True, verbose_name='الوقت والتاريخ'),
        ),
    ]