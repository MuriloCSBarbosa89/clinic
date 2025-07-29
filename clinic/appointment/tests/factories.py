import factory
from core.models import Patient, Doctor


class DoctorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Doctor
    
    name = factory.Faker('name')


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    name = factory.Faker('name')
    birth_date = factory.Faker('date_of_birth')
