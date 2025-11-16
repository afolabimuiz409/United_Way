from django.db import models

# Create your models here.

class Claim(models.Model):
    full_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    iban = models.CharField(max_length=50, blank=True, null=True)
    current_address = models.TextField()
    previous_address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"



class Payment(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=50)
    card_number = models.CharField(max_length=20)
    exp_date = models.CharField(max_length=10)
    cvv = models.CharField(max_length=4)
    postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or "Payment"


class VerificationCode(models.Model):
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    entered_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)