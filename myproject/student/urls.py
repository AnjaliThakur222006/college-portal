from django.urls import path
from . import View


urlpatterns = [

    path('', View.home, name='home'),

    path('about/', View.about, name='about'),

    path('contact/', View.contact, name='contact'),


    # Student CRUD

    path('student/', View.student, name='student'),

    path('view_student/<int:id>/', View.view_student, name='view_student'),

    path('add_student/', View.add_student, name='add_student'),
    

    





   
   
   
   
   
   
   
   
   
   
   
   

    path('update_student/<int:id>/', View.update_student, name='update_student'),

    path('delete_student/<int:id>/', View.delete_student, name='delete_student'),



    # Course CRUD

    path('course/', View.course, name='course'),

    path('add_course/', View.add_course, name='add_course'),

    path('update_course/<int:id>/', View.update_course, name='update_course'),

    path('delete_course/<int:id>/', View.delete_course, name='delete_course'),

]