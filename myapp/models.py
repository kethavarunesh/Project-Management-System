

from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255, primary_key=True)
    employee_id = models.CharField(max_length=50)
    integration_requirements = models.TextField()
    benefits = models.TextField()
    navigation_path = models.TextField()
    access_permissions = models.TextField()
    similar_modules = models.TextField()
    additional_info = models.TextField()

class EntryInformation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    approx_number_of_screens = models.CharField(max_length=50)
    entry_screen = models.BooleanField(default=False)
    data_entry = models.TextField()
    data_entry_access = models.TextField()
    entry_screen_attachment = models.FileField(upload_to='entry_screen_attachments/')
    entry_screen_additional_info = models.TextField()

class Approval1(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    approval_needed = models.BooleanField(default=False)
    data_approval = models.TextField()
    entry_approval_screen = models.FileField(upload_to='approval_screens/')
    approval_additional_info = models.TextField()
    additional_approval_needed = models.BooleanField(default=False)
    additional_approval_data = models.TextField()
    additional_approval_screen = models.FileField(upload_to='additional_approval_screens/')
    additional_approval_info = models.TextField()

class Approval2(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    approval2_needed = models.BooleanField(default=False)
    approval2_data = models.TextField()
    approval2_screen = models.FileField(upload_to='approval2_screens/')
    approval2_additional_info = models.TextField()

class Reports(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reports_needed = models.BooleanField(default=False)
    reports_access = models.TextField()
    reports_page_look = models.FileField(upload_to='reports_page_attachments/')
    reports_additional_info = models.TextField()

class ExtraQuestions(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    automails_needed = models.BooleanField(default=False)
    excel_generation_needed = models.BooleanField(default=False)
    text_file_needed = models.BooleanField(default=False)
    additional_features = models.TextField()

