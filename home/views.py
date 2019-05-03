from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import generic
# Create your views here.
def condition(request):
    context = { }
    return render(request,'condition.html',context=context)
def index(request):
    all_news=News.objects.all()
    all_news2=News2.objects.all()
    all_slide=Slide.objects.all()
    location=Location.objects.all()
    phone = Phone.objects.all()
    agriculture_suggestion = Suggestion.objects.all()
    industrial_suggestion = Suggestion.objects.all()
    development_suggestion = Suggestion.objects.all()
    service_suggestion = Suggestion.objects.all()
    tourist_suggestion = Suggestion.objects.all()
    organization_task = Organization_Task.objects.all()
    organization_leader = Organization_Leader.objects.all()
    organization_council = Organization_Governing_Council.objects.all()
    organization_law = Organization_Law.objects.all()
    project_ended = Project_Ended.objects.all()
    project_processing = Project_UnderProcessing.objects.all()
    project_planned = Project_Planned.objects.all()

    complaint_follow = Complaint.objects.all()

    page_path = request.get_full_path()

    if request.method == 'POST':
        suggestion_form = SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            return redirect('index')
    else:
        suggestion_form = SuggestionForm()
    if request.method == 'POST':
        complaint_form = ComplaintForm(request.POST)
        if complaint_form.is_valid():
            complaint_form.save()
            return redirect('index')
    else:
        complaint_form = ComplaintForm()
    context = {'all_news': all_news,'all_news2':all_news2, 'all_slide': all_slide,'suggestion_form':suggestion_form,
               'complaint_form':complaint_form,
               'page_path':page_path,'location':location,'phone':phone, 'agriculture_suggestion':agriculture_suggestion,
               'industrial_suggestion' : industrial_suggestion,'development_suggestion': development_suggestion ,
               'service_suggestion': service_suggestion,'tourist_suggestion':tourist_suggestion, 'organization_task':organization_task,
               'organization_leader':organization_leader,'organization_council' : organization_council,'organization_law':organization_law,
               'project_ended' : project_ended, 'project_processing':project_processing,'project_planned' : project_planned,
               'complaint_follow' : complaint_follow,
               }
    return render(request,'index.html',context=context)

class NewsListView(generic.ListView):
    model = News
    paginate_by = 4
class NewsDetailView(generic.DetailView):
    model = News
class News2DetailView(generic.DetailView):
    model = News2
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


