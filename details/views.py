from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views import View

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class Education(View):
    def get(self,request):
        return render(request,'education.html')

class Skills(View):
    def get(self,request):
        return render(request,'skills.html')

class Projects(View):
    def get(self,request):
        return render(request,'projects.html')

class Certificates(View):
    def get(self,request):
        return render(request,'certificates.html')

class Internships(View):
    def get(self,request):
        return render(request,'internships.html')

from django.contrib.staticfiles import finders
class DownloadCV(View):
    def get(self, request):
        cv_path = finders.find("files/cv.pdf")

        if not cv_path:
            raise Http404("CV not found.")

        return FileResponse(
            open(cv_path, "rb"),
            as_attachment=True,
            filename="Ajith_M_Joshy_CV.pdf"
        )