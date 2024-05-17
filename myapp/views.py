from django.shortcuts import render, get_object_or_404,redirect
from .models import Project, EntryInformation, Approval1, Approval2, Reports, ExtraQuestions

def index(request):
    if request.method == 'POST':
       
        project_name = request.POST.get('project_name')
        employee_id = request.POST.get('employee_id')
        integration_requirements = request.POST.get('integration_requirements')
        benefits = request.POST.get('benefits')
        navigation_path = request.POST.get('navigation_path')
        access_permissions = request.POST.get('access_permissions')
        similar_modules = request.POST.get('similar_modules')
        additional_info = request.POST.get('additional_info')

        approx_number_of_screens = request.POST.get('approx_number_of_screens')
        entry_screen = request.POST.get('entry_screen') == 'on' 
        data_entry = request.POST.get('data_entry')
        data_entry_access = request.POST.get('data_entry_access')
        entry_screen_additional_info = request.POST.get('entry_screen_additional_info')

        approval_needed = request.POST.get('approval_needed') == 'on'  
        data_approval = request.POST.get('data_approval')
        approval_additional_info = request.POST.get('approval_additional_info')
        additional_approval_needed = request.POST.get('additional_approval_needed') == 'on' 
        additional_approval_data = request.POST.get('additional_approval_data')
        additional_approval_info = request.POST.get('additional_approval_info')

        approval2_needed = request.POST.get('approval2_needed') == 'on'  
        approval2_data = request.POST.get('approval2_data')
        approval2_additional_info = request.POST.get('approval2_additional_info')

        reports_needed = request.POST.get('reports_needed') == 'on' 
        reports_access = request.POST.get('reports_access')
        reports_additional_info = request.POST.get('reports_additional_info')

        automails_needed = request.POST.get('automails_needed') == 'on'  
        excel_generation_needed = request.POST.get('excel_generation_needed') == 'on'  
        text_file_needed = request.POST.get('text_file_needed') == 'on'  
        additional_features = request.POST.get('additional_features')

        
        entry_screen_attachment = request.FILES.get('entry_screen_attachment')
        entry_approval_screen = request.FILES.get('entry_approval_screen')
        additional_approval_screen = request.FILES.get('additional_approval_screen')
        approval2_screen = request.FILES.get('approval2_screen')
        reports_page_look = request.FILES.get('reports_page_look')

        project_obj, created = Project.objects.get_or_create(
            project_name=project_name,
            defaults={
                'employee_id': employee_id,
                'integration_requirements': integration_requirements,
                'benefits': benefits,
                'navigation_path': navigation_path,
                'access_permissions': access_permissions,
                'similar_modules': similar_modules,
                'additional_info': additional_info
            }
        )

        entry_info_obj, created = EntryInformation.objects.get_or_create(
            project=project_obj,
            defaults={
                'approx_number_of_screens': approx_number_of_screens,
                'entry_screen': entry_screen,
                'data_entry': data_entry,
                'data_entry_access': data_entry_access,
                'entry_screen_attachment': entry_screen_attachment,
                'entry_screen_additional_info': entry_screen_additional_info
            }
        )

        approval1_obj, created = Approval1.objects.get_or_create(
            project=project_obj,
            defaults={
                'approval_needed': approval_needed,
                'data_approval': data_approval,
                'approval_additional_info': approval_additional_info,
                'additional_approval_needed': additional_approval_needed,
                'additional_approval_data': additional_approval_data,
                'entry_approval_screen': entry_approval_screen,
                'additional_approval_screen': additional_approval_screen,
                'additional_approval_info': additional_approval_info
            }
        )

        approval2_obj, created = Approval2.objects.get_or_create(
            project=project_obj,
            defaults={
                'approval2_needed': approval2_needed,
                'approval2_data': approval2_data,
                'approval2_screen': approval2_screen,
                'approval2_additional_info': approval2_additional_info
            }
        )

        reports_obj, created = Reports.objects.get_or_create(
            project=project_obj,
            defaults={
                'reports_needed': reports_needed,
                'reports_access': reports_access,
                'reports_page_look': reports_page_look,
                'reports_additional_info': reports_additional_info
            }
        )

        extra_questions_obj, created = ExtraQuestions.objects.get_or_create(
            project=project_obj,
            defaults={
                'automails_needed': automails_needed,
                'excel_generation_needed': excel_generation_needed,
                'text_file_needed': text_file_needed,
                'additional_features': additional_features
            }
        )

        
        return redirect ( 'reports/')
 
    return render(request, 'index.html')

def reports(request):
    projects = Project.objects.all()
    return render(request, 'reports.html', {'projects': projects})


def project_details(request, project_name):
    
    project = get_object_or_404(Project, project_name=project_name)

    
    entry_info = EntryInformation.objects.filter(project=project)
    approval1 = Approval1.objects.filter(project=project)
    approval2 = Approval2.objects.filter(project=project)
    reports = Reports.objects.filter(project=project)
    extra_questions = ExtraQuestions.objects.filter(project=project)

    context = {
        'project': project,
        'entry_info': entry_info,
        'approval1': approval1,
        'approval2': approval2,
        'reports': reports,
        'extra_questions': extra_questions,
    }

    return render(request, 'project_details.html', context)

def home(request):
    return render(request,'Home.html')