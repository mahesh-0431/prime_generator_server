from django.db import models

class PrimeExecution(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    start = models.IntegerField()
    end = models.IntegerField()
    elapsed = models.FloatField()
    algorithm = models.CharField(max_length=20)
    num_primes = models.IntegerField()
