# Generated by Django 3.2.19 on 2023-05-19 10:38

from django.conf import settings
from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_auto_20230516_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(blank=True, default=' ', on_delete=models.SET(tasks.models.Tasks.set_no_owner), to='auth.user'),
            preserve_default=False,
        ),
    ]
