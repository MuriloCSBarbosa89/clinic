from django.db import models

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey("core.Doctor", on_delete=models.CASCADE)
    patient = models.ForeignKey("core.Patient", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("doctor", "date", "time")
    
    def __str__(self):
        return  f"{self.date} {self.time} - {self.doctor} com {self.patient}"
