from django.urls import path
from jobapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "jobapp"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('jobs/', views.job_list_view, name='job-list'),
    path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),
    path('bookmark-job/<int:id>/', views.job_bookmark_view, name='bookmark-job'),
    path('about/', views.single_job_view, name='about'),
    path('contact/', views.single_job_view, name='contact'),
    path('result/', views.search_result_view, name='search_result'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/employer/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),
    path('dashboard/employer/job/edit/<int:id>', views.job_edit_view, name='edit-job'),
    path('dashboard/employer/applicant/<int:id>/', views.applicant_details_view, name='applicant-details'),
    path('dashboard/employer/close/<int:id>/', views.make_complete_job_view, name='complete'),
    path('dashboard/employer/delete/<int:id>/', views.delete_job_view, name='delete'),
    path('dashboard/employee/delete-bookmark/<int:id>/', views.delete_bookmark_view, name='delete-bookmark'),
    path('feedback/', views.feedback_redirect, name='feedback_redirect'),
    path('employee-feedback/', views.employee_feedback_form, name='employee_feedback_form'),
    path('employer-feedback/', views.employer_feedback_form, name='employer_feedback_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('subscription/', views.subscription, name='subscription'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)