# Generated by Django 5.0.3 on 2024-04-05 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entryscreen',
            name='project',
        ),
        migrations.RemoveField(
            model_name='extraquestions',
            name='project',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='project',
        ),
        migrations.DeleteModel(
            name='Approval',
        ),
        migrations.DeleteModel(
            name='EntryScreen',
        ),
        migrations.DeleteModel(
            name='ExtraQuestions',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Reports',
        ),
    ]
