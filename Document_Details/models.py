from django.db import models

class Department(models.Model):
    depart_id = models.CharField(db_column='Depart_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    depart_name = models.CharField(db_column='Depart_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()
    
    class Meta:
        managed = False
        db_table = 'department'

class Document(models.Model):
    document_id = models.CharField(db_column='Document_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Employee_ID', blank=True, null=True)  # Field name made lowercase.
    document_type = models.CharField(db_column='Document_Type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    generation_date = models.DateField(db_column='Generation_Date', blank=True, null=True)  # Field name made lowercase.
    document_time = models.DateTimeField(db_column='Document_Time', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    depart = models.ForeignKey(Department, models.DO_NOTHING, db_column='Depart_ID', blank=True, null=True)  # Field name made lowercase.
    link = models.CharField(db_column='Link', max_length=250, blank=True, null=True)  # Field name made lowercase.


    objects = models.Manager()
    
    class Meta:
        managed = False
        db_table = 'document'


class Employee(models.Model):
    employee_id = models.CharField(db_column='Employee_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=20, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()
   
    class Meta:
        managed = False
        db_table = 'employee'


class Officers(models.Model):
    officers_id = models.CharField(db_column='Officers_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    officers_name = models.CharField(db_column='Officers_Name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    depart = models.ForeignKey(Department, models.DO_NOTHING, db_column='Depart_ID', blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    
    class Meta:
        managed = False
        db_table = 'officers'


class Status(models.Model):
    status_id = models.CharField(db_column='Status_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    status_name = models.CharField(db_column='Status_Name', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()


    class Meta:
        managed = False
        db_table = 'status'


class Tracking(models.Model):
    transaction_no = models.IntegerField(db_column='Transaction_no', primary_key=True)  # Field name made lowercase.
    document = models.ForeignKey(Document, models.DO_NOTHING, db_column='Document_ID', blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    forwarded_to = models.ForeignKey(Officers, models.DO_NOTHING, db_column='Forwarded_To', blank=True, null=True)  # Field name made lowercase.
    forwarded_by = models.ForeignKey(Officers, models.DO_NOTHING, db_column='Forwarded_By', related_name='tracking_forwarded_by_set', blank=True, null=True)  # Field name made lowercase.
    forwarded_date = models.DateField(db_column='Forwarded_Date', blank=True, null=True)  # Field name made lowercase.
    forwarded_time = models.DateTimeField(db_column='Forwarded_Time', blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey(Status, models.DO_NOTHING, db_column='Status_ID', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'tracking'
