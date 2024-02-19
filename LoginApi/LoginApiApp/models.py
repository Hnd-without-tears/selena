from django.db import models

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
    
    
#     def __str__(self):
#         return self.titlepy 


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'