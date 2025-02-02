# Generated by Django 2.2.1 on 2019-05-05 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs_app', '0014_auto_20190505_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'matric'), (2, 'inter'), (3, 'grad'), (4, 'pgrad'), (5, 'phd')])),
                ('college', models.CharField(max_length=256)),
                ('percent', models.IntegerField()),
                ('completion_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
