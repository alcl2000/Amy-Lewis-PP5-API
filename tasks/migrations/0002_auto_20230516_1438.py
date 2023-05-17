# Generated by Django 3.2.19 on 2023-05-16 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_options'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='completed',
        ),
        migrations.AddField(
            model_name='tasks',
            name='progress',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('complete', 'Complete')], default='not_started', max_length=11),
        ),
        migrations.AddField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.projects'),
        ),
    ]