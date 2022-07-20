from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm, ProjectsClass, TalksClass, BlogsClass

projects = [
    ProjectsClass("14042021", "Whatsapp Data Analysis",
                  "Analysing my personal group chat and finding out interesting insights about it",
                  "https://deepnote.com/@ashish-karhade/whatsapp-data-analysis-ee8e7939-c4c7-44d7-967f-972aa6fac8de",
                  "1"),
    ProjectsClass("20122020", "Dog Breed Classifier",
                  "Check the breed of the dog from image, or check which dog looks like you.",
                  "https://github.com/AshiishKarhade/Dog-Breed-Classifier", "project-image-2"),
    ProjectsClass("28042021", "COVID-19 Detection",
                  "Detection using chest x-ray images from collecting 150 Images of Positive and Negative Images of Chest X-ray from COVID-19 Test.",
                  "https://github.com/dsc-sits/COVID-19-X-RAY-Images-Detection", "project-image-3"),
]

talks = [
    TalksClass("07012020", "Machine Learning Session @ KBTCOE, Nashik",
               "Invited as guest speaker to conduct 2-Day Machine Learning Workshop", "#", "talk-image-1"),
    TalksClass("17122019", "Explore ML Workshop @ SIT, Lonavala",
               "2-Days Machine Learning workshop at Sinhgad Institutes.", "#", "talk-image-2"),
    TalksClass("25072019", "ML Facilitator Program, Google",
               "Selected as ML Facilitator and invited to Google Office, Hyderabad to learn ML from Googlers", "#", "talk-image-3"),
]


blogs = [
   "blogs"
]


# Create your views here.
def home(request):
    context = {"projects": projects,
               "talks": talks,
               "blogs": blogs
               }
    return render(request, 'index.html', context=context)


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail("Ashish Karhade - Contact", message, from_email, ['akarhade5@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "index.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
