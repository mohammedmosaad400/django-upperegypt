from _ast import mod
import datetime
from django.db import models
import uuid
# Create your models here.
class News(models.Model) :
    # fields
    news_Title=models.CharField(max_length=200,help_text='أدخل عنوان الخبر', verbose_name='عنوان الخبر')
    news_Img=models.ImageField(upload_to='home/static/img', help_text='قم بتحميل صورة الخبرة', verbose_name='صورة الخبر' )
    news_Date=models.DateTimeField(null=True,blank=True, help_text='أدخل الوقت والتاريخ',verbose_name='الوقت والتاريخ')
    news_Content=models.TextField(help_text='أدخل محتوى الخبر',verbose_name='محتوى الخبر')
    # metadata
    class Meta:
        ordering=['news_Title','news_Img','news_Content']
        verbose_name = 'أخبار أهل الصعيد'
        verbose_name_plural = 'أخبار أهل الصعيد'
    # methods
    def get_img_path(self):
        s = str(self.news_Img)
        return s[5:]
    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])
    def __str__(self):
        return self.news_Title

class News2(models.Model):
    # fields
    news_Title=models.CharField(max_length=200,help_text='أدخل عنوان الخبر', verbose_name='عنوان الخبر')
    news_Img=models.ImageField(upload_to='home/static/img', help_text='قم بتحميل صورة الخبرة', verbose_name='صورة الخبر' )
    news_Date=models.DateTimeField(null=True,blank=True, help_text='أدخل الوقت والتاريخ',verbose_name='الوقت والتاريخ')
    news_Content=models.TextField(help_text='أدخل محتوى الخبر',verbose_name='محتوى الخبر')
    # metadata
    class Meta:
        ordering=['news_Title','news_Img','news_Content']
        verbose_name = 'أخبار الهيئة'
        verbose_name_plural = 'أخبار الهيئة'

    # methods
    def get_img_path(self):
        s = str(self.news_Img)
        return s[5:]
    def get_absolute_url(self):
        return reverse('news2-detail', args=[str(self.id)])
    def __str__(self):
        return self.news_Title


class Slide(models.Model):
    slide_img=models.ImageField(upload_to='home/static/img/slideShow',help_text='قم برفع الصورة',verbose_name='الصورة')
    slide_caption=models.CharField(default="Caption Text", max_length=200,help_text='اكتب التعليق - التعقيب أسفل الصورة',verbose_name='تعليق على الصورة')
    slide_album=models.CharField(default='Tourist Album', max_length=200,help_text='أدخل اسم الألبوم(مثال : سياحية - فرعونية - إسلامية - قبطية  وهكذا ...)',verbose_name='اسم الألبوم')
    class Meta:
        ordering=['slide_img']
        verbose_name = 'معرض الصور'
        verbose_name_plural = 'معرض الصور'
    def get_img_path(self):
        s = str(self.slide_img)
        return s[5:]
    def get_absolute_url(self):
        return reverse('slide-detail',args=[str(self.id)])
    def __str__(self):
        return str(self.slide_caption)

class Agriculture_Suggestion(models.Model):
    title = models.CharField(max_length=500,help_text='عنوان الإقتراح',verbose_name='عنوان الإقتراح')
    content = models.TextField(default='محتوى الإقتراح ...',verbose_name='محتوى الإقتراح')
    class Meta:
        ordering = ['title' ,'content', ]
        verbose_name = 'مقترحات زراعية'
        verbose_name_plural = 'مقترحات زراعية'
    def __str__(self):
        return str(self.title)
class Industrial_Suggestion(models.Model):
    title = models.CharField(max_length=500,help_text='عنوان الإقتراح',verbose_name='عنوان الإقتراح')
    content = models.TextField(default='محتوى الإقتراح ...',verbose_name='محتوى الإقتراح')
    class Meta:
        ordering = ['title' ,'content', ]
        verbose_name = 'مقترحات صناعية'
        verbose_name_plural = 'مقترحات صناعية'
    def __str__(self):
        return str(self.title)
class Development_Suggestion(models.Model):
    title = models.CharField(max_length=500,help_text='عنوان الإقتراح',verbose_name='عنوان الإقتراح')
    content = models.TextField(default='محتوى الإقتراح ...',verbose_name='محتوى الإقتراح')
    class Meta:
        ordering = ['title' ,'content', ]
        verbose_name = 'مقترحات تنموية'
        verbose_name_plural = 'مقترحات تنموية'
    def __str__(self):
        return str(self.title)
class Service_Suggestion(models.Model):
    title = models.CharField(max_length=500,help_text='عنوان الإقتراح',verbose_name='عنوان الإقتراح')
    content = models.TextField(default='محتوى الإقتراح ...',verbose_name='محتوى الإقتراح')
    class Meta:
        ordering = ['title' ,'content', ]
        verbose_name = 'مقترحات خدمية'
        verbose_name_plural = 'مقترحات خدمية'
    def __str__(self):
        return str(self.title)
class Tourist_Suggestion(models.Model):
    title = models.CharField(max_length=500,help_text='عنوان الإقتراح',verbose_name='عنوان الإقتراح')
    content = models.TextField(default='محتوى الإقتراح ...',verbose_name='محتوى الإقتراح')
    class Meta:
        ordering = ['title' ,'content', ]
        verbose_name = 'مقترحات سياحية'
        verbose_name_plural = 'مقترحات سياحية'
    def __str__(self):
        return str(self.title)

class Organization_Task(models.Model):
    organization_task = models.TextField(help_text='مهام الهيئة',verbose_name='مهام الهيئة')
    class Meta:
        ordering = ['organization_task']
        verbose_name = 'مهام الهيئة'
        verbose_name_plural = 'مهام الهيئة'
    def __str__(self):
        return str(self.organization_task)

class Organization_Leader(models.Model):
    organization_leader = models.CharField(max_length=300,help_text='قيادات الهيئة',verbose_name='قيادات الهيئة')
    class Meta:
        ordering = ['organization_leader']
        verbose_name = 'قيادات الهيئة'
        verbose_name_plural = 'قيادات الهيئة'
    def __str__(self):
        return str(self.organization_leader)

class Organization_Governing_Council(models.Model):
    title = models.CharField(max_length=300,help_text='اللقب',verbose_name='اللقب أو الدرجة')
    name = models.CharField(max_length=400,help_text='الاسم',verbose_name='الاسم')
    class Meta:
        ordering = ['title','name']
        verbose_name = 'مجلس الإدارة'
        verbose_name_plural = 'مجلس الإدارة'
    def __str__(self):
        return str(self.title) +' /  ' + str(self.name)

class Organization_Law(models.Model):
    law_title = models.CharField(max_length=1000,help_text='الوثيقة',verbose_name='عنوان الوثيقة')
    law_date = models.DateField(help_text='التاريخ',verbose_name='تاريخ الوثيقة')
    law_content = models.FileField(help_text='ملف الوثيقة',verbose_name='ملف الوثيقة',upload_to='home/static/docs')
    class Meta:
        ordering = ['law_title','law_date','law_content',]
        verbose_name = 'قوانين ولوائح'
        verbose_name_plural = 'قوانين ولوائح'
    def get_doc_path(self):
        s = str(self.law_content)
        return s[5:]
    def __str__(self):
        return str(self.law_title)

class Project_Ended(models.Model):
    project_name = models.CharField(max_length=500,help_text='اسم المشروع',verbose_name='اسم المشروع')
    project_description = models.TextField(help_text='وصف المشروع',verbose_name='وصف المشروع')
    class Meta:
        ordering = ['project_name','project_description']
        verbose_name = 'مشروعات تم تنفيذها'
        verbose_name_plural = 'مشروعات تم تنفيذها'
    def __str__(self):
        return str(self.project_name)

class Project_UnderProcessing(models.Model):
    project_name = models.CharField(max_length=500,help_text='اسم المشروع',verbose_name='اسم المشروع')
    project_description = models.TextField(help_text='وصف المشروع',verbose_name='وصف المشروع')
    class Meta:
        ordering = ['project_name','project_description']
        verbose_name = 'مشروعات تحت التنفيذ'
        verbose_name_plural = 'مشروعات تحت التنفيذ'
    def __str__(self):
        return str(self.project_name)

class Project_Planned(models.Model):
    project_name = models.CharField(max_length=500,help_text='اسم المشروع',verbose_name='اسم المشروع')
    project_description = models.TextField(help_text='وصف المشروع',verbose_name='وصف المشروع')
    class Meta:
        ordering = ['project_name','project_description']
        verbose_name = 'مشروعات مخططه'
        verbose_name_plural = 'مشروعات مخططه'
    def __str__(self):
        return str(self.project_name)

class Complaint(models.Model):

    Complaint_reply = models.TextField(default='لم يتم الرد بعد ...',verbose_name='الرد على الشكوى')
    Complaint_title =models.CharField(max_length=500,help_text="عنوان الشكوى",verbose_name='عنوان الشكوى')
    Complaint_writer =models.CharField( max_length=200,help_text="اسم المواطن",verbose_name='اسم المواطن')
    Complaint_writer_id =models.CharField( max_length=200,help_text="الرقم القومي",verbose_name='الرقم القومي')
    Complaint_writer_phone =models.CharField( max_length=200,help_text="رقم الهاتف",verbose_name='رقم الهاتف')
    Complaint_email=models.EmailField(max_length=254,help_text="البريد الإلكتروني",verbose_name='البريد الإلكتروني')
    Complaint_date=models.DateTimeField(default=datetime.datetime.now(),null=True,blank=True,help_text="التاريخ",verbose_name='الوقت والتاريخ')
    Complaint_content=models.TextField(default='محتوى الشكوى ...', help_text='',verbose_name='محتوى الشكوى')
    class Meta:
        ordering=['Complaint_reply','Complaint_title','Complaint_writer','Complaint_writer_id','Complaint_writer_phone', 'Complaint_email', 'Complaint_date', 'Complaint_content',]
        verbose_name = 'شكاوى المواطنين'
        verbose_name_plural = 'شكاوى المواطنين'

    def get_absolute_url(self):
        return reverse('Complaint-detail',args=[str(self.id)])
    def __str__(self):
        return str(self.Complaint_title)
class Suggestion(models.Model):
    suggestion_title=models.CharField(max_length=500,help_text="عنوان الإقتراح",verbose_name='عنوان الإقتراح')
    suggestion_writer=models.CharField( max_length=200,help_text="اسم المواطن",verbose_name='اسم المواطن')
    suggestion_email=models.EmailField(max_length=254,help_text="البريد الإلكتروني",verbose_name='البريد الإلكتروني')
    suggestion_date=models.DateTimeField(default=datetime.datetime.now(),null=True,blank=True,help_text="التاريخ",verbose_name='الوقت والتاريخ')
    suggestion_content=models.TextField(default='محتوى الإقتراح ...', help_text='',verbose_name='محتوى الإقتراح')
    choices = (('option1','مقترحات زراعية'),('option2','مقترحات صناعية'),('option3','مقترحات تنموية'),('option4','مقترحات خدمية'),('option5','مقترحات سياحية'))
    suggestion_kind = models.CharField(max_length=100,choices=choices,help_text='نوع الإقتراح',verbose_name='نوع الإقتراح')

    class Meta:
        ordering=['suggestion_title','suggestion_writer', 'suggestion_email', 'suggestion_date', 'suggestion_content']
        verbose_name = 'مقترحات المواطنين'
        verbose_name_plural = 'مقترحات المواطنين'
    def get_absolute_url(self):
        return reverse('suggestion-detail',args=[str(self.id)])
    def __str__(self):
        return str(self.suggestion_title)

class Location(models.Model):
    location = models.CharField(max_length=500,help_text='مكان الهيئة',verbose_name='مكان الهيئة')
    class Meta:
        ordering = ['location',]
        verbose_name = 'مكان الهيئة'
        verbose_name_plural = 'مكان الهيئة'
    def __str__(self):
        return str(self.location)
class Phone(models.Model):
    phone=models.CharField(max_length=200,help_text='تليفونات الهيئة',verbose_name='تليفونات الهيئة')
    class Meta:
        ordering = ['phone']
        verbose_name = 'تليفونات الهيئة'
        verbose_name_plural = 'تليفونات الهيئة'
    def __str__(self):
        return str(self.phone)
