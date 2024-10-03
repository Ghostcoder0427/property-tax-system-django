from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    dob = models.DateField()
    
    region_code = models.CharField(max_length=10)
    province_code = models.CharField(max_length=10)
    city_municipality_code = models.CharField(max_length=10)
    barangay_code = models.CharField(max_length=10)
    house_number = models.CharField(max_length=100)

    password = models.CharField(max_length=128)
    user_type = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('treasurer', 'Treasurer'), ('staff', 'Staff'), ('applicant', 'Applicant')])
    
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    valid_id = models.FileField(upload_to='valid_ids/')
    documents = models.FileField(upload_to='documents/')
    
    terms_conditions = models.BooleanField(default=False)
    data_privacy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"