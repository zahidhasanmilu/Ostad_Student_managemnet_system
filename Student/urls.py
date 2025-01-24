from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_student/', views.create_student, name='create_student'),
    path('student/update/<int:student_id>/', views.update_student, name='student_update'),

    # path('add_student/', views.add_student, name='add_student'),
    # path('update_student/<int:id>/', views.update_student, name='update_student'),
    # path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
    # path('student_list/', views.student_list, name='student_list'),
    # path('search_student/', views.search_student, name='search_student'),
    # path('student_detail/<int:id>/', views.student_detail, name='student_detail'),
    # path('student_detail/<int:id>/add_marks/', views.add_marks, name='add_marks'),
    # path('student_detail/<int:id>/update_marks/<int:marks_id>/', views.update_marks, name='update_marks'),
    # path('student_detail/<int:id>/delete_marks/<int:marks_id>/', views.delete_marks, name='delete_marks'),
    # path('student_detail/<int:id>/generate_pdf/', views.generate_pdf, name='generate_pdf'),
    # path('student_detail/<int:id>/generate_pdf/<int:marks_id>/', views.generate_pdf, name='generate_pdf'),
]
