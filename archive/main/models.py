from django.db import models



class information(models.Model):
     title= models.CharField(max_length=255)
     type  = models.CharField(max_length=255)
     entity =models.CharField(max_length=255)


class archives(models.Model):
     sel1='export'
     sel2='import'
     SEL_CHOICES=[
      (sel1,"export"),
      (sel2,"import")
      ]
     title= models.CharField(max_length=255)
     file =models.FileField(upload_to="file/",max_length=245)
     type  =models.CharField(max_length=10,blank=False, choices=SEL_CHOICES)
     entity =models.CharField(max_length=255)
     tips =models.CharField( max_length=225)
     

     
