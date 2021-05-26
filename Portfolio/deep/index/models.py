from django.db import models

# Create your models here.
class Project(models.Model):
    project_id=models.IntegerField(primary_key=True)
    project_description=models.CharField(max_length=100)
    project_name=models.CharField(max_length=100)
    project_status=models.IntegerField()

    def __str__(self):
        return self.project_name;
