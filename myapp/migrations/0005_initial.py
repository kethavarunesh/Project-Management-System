# Generated by Django 5.0.3 on 2024-04-05 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0004_remove_entryscreen_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('employee_id', models.CharField(max_length=50)),
                ('integration_requirements', models.TextField()),
                ('benefits', models.TextField()),
                ('navigation_path', models.TextField()),
                ('access_permissions', models.TextField()),
                ('similar_modules', models.TextField()),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExtraQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automails_needed', models.BooleanField(default=False)),
                ('excel_generation_needed', models.BooleanField(default=False)),
                ('text_file_needed', models.BooleanField(default=False)),
                ('additional_features', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='EntryInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approx_number_of_screens', models.CharField(max_length=50)),
                ('entry_screen', models.BooleanField(default=False)),
                ('data_entry', models.TextField()),
                ('data_entry_access', models.TextField()),
                ('entry_screen_attachment', models.FileField(upload_to='entry_screen_attachments/')),
                ('entry_screen_additional_info', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Approval2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval2_needed', models.BooleanField(default=False)),
                ('approval2_data', models.TextField()),
                ('approval2_screen', models.FileField(upload_to='approval2_screens/')),
                ('approval2_additional_info', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Approval1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_needed', models.BooleanField(default=False)),
                ('data_approval', models.TextField()),
                ('entry_approval_screen', models.FileField(upload_to='approval_screens/')),
                ('approval_additional_info', models.TextField()),
                ('additional_approval_needed', models.BooleanField(default=False)),
                ('additional_approval_data', models.TextField()),
                ('additional_approval_screen', models.FileField(upload_to='additional_approval_screens/')),
                ('additional_approval_info', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reports_needed', models.BooleanField(default=False)),
                ('reports_access', models.TextField()),
                ('reports_page_look', models.FileField(upload_to='reports_page_attachments/')),
                ('reports_additional_info', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
    ]
