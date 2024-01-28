from django import forms 
from django.forms import ModelForm
from .models import information,archives


class formfile(ModelForm):
    class Meta:
        model=archives
        fields=["title","file","type","entity","tips"]
        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
            'file':forms.FileInput(attrs={'class':'form-control','id':'sel-file'}),
            'type':forms.Select(attrs={'class':'form-select','placeholder': 'type'}),
            'entity':forms.TextInput(attrs={'class':'form-control','placeholder': 'entity'}),
            'tips':forms.TextInput(attrs={'class':'form-control','placeholder': 'tips'}),
                  
        }
        labels={
            'title':"",
            'file':"",
            'type':"",
            'entity':"",
            'tips':""
        }

    
        

    

