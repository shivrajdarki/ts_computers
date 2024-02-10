from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='service_photos/', null=True, blank=True)

    def __str__(self):
        return self.name

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='subservices')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.description}"

class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    subservice = models.ForeignKey(SubService, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.subservice.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
