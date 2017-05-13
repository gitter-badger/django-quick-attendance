# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 07:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0005_auto_20170513_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[(b'present', b'present'), (b'absent', b'absent'), (b'leave', b'leave')], default=b'present', max_length=20)),
                ('leave_reason', models.TextField(default=None)),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.SabhaSession')),
                ('taken_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]