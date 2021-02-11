from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView 
from django.contrib.auth.decorators import user_passes_test

from rest_framework.views import APIView 
from rest_framework.response import Response 



def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    usern = request.user.username
    doctor1 = Doctor.objects.get(username=usern)
    patients = Patient.objects.filter(doctor=doctor1)
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.filter(doctor=doctor1)

    d = 0
    p = 0
    a = 0

    for i in doctors:
        d += 1
    for e in patients:
        p += 1
    for o in appointments:
        a += 1
    d1 = {'d': d, 'p': p, 'a': a}
    return render(request, 'index.html', d1)


def IndexAdmin(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    d = 0
    p = 0
    a = 0

    for i in doctors:
        d += 1
    for e in patients:
        p += 1
    for o in appointments:
        a += 1
    d1 = {'d': d, 'p': p, 'a': a}
    return render(request, 'indexAdmin.html', d1)

def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"

        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    d = {'doctor': doctor}
    return render(request, 'view_doctor.html', d)

def View_doctors_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.all()
    d = {'doctor': doctor}
    return render(request, 'view_doctors_admin.html', d)


def Add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST["name"]
        m = request.POST["mobile"]
        s = request.POST["specialization"]
        try:
            Doctor.objects.create(name=n, mobile=m, specialization=s)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_doctor.html', d)

def Delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def View_patients(request):
    if not request.user.is_staff:
        return redirect('login')
    usern = request.user.username
    doctor1 = Doctor.objects.get(username=usern)
    patient = Patient.objects.filter(doctor=doctor1)
    p = {'patient': patient}
    return render(request, 'view_patients.html', p)

def View_patients_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.all()
    p = {'patient': patient}
    return render(request, 'view_patients_admin.html', p)

def Add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    usern = request.user.username
    doctor1 = Doctor.objects.get(username=usern)
    if request.method == 'POST':
        n = request.POST["name"]
        g = request.POST["gender"]
        m = request.POST["mobile"]
        a = request.POST["address"]
        c = request.POST["condition"]
        ag = request.POST["age"]
        w = request.POST["weight"]
        h = request.POST["height"]
        i = request.POST["imc"]
        s = request.POST["smoker"]
        me = request.POST["medication"]
        doc = doctor1
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a, condition=c, age=ag, weight=w, height=h, imc=i, smoker=s, medication=me, doctor=doc) 
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_patient.html', d)

def Add_patient_admin(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    doctor1 = Doctor.objects.all()
    if request.method == 'POST':
        n = request.POST["name"]
        g = request.POST["gender"]
        m = request.POST["mobile"]
        a = request.POST["address"]
        c = request.POST["condition"]
        ag = request.POST["age"]
        w = request.POST["weight"]
        h = request.POST["height"]
        i = request.POST["imc"]
        s = request.POST["smoker"]
        me = request.POST["medication"]
        doc = request.POST["doctor"]
        doctor = Doctor.objects.filter(name=doc).first()
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a, condition=c, age=ag, weight=w, height=h, imc=i, smoker=s, medication=me, doctor=doctor) 
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'doctor':doctor1}
    return render(request, 'add_patient_admin.html', d)

def Edit_patient_general(request, pid):

    patient = Patient.objects.get(id=pid)
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        patient.name = request.POST["name"]
        patient.gender = request.POST["gender"]
        patient.mobile = request.POST["mobile"]
        patient.address= request.POST["address"]
        patient.condition= request.POST["condition"]
        patient.age= request.POST["age"]
        patient.weight= request.POST["weight"]
        patient.height= request.POST["height"]
        patient.imc= request.POST["imc"]
        patient.smoker= request.POST["smoker"]
        patient.medication=request.POST["medication"]
        
        try:
            patient.save(update_fields=['name','gender','mobile','address', 'condition', 'age', 'weight', 'height', 'imc','smoker','medication'])
            error = "no"
        except:
            error = "yes"
    p = {'patient': patient, 'error': error}
    return render(request, 'edit_patient_general.html', p)

def Edit_clinical_data(request, cid):

    clinical_data=Clinical_Data.objects.get(id=cid)
    patient = clinical_data.patient
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        clinical_data.annArbour = request.POST["annArbour"]
        clinical_data.ecog = request.POST["ecog"]
        clinical_data.pet = request.POST["pet"]
        clinical_data.tac= request.POST["tac"]
        clinical_data.ipi= request.POST["ipi"]
        clinical_data.immunophenotyping= request.POST["immunophenotyping"]
        clinical_data.biopsy= request.POST["biopsy"]
        clinical_data.hemoglobin= request.POST["hemoglobin"]
        clinical_data.ldh= request.POST["ldh"]
        clinical_data.microglobulin= request.POST["microglobulin"]
        clinical_data.patient=patient
        
        try:
            clinical_data.save(update_fields=['annArbour','ecog','pet','tac', 'ipi', 'immunophenotyping', 'biopsy', 'hemoglobin', 'ldh','microglobulin','patient'])
            error = "no"
        except:
            error = "yes"
    d = {'clinical_data': clinical_data, 'patient':patient, 'error': error}
    return render(request, 'edit_clinical_data.html', d)

def Edit_radiotherapy(request, rid):

    radiotherapy=RadiotherapyData.objects.get(id=rid)
    patient = radiotherapy.patient
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        radiotherapy.date = request.POST["date"]
        radiotherapy.location = request.POST["location"]
        radiotherapy.radiation = request.POST["radiation"]
        radiotherapy.intensity = request.POST["intensity"]
        radiotherapy.frequency = request.POST["frequency"]
        radiotherapy.patient=patient
        
        try:
            radiotherapy.save(update_fields=['date','location','radiation','intensity', 'frequency','patient'])
            error = "no"
        except:
            error = "yes"
    d = {'radiotherapy': radiotherapy, 'patient':patient, 'error': error}
    return render(request, 'edit_radiotherapy.html', d)

def Add_clinical_data(request, pid):

    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        aa = request.POST["annArbour"]
        e = request.POST["ecog"]
        pet = request.POST["pet"]
        tac = request.POST["tac"]
        ipi = request.POST["ipi"]
        im = request.POST["immunophenotyping"]
        b = request.POST["biopsy"]
        h = request.POST["hemoglobin"]
        ldh = request.POST["ldh"]
        m = request.POST["microglobulin"]
        p = patient

        try:
            Clinical_Data.objects.create(annArbour=aa, ecog=e, pet=pet, tac=tac,  ipi=ipi, immunophenotyping=im, 
            biopsy=b, hemoglobin=h, ldh=ldh, microglobulin=m,patient=p)
            error = "no"
        except:
            error = "yes"
    d = {'patient':patient,'error': error}
    return render(request, 'add_clinical_data.html', d)

def Add_radiotherapy(request, pid):

    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        d = request.POST["date"]
        l = request.POST["location"]
        r = request.POST["radiation"]
        i = request.POST["intensity"]
        f = request.POST["frequency"]
        p = patient

        try:
            RadiotherapyData.objects.create(date=d,location=l,radiation=r,intensity=i,frequency=f,patient=p)
            error = "no"
        except:
            error = "yes"
    a = {'patient':patient,'error': error}
    return render(request, 'add_radiotherapy.html', a)

def Add_chemotherapy(request, pid):

    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        c = request.POST["cycle"]
        d1 = request.POST["dateBeg"]
        d2 = request.POST["dateEnd"]
        s = request.POST["scheme"]
        p = patient

        try:
            ChemotherapyData.objects.create(cycle=c,dateBeg=d1,dateEnd=d2,scheme=s,patient=p)
            error = "no"
        except:
            error = "yes"
    a = {'patient':patient,'error': error}
    return render(request, 'add_chemotherapy.html', a)

def Add_questionnaire_sf36(request, pid):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        n = request.POST["evaluationMoment"]
        fc = request.POST["functional_capacity"]
        pl = request.POST["physical_limitations"]
        pa = request.POST["pain"]
        oh = request.POST["overall_health"]
        v = request.POST["vitality"]
        sa = request.POST["social_aspects"]
        ea = request.POST["emotional_aspects"]
        mh = request.POST["mental_health"]
        p = patient

        try:
            SF_36.objects.create(evaluationMoment=n, functional_capacity=fc, physical_limitations=pl, pain=pa,  overall_health=oh, vitality=v, 
            social_aspects=sa, emotional_aspects=ea, mental_health=mh, patient=p)
            error = "no"
        except:
            error = "yes"
    d = {'patient':patient,'error': error}
    return render(request, 'add_questionnaire_sf36.html', d)

def Add_questionnaire_factlym(request, pid):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        n = request.POST["evaluationMoment"]
        ph = request.POST["physical"]
        sf = request.POST["social_family"]
        e = request.POST["emotional"]
        f = request.POST["functional"]
        l = request.POST["lymphoma"]
        t = request.POST["toi"]
        fg = request.POST["fact_g"]
        fl = request.POST["fact_lym"]
        p = patient

        try:
            Fact_lym.objects.create(evaluationMoment=n, physical=ph, social_family=sf, emotional=e,  functional=f, lymphoma=l, 
            toi=t, fact_g=fg, fact_lym=fl, patient=p)
            error = "no"
        except:
            error = "yes"
    d = {'patient':patient,'error': error}
    return render(request, 'add_questionnaire_factlym.html', d)

def Add_hrv_data(request, pid):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        c = request.POST["cycle"]
        r = request.POST["rmssd"]
        s = request.POST["sdnn"]
        p = patient

        try:
            HrvData.objects.create(cycle=c, rmssd=r, sdnn=s, patient=p)
            error = "no"
        except:
            error = "yes"
    d = {'patient':patient,'error': error}
    return render(request, 'add_hrv_data.html', d)

def Add_sleep_data(request, pid):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        cy = request.POST["cycle"]
        du = request.POST["duration"]
        e = request.POST["eficency"]
        t = request.POST["timesWake"]
        c = request.POST["calories"]
        h = request.POST["hrvSleep"]
        p = patient

        try:
            SleepData.objects.create(cycle=cy, duration=du, eficency=e, timesWake=t, calories=c, hrvSleep=h, patient=p)
            error = "no"
        except:
            error = "yes"

    d = {'patient':patient,'error': error}
    return render(request, 'add_sleep_data.html', d)

def Add_physical_activity_data(request, pid):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    if request.method == 'POST':
        c = request.POST["cycle"]
        s = request.POST["stepsDay"]
        di = request.POST["distance"]
        st = request.POST["sedentaryTime"]
        sh = request.POST["sedentaryHRV"]
        sc = request.POST["sedentaryCalories"]
        lt = request.POST["lightTime"]
        lh = request.POST["lightHRV"]
        lc = request.POST["lightCalories"]
        mt = request.POST["moderateTime"]
        mh = request.POST["moderateHRV"]
        mc = request.POST["moderateCalories"]
        p = patient

        try:
            PhysicalActivityData.objects.create(cycle=c, stepsDay=s, distance=di, sedentaryTime=st, sedentaryHRV=sh, sedentaryCalories=sc, 
            lightTime=lt,lightHRV=lh,lightCalories=lc,moderateTime=mt,moderateHRV=mh,moderateCalories=mc,
            patient=p)
            error = "no"
        except:
            error = "yes"

    d = {'patient':patient,'error': error}
    return render(request, 'add_physical_activity_data.html', d)

   

def Delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patients')

def Delete_sf36(request,sid):
    if not request.user.is_staff:
        return redirect('login')
    sf_36 = SF_36.objects.get(id=sid)
    patient = sf_36.patient
    sf_36.delete()
    return redirect( 'sf_36', pid=patient.id)

def Delete_factlym(request,fid):
    if not request.user.is_staff:
        return redirect('login')
    factlym = Fact_lym.objects.get(id=fid)
    patient = factlym.patient
    factlym.delete()
    return redirect( 'facit', pid=patient.id)

def Delete_chemotherapy(request,cid):
    if not request.user.is_staff:
        return redirect('login')
    chemotherapy = ChemotherapyData.objects.get(id=fid)
    patient = chemotherapy.patient
    chemotherapy.delete()
    return redirect( 'chemotherapy', pid=patient.id)

def Delete_hrvData(request,hid):
    if not request.user.is_staff:
        return redirect('login')
    hrvData = HrvData.objects.get(id=hid)
    patient = hrvData.patient
    hrvData.delete()
    return redirect( 'hrv_data', pid=patient.id)

def Delete_sleepData(request,sid):
    if not request.user.is_staff:
        return redirect('login')
    sleepData = SleepData.objects.get(id=sid)
    patient = sleepData.patient
    sleepData.delete()
    return redirect( 'sleep_data', pid=patient.id)

def Delete_physicalActivityData(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    physicalActivityData = PhysicalActiviyData.objects.get(id=pid)
    patient = physicalActivityData.patient
    physicalActivityData.delete()
    return redirect( 'physical_activity_data', pid=patient.id)

def View_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    usern = request.user.username
    doctor1 = Doctor.objects.get(username=usern)
    appointment = Appointment.objects.filter(doctor=doctor1)
    a = {'appointment': appointment}
    return render(request, 'view_appointment.html', a)

def View_appointments_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    a = {'appointment': appointment}
    return render(request, 'view_appointments_admin.html', a)



def Add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    usern = request.user.username
    doctor1 = Doctor.objects.get(username=usern)
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = doctor1
        p = request.POST["patient"]
        d1 = request.POST["date"]
        t1 = request.POST["time"]
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=d, patient=patient, date1=d1, time1=t1)
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error }
    return render(request, 'add_appointment.html', d)

def Add_appointment_admin(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        d = request.POST["doctor"]
        p = request.POST["patient"]
        d1 = request.POST["date"]
        t1 = request.POST["time"]
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t1)
            error = "no"
        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error }
    return render(request, 'add_appointment_admin.html', d)


def Delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')

def View_patient_general(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    p = {'patient': patient}
    return render(request, 'view_patient_general.html', p)

def Clinical_data(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    if not Clinical_Data.objects.filter(patient=patient).exists():
        error = "yes"
        p = {'patient': patient, 'error':error}
    else:
        clinical_data= Clinical_Data.objects.get(patient=patient)
        error = "no"
        p = {'patient': patient, 'clinical_data':clinical_data, 'error':error}  
    return render(request, 'clinical_data.html', p)

def Radiotherapy(request, pid):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    if not RadiotherapyData.objects.filter(patient=patient).exists():
        error = "yes"
        p = {'patient': patient, 'error':error}
    else:
        radiotherapy= RadiotherapyData.objects.get(patient=patient)
        error = "no"
        p = {'patient': patient, 'radiotherapy':radiotherapy, 'error':error}  
    return render(request, 'radiotherapy.html', p)

def Chemotherapy(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    chemotherapy = ChemotherapyData.objects.all()
    p = {'patient': patient, 'chemotherapy':chemotherapy}
    return render(request, 'chemotherapy.html', p)

def Questionnaires(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    p = {'patient': patient}
    return render(request, 'questionnaires.html', p)

def Sf_36(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    p = {'patient': patient}
    return render(request, 'sf_36.html', p)

def Sf_36table(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    sf_36 = SF_36.objects.all().filter(patient=patient)
    count = sf_36.count()
    if not count > 1:
        d = {'patient': patient, 'sf_36':sf_36}
        return render(request, 'sf_36table.html', d)
    first = SF_36.objects.filter(patient=patient).first()
    last = SF_36.objects.filter(patient=patient).last()
    sfTemp=sf_36.exclude(id=first.id)
    sfTemp2=sf_36.exclude(id=last.id)

    zipped=zip(sfTemp2, sfTemp)
  
    d = {'patient': patient, 'sf_36':sf_36, 'zipped':zipped}
    return render(request, 'sf_36table.html', d)

def Sf_36chart(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    sf_36 = SF_36.objects.all().filter(patient=patient)



    labels = []
    functional = []
    physical = []
    pain = []
    overall = []
    vitality = []
    social = []
    emotional = []
    mental=[]

    for i in sf_36:
            
        labels.append(i.evaluationMoment)
        functional.append(i.functional_capacity)
        physical.append(i.physical_limitations)
        pain.append(i.pain)
        overall.append(i.overall_health)
        vitality.append(i.vitality)
        social.append(i.social_aspects)
        emotional.append(i.emotional_aspects)
        mental.append(i.mental_health)

    
  
    d = {'patient': patient, 'sf_36':sf_36, 'labels':labels, 'functional':functional, 'physical':physical, 'pain':pain, 
    'overall':overall, 'vitality':vitality, 'social':social, 'emotional':emotional, 'mental':mental}
    return render(request, 'sf_36chart.html', d)


def Facit(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    p = {'patient': patient}
    return render(request, 'facit.html', p)

def FactTable(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    fact_lym = Fact_lym.objects.all().filter(patient=patient)
    count = fact_lym.count()
    if not count > 1:
        d = {'patient': patient, 'fact_lym':fact_lym}
        return render(request, 'factTable.html', d)
    first = Fact_lym.objects.filter(patient=patient).first()
    last = Fact_lym.objects.filter(patient=patient).last()
    sfTemp=fact_lym.exclude(id=first.id)
    sfTemp2=fact_lym.exclude(id=last.id)
    zipped=zip(sfTemp2, sfTemp)

    d = {'patient': patient, 'fact_lym':fact_lym, 'zipped':zipped, }
    return render(request, 'factTable.html', d)

def FactChart(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    fact_lym = Fact_lym.objects.all().filter(patient=patient)
    labels = []
    physical = []
    social_family = []
    emotional = []
    functional = []
    lymphoma = []
    toi = []
    fact_g = []
    fact_l = []

    for i in fact_lym:
            
        labels.append(i.evaluationMoment)
        physical.append(i.physical)
        social_family.append(i.social_family)
        emotional.append(i.emotional)
        functional.append(i.functional)
        lymphoma.append(i.lymphoma)
        toi.append(i.toi)
        fact_g.append(i.fact_g)
        fact_l.append(i.fact_lym)

    d = {'patient': patient, 'fact_lym':fact_lym, 'labels':labels, 'physical':physical, 'social_family':social_family, 'emotional':emotional, 
    'functional':functional, 'lymphoma':lymphoma, 'toi':toi, 'fact_g':fact_g, 'fact_l':fact_l}

    return render(request, 'factChart.html', d)
def Biometric_data(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    p = {'patient': patient}
    return render(request, 'biometric_data.html', p)

def Hrv_data(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    hrvData = HrvData.objects.all().filter(patient=patient)

    labels = []
    rmssd = []
    sdnn = []

    for i in hrvData:
            
        labels.append(i.cycle)
        rmssd.append(i.rmssd)
        sdnn.append(i.sdnn)

    p = {'patient': patient, 'hrvData':hrvData, 'labels':labels, 'rmssd':rmssd, 'sdnn':sdnn}
    return render(request, 'hrv_data.html', p)


def Sleep_data(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    sleepData = SleepData.objects.all().filter(patient=patient)
    labels = []
    duration = []
    eficency = []
    timesAwake = []
    calories = []
    hrv = []

    for i in sleepData:
            
        labels.append(i.cycle)
        duration.append(i.duration)
        eficency.append(i.eficency)
        timesAwake.append(i.timesWake)
        calories.append(i.calories)
        hrv.append(i.hrvSleep)

    p = {'patient': patient, 'sleepData':sleepData, 'labels':labels, 'duration':duration, 'eficency':eficency, 
    'timesAwake':timesAwake, 'calories':calories, 'hrv':hrv }
    return render(request, 'sleep_data.html', p)


def Physical_activity_data(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    physicalActivityData = PhysicalActivityData.objects.all().filter(patient=patient)
    labels = []
    stepsDay = []
    distance = []
    timeS = []
    timeL = []
    timeM = []

    for i in physicalActivityData:
            
        labels.append(i.cycle)
        stepsDay.append(i.stepsDay)
        distance.append(i.distance)
        timeS.append(i.sedentaryTime)
        timeL.append(i.lightTime)
        timeM.append(i.moderateTime)

    p = {'patient': patient, 'physicalActivityData':physicalActivityData, 'labels':labels, 'stepsDay':stepsDay,
    'distance':distance, 'timeS':timeS, 'timeL':timeL, 'timeM':timeM, }
    return render(request, 'physical_activity_data.html', p)



def Sedentary_activity(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    sedentary = PhysicalActivityData.objects.all().filter(patient=patient)
    labels = []
    times = []
    hrv = []
    calories = []
   

    for i in sedentary:
            
        labels.append(i.cycle)
        times.append(i.sedentaryTime)
        hrv.append(i.sedentaryHRV)
        calories.append(i.sedentaryCalories)

    p = {'patient': patient, 'sedentary':sedentary, 'labels':labels, 'times':times, 'hrv':hrv, 'calories':calories}
    return render(request, 'sedentary_activity.html', p)


def Light_activity(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    light = PhysicalActivityData.objects.all().filter(patient=patient)
    labels = []
    times = []
    hrv = []
    calories = []
   

    for i in light:
            
        labels.append(i.cycle)
        times.append(i.lightTime)
        hrv.append(i.lightHRV)
        calories.append(i.lightCalories)
        

    p = {'patient': patient, 'labels':labels, 'times':times, 'hrv':hrv, 'calories':calories, 'light':light}
    return render(request, 'light_activity.html', p)


def Moderate_activity(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    moderate = PhysicalActivityData.objects.all().filter(patient=patient)
    labels = []
    times = []
    hrv = []
    calories = []
   

    for i in moderate:
            
        labels.append(i.cycle)
        times.append(i.moderateTime)
        hrv.append(i.moderateHRV)
        calories.append(i.moderateCalories)
        

    p = {'patient': patient, 'labels':labels, 'times':times, 'hrv':hrv, 'calories':calories, 'moderate':moderate}
    return render(request, 'moderate_activity.html', p)


def Qdvrs_total(request, pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    p = {'patient': patient}
    return render(request, 'qdvrs_total.html', p)

