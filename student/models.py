from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=200)
    tagline = models.CharField(max_length=250)
    about = models.TextField()

    profile_image = models.ImageField(upload_to='profile/')

    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    location = models.CharField(max_length=100)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title


class Education(models.Model):
    course = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.course


class Project(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='projects/')

    github = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    certificate_image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return self.title