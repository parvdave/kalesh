from django.db import models
import uuid

class Kalesh(models.Model):
    email_1 = models.EmailField()
    kaleshi_slug_1 = models.CharField(
        max_length=36,
        blank=True,
        default=uuid.uuid4,
        editable=False
    )
    kaleshi_slug_2 = models.CharField(
        max_length=36,
        blank=True,
        default=uuid.uuid4,
        editable=False
    )
    email_2 = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    response_count = models.PositiveIntegerField(default=0)
    resolution=models.TextField(blank=True)


    def __str__(self):
        return f"Kalesh between {self.email_1} and {self.email_2}"

class Kaleshi(models.Model):
    kalesh = models.ForeignKey(Kalesh, on_delete=models.CASCADE)  # ForeignKey referencing Kalesh model
    kaleshi_name = models.CharField(max_length=100,default="TBA")  # Name of the Kaleshi (fighter)
    kaleshi_email = models.EmailField()  # Email of the Kaleshi
    kaleshi_slug = models.CharField(
        max_length=36, 
        unique=True,
        editable=False
    )
    kaleshi_response = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Kaleshi {self.kaleshi_name} ({self.kaleshi_email})"