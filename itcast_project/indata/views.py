# coding=utf-8
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from indata.models import *
from django.core import serializers


def outdata(request):
    print "***** indata_views.py  outdata() *******"
    data_list = Indata.objects.all()
    data_dict = {'data_dic': data_list}
    return render(request, 'indata/outdata.html', data_dict)


def index(request):
    if request.method == 'POST':
        print "###### indata  views.py #######POST"
        isub_id = request.POST.get('isubject')
        print isub_id
        if(isub_id == '404'):
            return HttpResponseRedirect('/indata')

        isub = Subject.objects.filter(id=isub_id)
        isubject = ""
        for isub in isub:
            isubject = isub.subname
        isection = request.POST.get('isection')
        ichapter = request.POST.get('ichapter')
        itype = request.POST.get('itype')
        ikeyword = request.POST.get('ikeyword')
        ipoints = request.POST.get('ipoints')
        ilevel = request.POST.get('ilevel')
        iquestion = ""
        iselect = ""
        ianswer = ""
        iexplain = request.POST.get('iexplain')

        if(itype == u'单选'):
            iquestion = request.POST.get('q_danxuan')
            dan_A = request.POST.get('danxuan_A')
            dan_A = 'A.' + dan_A
            dan_B = request.POST.get('danxuan_B')
            dan_B = 'B.' + dan_B
            dan_C = request.POST.get('danxuan_C')
            dan_C = 'C.' + dan_C
            dan_D = request.POST.get('danxuan_D')
            dan_D = 'D.' + dan_D
            iselect = '~'.join((dan_A, dan_B, dan_C, dan_D))
            ianswer = request.POST.get('a_danxuan')
        if(itype == u'多选'):
            iquestion = request.POST.get('q_duoxuan')
            duo_A = request.POST.get('duoxuan_A')
            dan_A = 'A.' + dan_A
            duo_B = request.POST.get('duoxuan_B')
            dan_B = 'B.' + dan_B
            duo_C = request.POST.get('duoxuan_C')
            dan_C = 'C.' + dan_C
            duo_D = request.POST.get('duoxuan_D')
            dan_D = 'D.' + dan_D
            duo_E = request.POST.get('duoxuan_E')
            dan_E = 'E.' + dan_E
            duo_F = request.POST.get('duoxuan_F')
            dan_F = 'F.' + dan_F
            duo_G = request.POST.get('duoxuan_G')
            dan_G = 'G.' + dan_G

            sels = (duo_A, duo_B, duo_C, duo_D, duo_E, duo_F, duo_G)
            select = ""
            for i in sels:
                if(i != ""):
                    select = (select + i)
                else:
                    select = select

            iselect = '~'.join(select)
            if request.POST.has_key('a_duoxuan'):
                if request.POST['a_duoxuan']:
                    ianswer = ','.join(request.POST.getlist('a_duoxuan'))
            else:
                ianswer = ""

        if(itype == u'判断'):
            iquestion = request.POST.get('q_panduan')
            ianswer = request.POST.get('a_panduan')
        if(itype == u'填空'):
            iquestion = request.POST.get('q_tiankong')
            ianswer = request.POST.get('a_tiankong')
        if(itype == u'编程'):
            iquestion = request.POST.get('q_biancheng')
            ianswer = request.POST.get('a_biancheng')

        print "subject  >>>%s\nsection  >>>%s\nchapter >>>%s\ntype  >>>%s\nkeyword  >>>%s\npoints  >>>%s\nlevel  >>>%s\nquestion  >>>%s\nselect  >>>%s\nanswer  >>>%s\nexplain  >>>%s\n" % (isubject, isection, ichapter, itype, ikeyword, ipoints, ilevel, iquestion, iselect, ianswer, iexplain)

        Indata.objects.get_or_create(isubject=isubject, isection=isection, ichapter=ichapter, itype=itype, ikeyword=ikeyword, ipoints=ipoints,
                                     ilevel=ilevel, iquestion=iquestion, iselect=iselect, ianswer=ianswer, iexplain=iexplain)

        return HttpResponseRedirect('/indata')
    # else GET请求
    else:
        sub_list = Subject.objects.all()
        context_dict = {'sublist': sub_list}
        return render(request, 'indata/example.html', context_dict)


def choice_section(request):
    # print "*********** indata/views.py choice_section() **********"
    param = request.GET.get('sub_id')
    # print "***********  %s  ************" % (param)
    if param != 404:
        data = serializers.serialize(
            "json", Section.objects.filter(secsubject=param))
    else:
        data = {}
    return HttpResponse(data)


def choice_chapter(request):
    print "*********** indata/views.py choice_chapter() **********"
    param = request.GET.get('sec_id')
    param = Section.objects.get(secname=param)
    print "***********  %s  ************" % (param)
    if param != 404:
        print "123"
        data = serializers.serialize(
            "json", Chapter.objects.filter(chasection=param))
    else:
        data = {}
    return HttpResponse(data)
