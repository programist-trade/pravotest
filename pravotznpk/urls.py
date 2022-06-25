from django.urls import path, re_path
from django.views.generic import TemplateView
from .models import Subject

from . import views

law = Subject.objects.all()

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html",
    extra_context={"law": law})),
    re_path(r'^info', TemplateView.as_view(template_name="info.html"), name='info'),
    re_path(r'^(?P<subjectid>\d+)', views.choose_subject),
]