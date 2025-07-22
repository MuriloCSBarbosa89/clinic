from django.contrib import admin
from core.models import Doctor, Patient


class DoctorAdmin(admin.ModelAdmin):
    pass

class PatientAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)