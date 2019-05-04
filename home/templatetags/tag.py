# -*- coding: utf-8 -*-
from ummalqura.hijri_date import HijriDate
from django import template
import  datetime
register=template.Library()
@register.simple_tag()
def getdatefunction():

    today =datetime.date.today()
    um = ''
    um = HijriDate(today.year, today.month, today.day, gr=True)
    um = str(um.day) +' '+ str(um.month_name) + ' ' + str(um.year)
    now = datetime.datetime.now()
    day = now.strftime("%A")
    month = now.strftime("%B")
    daynumber=now.strftime("%d")
    year=now.strftime("%Y")
    if (day == "Friday"): day = "الجمعة"
    if (day == "Saturday"): day = "السبت"
    if (day == "Sunday"): day = "الأحد"
    if (day == "Monday"): day = "الإثنين"
    if (day == "Tuesday"): day = "الثلاثاء"
    if (day == "Wednesday"): day = "الأربعاء"
    if (day == "Thursday"): day = "الخميس"
    if (month == "January"): month = "يناير"
    if (month == "February"): month = "فبراير"
    if (month == "March"): month = "مارس"
    if (month == "April"): month = "أبريل"
    if (month == "May"): month = "مايو"
    if (month == "June"): month = "يونيو"
    if (month == "July"): month = "يوليو"
    if (month == "August"): month = "أغسطس"
    if (month == "September"): month = "سبتمبر"
    if (month == "October"): month = "أكتوبر"
    if (month == "November"): month = "نوفمبر"
    if (month == "December"): month = "ديسمبر"
    now = day +'  '+ daynumber +'  '+ month +'  '+ year
    now.encode(encoding='utf-8')
    return um + "  --  " + now
