# coding=utf-8
from django.db import models

# 试题类


class Indata(models.Model):
    isubject = models.CharField(max_length=128)

    isection = models.CharField(max_length=128)

    ichapter = models.CharField(max_length=128)

    itype = models.CharField(max_length=128)

    ikeyword = models.CharField(max_length=128)

    ipoints = models.CharField(max_length=256)

    ilevel = models.CharField(max_length=128)

    iquestion = models.TextField()

    iselect = models.CharField(max_length=128)

    ianswer = models.TextField()

    iexplain = models.TextField()

    #ifile = models.FileField(upload_to='upload', blank=True)

    def __unicode__(self):
        return self.ikeyword


# 科目类
class Subject(models.Model):
    subname = models.CharField(max_length=20, verbose_name=u"科目名称")

    def __unicode__(self):
        return self.subname

# 阶段类


class Section(models.Model):
    secsubject = models.ForeignKey(Subject)
    secname = models.CharField(max_length=24, verbose_name=u"阶段名称")

    def __unicode__(self):
        return self.secname

# 章节类


class Chapter(models.Model):
    chasection = models.ForeignKey(Section)
    chaname = models.CharField(max_length=24, verbose_name=u"章节名称")

    def __unicode__(self):
        return self.chaname
