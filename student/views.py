from django.shortcuts import render
from .models import (
    Profile,
    Skill,
    Service,
    Education,
    Project,
    Certificate,
)


def home(request):

    profile = Profile.objects.first()

    skills = Skill.objects.all()

    services = Service.objects.all()

    education = Education.objects.all()

    projects = Project.objects.all()

    certificates = Certificate.objects.all()

    context = {

        "profile": profile,

        "skills": skills,

        "services": services,

        "education": education,

        "projects": projects,

        "certificates": certificates,

    }

    return render(request, "student/index.html", context)