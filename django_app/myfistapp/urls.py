from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home,name='home'),
   path('about/',views.about, name='about'),
   path('contact/',views.contact_us, name='contact'),
   path('update/',views.update_table,name='update'),
   path('insertdata/',views.insert_data,name='insertdata'),
   path('display/',views.retrieve_data,name='display'),
   path('delete/',views.delete_data, name='delete'),
   path('update1/', views.update_salary,name='update1'),
]
