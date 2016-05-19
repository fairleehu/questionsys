from django import forms
from indata.models import Indata

class IndataForm(forms.ModelForm):
    isubject = forms.CharField(max_length=128)

    isection = forms.CharField(max_length=128)

    itype = forms.CharField(max_length=128)

    ikeyword = forms.CharField(max_length=128)

    ipoints = forms.CharField(max_length=256)

    ilevel = forms.CharField(max_length=128)

    iquestion = forms.CharField(max_length=1024)

    iselect = forms.CharField(max_length=128)

    ianswer = forms.CharField(max_length=1024)

    iexplain = forms.CharField(max_length=1024)


    #ifile = forms.FileField()

    class Meta:
        model = Indata
        fields = ('isubject', 'isection', 'itype', 'ikeyword', 'ipoints', 'ilevel', 'iquestion', 'iselect', 'ianswer','iexplain')
