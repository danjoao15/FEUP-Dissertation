from django.db import models

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    mobile=models.IntegerField()
    specialization=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=150)
    condition = models.CharField(max_length=150)
    age = models.IntegerField(null=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    imc = models.CharField(max_length=10, null=True, blank=True)
    smoker = models.CharField(max_length=10, null=True, blank=True)
    medication = models.CharField(max_length=10, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   
  

    def __str__(self):
        return self.name

class Clinical_Data(models.Model):
    annArbour = models.CharField(max_length=10, null=True, blank=True)
    ecog = models.CharField(max_length=10, null=True, blank=True)
    pet = models.CharField(max_length=10, null=True, blank=True)
    tac = models.CharField(max_length=10, null=True, blank=True)
    ipi = models.CharField(max_length=10, null=True, blank=True)
    immunophenotyping = models.CharField(max_length=10, null=True, blank=True)
    biopsy = models.CharField(max_length=10, null=True, blank=True)
    hemoglobin = models.CharField(max_length=10, null=True, blank=True)
    ldh = models.CharField(max_length=10, null=True, blank=True)
    microglobulin = models.CharField(max_length=10, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.annArbour+"--"+self.patient.name

class ChemotherapyData(models.Model):
    cycle = models.CharField(max_length=10, null=True, blank=True)
    dateBeg = models.CharField(max_length=10, null=True, blank=True)
    dateEnd = models.CharField(max_length=20, null=True, blank=True)
    scheme = models.CharField(max_length=20, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.cycle+"--"+self.patient.name

class RadiotherapyData(models.Model):
    date = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    radiation = models.CharField(max_length=20, null=True, blank=True)
    intensity = models.CharField(max_length=20, null=True, blank=True)
    frequency = models.CharField(max_length=20, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.location+"--"+self.patient.name


class SF_36 (models.Model):
    evaluationMoment = models.CharField(max_length=150)
    functional_capacity =models.IntegerField(null=True)
    physical_limitations = models.IntegerField(null=True)
    pain = models.IntegerField(null=True)
    overall_health =models.IntegerField(null=True)
    vitality = models.IntegerField(null=True)
    social_aspects = models.IntegerField(null=True)
    emotional_aspects = models.IntegerField(null=True)
    mental_health= models.IntegerField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.evaluationMoment


class Fact_lym (models.Model):
    evaluationMoment = models.CharField(max_length=150)
    physical =models.IntegerField(null=True)
    social_family = models.IntegerField(null=True)
    emotional = models.IntegerField(null=True)
    functional =models.IntegerField(null=True)
    lymphoma = models.IntegerField(null=True)
    toi = models.IntegerField(null=True)
    fact_g = models.IntegerField(null=True)
    fact_lym= models.IntegerField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.evaluationMoment

class HrvData (models.Model):
    cycle = models.CharField(max_length=150)
    rmssd =models.FloatField(null=True)
    sdnn = models.FloatField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cycle

class SleepData (models.Model):
    cycle = models.CharField(max_length=150)
    duration = models.FloatField(null=True)
    eficency =models.FloatField(null=True)
    timesWake = models.FloatField(null=True)
    calories = models.FloatField(null=True)
    hrvSleep = models.FloatField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cycle

class PhysicalActivityData (models.Model):
    cycle = models.CharField(max_length=150)
    stepsDay = models.FloatField(null=True)
    distance = models.FloatField(null=True)
    sedentaryTime =models.FloatField(null=True)
    sedentaryHRV  = models.FloatField(null=True)
    sedentaryCalories =models.FloatField(null=True)
    lightTime  = models.FloatField(null=True)
    lightHRV  = models.FloatField(null=True)
    lightCalories =models.FloatField(null=True)
    moderateTime  = models.FloatField(null=True)
    moderateHRV  = models.FloatField(null=True)
    moderateCalories  = models.FloatField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cycle


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name