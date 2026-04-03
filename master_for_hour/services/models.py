from django.db import models

# Create your models here.
class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True, null=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'