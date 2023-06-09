# Generated by Django 3.2.19 on 2023-06-09 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_members'),
        ('tasks', '0002_rename_user_tasks_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.projects'),
        ),
    ]
