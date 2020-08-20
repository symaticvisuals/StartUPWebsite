# Generated by Django 3.0.5 on 2020-04-30 18:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_investor', models.BooleanField(default=True)),
                ('is_entre', models.BooleanField(default=False)),
                ('phone', models.CharField(default='', max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_funds', models.IntegerField(default=0)),
                ('previous_proj', models.CharField(default='nan', max_length=1000)),
                ('logo', models.ImageField(default='', upload_to='investor/logo')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor_profile', to='user_app.Userp')),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_title', models.CharField(default=' ', max_length=60, unique=True)),
                ('idea_desc', models.CharField(default=' ', max_length=2048)),
                ('amount', models.IntegerField(default=0)),
                ('no_of_days_req', models.IntegerField(default=0)),
                ('last_date', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(default='', upload_to='entre/logo')),
                ('idea_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_app.Idea')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entre_profile', to='user_app.Userp')),
            ],
        ),
    ]