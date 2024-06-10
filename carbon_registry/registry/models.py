from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    project_type = models.CharField(max_length=50)
    date_registered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CarbonCredit(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.credit_amount} credits from {self.project.name}"
