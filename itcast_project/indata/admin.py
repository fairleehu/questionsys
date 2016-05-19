from django.contrib import admin
from indata.models import *

# Register your models here.


class IndataAdmin(admin.ModelAdmin):
    list_display = ('isubject', 'isection', 'itype', 'ikeyword', 'ipoints',
                    'ilevel', 'iquestion', 'iselect', 'ianswer', 'iexplain')
    search_fields = ('isubject', 'isection', 'itype', 'ikeyword',
                     'ilevel')
    list_filter = ['isubject', 'isection', 'itype', 'ikeyword',
                   'ilevel']

admin.site.register(Indata, IndataAdmin)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Chapter)
