from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ResumeForm
from .models import Resume
from django.views import View

# Create your views here.


class HomeView(View):

    # we see blank form over get request!
    def get(self, request):
        # create object
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})
    # when we click on submit button, then post request will work

    def post(self, request):
        submitted = False
        if request.method == "POST":
            form = ResumeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.path)
                # return render(request, 'myapp/home.html', {'form':form})
        else:
            form = ResumeForm
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'myapp/home.html', {'form': form, 'submitted': submitted})


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})
# sometimes,we refresh the page, forms will resubmited,
# then simplily we have to redirect to the page using httpresponse
