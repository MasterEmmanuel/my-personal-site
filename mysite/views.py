from django.shortcuts import render
import datetime




def index(request):
    time_now=datetime.datetime.now()
    night_time= time_now.replace(hour=19, minute=45, second=0, microsecond=0)
    if (time_now.hour >= night_time.hour) or (time_now.hour <= 5):
        template = 'iam.html'
    else:
        template= 'iam.html'
    return render(request, template)

def resume(request):
    template = 'my_resume.html'
    context = {
        'title':'title',
    }
    return render(request, template)