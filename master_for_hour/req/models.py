from django.db import models
from accounts.models import Profiles
from services.models import Services

class RepairRequests(models.Model):
    request_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Profiles, models.DO_NOTHING)
    service = models.ForeignKey(Services, models.DO_NOTHING)
    description = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=255)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    assigned_master = models.ForeignKey(Profiles, models.DO_NOTHING, related_name='assigned_requests', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_requests'

class RequestUpdates(models.Model):
    update_id = models.AutoField(primary_key=True)
    request = models.ForeignKey(RepairRequests, models.DO_NOTHING)
    updated_by = models.ForeignKey(Profiles, models.DO_NOTHING, db_column='updated_by')
    old_status = models.CharField(max_length=20, blank=True, null=True)
    new_status = models.CharField(max_length=20, blank=True, null=True)
    note = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_updates'

class MasterAvailability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    master = models.ForeignKey(Profiles, models.DO_NOTHING)
    is_available = models.BooleanField(blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_availability'

class Notifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profiles, models.DO_NOTHING)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'