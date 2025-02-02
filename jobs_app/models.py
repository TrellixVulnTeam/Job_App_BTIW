import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model

class intro(models.Model):
    name = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=30, default="")
    message = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name


class Signup(models.Model):
    first_name = models.CharField(max_length=10, default="")
    last_name = models.CharField(max_length=10, default="")
    email = models.CharField(max_length=10, default="")
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)

    def __str__(self):
        return self.username


class Signuprec(models.Model):

    first_name = models.CharField(max_length=10, default="")
    last_name = models.CharField(max_length=10, default="")
    designation = models.CharField(max_length=15, default="")
    email = models.CharField(max_length=20, default="")
    company = models.CharField(max_length=20, default="")
    office_ad = models.CharField(max_length=20, default="")
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Profile(models.Model):

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    designation = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    office_address = models.CharField(max_length=100, null=True)

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Resume(models.Model):

    resume = models.FileField(upload_to='resume/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Job(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    category = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)

    deleted = models.BooleanField(default=False)

    deadline = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class JobApplication(models.Model):

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        Job,
        null=True,
        on_delete=models.SET_NULL
    )
    resume = models.ForeignKey(
        Resume,
        null=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=512)
    cover_letter = models.TextField(max_length=5000)
    sites = models.CharField(max_length=1024, null=True)
    email = models.EmailField()
    skills = models.CharField(max_length=1024, null=True)
    score = models.FloatField(default=0)
    video_token = models.CharField(max_length=100, null=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CandidateProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    resume = models.ForeignKey(
        Resume,
        null=True,
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=512)
    sites = models.CharField(max_length=5000, null=True, default='')
    skills = models.CharField(max_length=1204, null=True, default='')
    gender = models.CharField(max_length=10, null=True, default='')
    address = models.CharField(max_length=256, null=True, default='')
    city = models.CharField(max_length=100, null=True, default='')
    country = models.CharField(max_length=100, null=True, default='')
    postal_code = models.CharField(max_length=100, null=True, default='')
    phone = models.CharField(max_length=26, null=True, default='')
    about = models.TextField(null=True, default='')

@receiver(post_save, sender=get_user_model())
def create_candidate_profile(sender, instance, created, **kwargs):
    if created:
        CandidateProfile.objects.create(
            user=instance,
            name='{first} {last}'.format(first=instance.first_name, last=instance.last_name),
        )

class Experience(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    @property
    def experience_years(self):
        if self.end_date:
            return int((self.end_date - self.start_date).days/365)
        else:
            return int((datetime.date.today() - self.start_date).days/365)


class Education(models.Model):
    EDUCATION_LEVEL_CHOICES = (
        (1, 'Matriculate'),
        (2, 'Intermediate'),
        (3, 'Graduation'),
        (4, 'Post-Graduation'),
        (5, 'PHD')
        )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    level = models.IntegerField(choices=EDUCATION_LEVEL_CHOICES)
    college = models.CharField(max_length=256)
    percent = models.IntegerField()
    completion_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)