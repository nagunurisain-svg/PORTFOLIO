from django.contrib import admin
from .models import (
    Profile,
    Skill,
    Service,
    Education,
    Project,
    Certificate
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'profession',
        'email',
        'phone'
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'percentage'
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'college',
        'year'
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organization'
    )