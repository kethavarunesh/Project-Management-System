from django.contrib import admin
from .models import Project, EntryInformation, Approval1, Approval2, Reports, ExtraQuestions

# Register your models here
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'employee_id')  # Customize the display fields as needed

@admin.register(EntryInformation)
class EntryInformationAdmin(admin.ModelAdmin):
    list_display = ('project', 'approx_number_of_screens', 'entry_screen')
    list_filter = ('entry_screen',)  # Add filter options as needed
    search_fields = ('project__project_name',)  # Add search fields as needed

@admin.register(Approval1)
class Approval1Admin(admin.ModelAdmin):
    list_display = ('project', 'approval_needed', 'additional_approval_needed')
    list_filter = ('approval_needed', 'additional_approval_needed')
    search_fields = ('project__project_name',)

@admin.register(Approval2)
class Approval2Admin(admin.ModelAdmin):
    list_display = ('project', 'approval2_needed')
    list_filter = ('approval2_needed',)
    search_fields = ('project__project_name',)

@admin.register(Reports)
class ReportsAdmin(admin.ModelAdmin):
    list_display = ('project', 'reports_needed')
    list_filter = ('reports_needed',)
    search_fields = ('project__project_name',)

@admin.register(ExtraQuestions)
class ExtraQuestionsAdmin(admin.ModelAdmin):
    list_display = ('project', 'automails_needed', 'excel_generation_needed', 'text_file_needed')
    list_filter = ('automails_needed', 'excel_generation_needed', 'text_file_needed')
    search_fields = ('project__project_name',)
