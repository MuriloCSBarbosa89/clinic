import pytest
from rest_framework.test import APIClient
from appointment.models import Appointment
from factories import DoctorFactory, PatientFactory

# Create your tests here.
@pytest.mark.django_db
def test_create_appointment():
    client = APIClient()
    doctor = DoctorFactory()
    patient = PatientFactory()

    payload = {
                "doctor": str(doctor.id),
                "patient": str(patient.id),
                "date": "2025-07-30",
                "time": "14:00:00"
            }
    
    response = client.post("/api/appointments/", payload, format="json")

    assert response.status_code == 201
