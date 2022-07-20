from django.db import models
from django import forms
from datetime import date, datetime


# Create your models here.

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea, required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class Work:
    dates = date.today().strftime("%b %d, %y")
    title = "Default Title"
    description = "Default Description"
    link = "https://www.google.com"
    image_name = "photo-1"

    def __init__(self, dates, title, description, link, image_name):
        self.dates = datetime.strptime(dates, "%d%m%Y").date().strftime("%b %m, %Y")
        self.title = title
        self.description = description
        self.link = link
        self.image_name = image_name

    def __str__(self):
        print(self.title)


class ProjectsClass(Work):
    def __str__(self):
        print("Project : " + self.title)


class TalksClass(Work):
    def __str__(self):
        print("Talks : " + self.title)


class BlogsClass(Work):
    def __str__(self):
        print("Blogs : " + self.title)
