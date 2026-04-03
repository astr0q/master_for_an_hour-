from django.db import models

# Create your models here.
class Profiles(models.Model):
    profile_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=250)
    phone = models.IntegerField(blank=True, null=True)
    role = models.CharField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'