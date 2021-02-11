"""qv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cds.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('about/', About, name="about"),
    path('contact/', Contact, name="contact"),
    path('', Index, name="home"),
    path('homeAdmin', IndexAdmin, name="homeAdmin"),
    path('admin_login/', Login, name="login"),
    path('logout/', Logout_admin, name="logout"),
    path('view_doctor/', View_doctor, name="view_doctor"),
    path('view_doctors_admin/', View_doctors_admin, name="view_doctors_admin"),
    path('add_doctor/', Add_doctor, name="add_doctor"),
    path('delete_doctor(?P<int:pid>)', Delete_doctor, name="delete_doctor"),
    path('view_patients/', View_patients, name="view_patients"),
    path('view_patients_admin/', View_patients_admin, name="view_patients_admin"),
    path('view_patient_general(?P<int:pid>)/', View_patient_general, name="view_patient_general"),
    path('edit_patient_general(?P<int:pid>)/', Edit_patient_general, name="edit_patient_general"),
    path('clinical_data(?P<int:pid>)/', Clinical_data, name="clinical_data"),
    path('radiotherapy(?P<int:pid>)/', Radiotherapy, name="radiotherapy"),
    path('chemotherapy(?P<int:pid>)/', Chemotherapy, name="chemotherapy"),
    path('questionnaires(?P<int:pid>)/', Questionnaires, name="questionnaires"),
    path('sf_36(?P<int:pid>)/', Sf_36, name="sf_36"),
    path('sf_36table(?P<int:pid>)/', Sf_36table, name="sf_36table"),
    path('sf_36chart(?P<int:pid>)/', Sf_36chart, name="sf_36chart"),
    path('add_questionnaire_sf36(?P<int:pid>)/', Add_questionnaire_sf36, name="add_questionnaire_sf36"),
    path('add_questionnaire_factlym(?P<int:pid>)/', Add_questionnaire_factlym, name="add_questionnaire_factlym"),
    path('facit(?P<int:pid>)/', Facit, name="facit"),
    path('factTable(?P<int:pid>)/', FactTable, name="factTable"),
    path('factChart(?P<int:pid>)/', FactChart, name="factChart"),
    path('biometric_data(?P<int:pid>)/', Biometric_data, name="biometric_data"),
    path('hrv_data(?P<int:pid>)/', Hrv_data, name="hrv_data"),
    path('sleep_data(?P<int:pid>)/', Sleep_data, name="sleep_data"),
    path('physical_activity_data(?P<int:pid>)/', Physical_activity_data, name="physical_activity_data"),
    path('sedentary_activity(?P<int:pid>)/', Sedentary_activity, name="sedentary_activity"),
    path('light_activity(?P<int:pid>)/', Light_activity, name="light_activity"),
    path('moderate_activity(?P<int:pid>)/', Moderate_activity, name="moderate_activity"),
    path('qdvrs_total(?P<int:pid>)/', Qdvrs_total, name="qdvrs_total"),
    path('add_patient/', Add_patient, name="add_patient"),
    path('add_patient_admin/', Add_patient_admin, name="add_patient_admin"),
    path('delete_patient(?P<int:pid>)', Delete_patient, name="delete_patient"),
    path('delete_sf36(?P<int:sid>)', Delete_sf36, name="delete_sf36"),
    path('delete_factlym(?P<int:fid>)', Delete_factlym, name="delete_factlym"),
    path('view_appointment/', View_appointment, name="view_appointment"),
    path('view_appointments_admin/', View_appointments_admin, name="view_appointments_admin"),
    path('add_appointment/', Add_appointment, name="add_appointment"),
    path('add_appointment_admin/', Add_appointment_admin, name="add_appointment_admin"),
    path('delete_appointment(?P<int:pid>)/', Delete_appointment, name="delete_appointment"),
    path('add_clinical_data(?P<int:pid>)/', Add_clinical_data, name="add_clinical_data"),
    path('edit_clinical_data(?P<int:cid>)/', Edit_clinical_data, name="edit_clinical_data"),
    path('add_radiotherapy(?P<int:pid>)/', Add_radiotherapy, name="add_radiotherapy"),
    path('edit_radiotherapy(?P<int:rid>)/', Edit_radiotherapy, name="edit_radiotherapy"),
    path('add_chemotherapy(?P<int:pid>)/', Add_chemotherapy, name="add_chemotherapy"),
    path('add_hrv_data(?P<int:pid>)/', Add_hrv_data, name="add_hrv_data"),
    path('add_sleep_data(?P<int:pid>)/', Add_sleep_data, name="add_sleep_data"),
    path('add_physical_activity_data(?P<int:pid>)/', Add_physical_activity_data, name="add_physical_activity_data"),
    path('delete_chemotherapy(?P<int:cid>)', Delete_chemotherapy, name="delete_chemotherapy"),
    path('delete_hrvData(?P<int:hid>)', Delete_hrvData, name="delete_hrvData"),
    path('delete_sleepData(?P<int:sid>)', Delete_sleepData, name="delete_sleepData"),
    path('delete_physicalActivityData(?P<int:sid>)', Delete_physicalActivityData, name="delete_physicalActivityData"),

   
   
]
