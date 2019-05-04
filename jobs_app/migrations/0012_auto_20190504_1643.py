# Generated by Django 2.2.1 on 2019-05-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0011_candidateprofile_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofile',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='address',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='phone',
            field=models.CharField(max_length=26, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='postal_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]