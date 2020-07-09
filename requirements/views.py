from django.shortcuts import render
from django.views import generic
from django.forms import formset_factory
from django.shortcuts import redirect, RequestContext, render_to_response
from crispy_forms.layout import Submit
from requirements import forms
from requirements import models
from . import choices
from django.utils import timezone

# Create your views here.

class Requirements(generic.TemplateView):
    template_name = "requirements/requirements.html"
    http_method_names = ['get','post']

    def get(self, request, *args, **kwargs):

        if "requirement_form" not in kwargs:
            kwargs['requirement_form'] = forms.RequirementsForm()
            return super(Requirements,self).get(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):

        requirement_form = forms.RequirementsForm(request.POST)

        if not (requirement_form.is_valid()):
            return super(Requirements, self).get(request,requirement_form=requirement_form)

        producerName = requirement_form.cleaned_data['producerName']
        producerSponsor = requirement_form.cleaned_data['producerSponsor']
        producerPhone = requirement_form.cleaned_data['producerPhone']
        producerEmail = requirement_form.cleaned_data['producerEmail']
        requirement = requirement_form.save(commit=False)
        if producerName and producerPhone and producerName:
            producer = models.Producer(name=producerName,person=producerSponsor,phone=producerPhone, email=producerEmail)
            producer.save()
            requirement.producer = producer
        requirement.ini_date = timezone.now()
        requirement.numeroentrevistadores = requirement_form.cleaned_data['numeroentrevistadores'] 
        requirement.save()

        degrees = requirement_form.cleaned_data['degree']
        stand_type = requirement_form.cleaned_data['stand_type']
        entrevistadores = requirement_form.cleaned_data['numeroentrevistadores']
        tiempoentrevista = requirement_form.cleaned_data['tiempoxentrevista']
        tipoentrevista = requirement_form.cleaned_data['tipoentrevista']
        if entrevistadores and tiempoentrevista and tipoentrevista=="1":
            cupos = int(26*(15/tiempoentrevista)*entrevistadores)
        else:
            cupos = 52 #esto es para que omita la matriz si es que cambia el tipo de entrvista
        request.session['degrees'] = degrees
        request.session['cupos'] = cupos
        request.session['requirement_id'] = requirement.id
        return redirect("requirements:cupos")


class Exito(generic.TemplateView):
    template_name = 'requirements/exito.html'

def cupos(request):
    cupos = request.session['cupos']
    if cupos ==2:
        return redirect("requirements:exito")
    degrees = request.session['degrees']
    verb_degree = []
    for d in degrees:
        for choice in choices.DEGREE_CHOICES:
            if d == choice[0]:
                verb_degree.append(choice[1])

    CuposFormSet = formset_factory(forms.CuposForm, formset=forms.CuposFormSet, extra=len(verb_degree), max_num=15)

    if request.method == "POST":
        formset = CuposFormSet(request.POST,form_kwargs={'degrees' : verb_degree, 'cupos': cupos})
        helper = forms.CuposFormSetHelper()
        helper.template = 'requirements/table_inline_formset2.html'
        helper.add_input(Submit("submit", "Enviar y Terminar"))
        if not formset.is_valid():
            return render(request, "requirements/cupos.html",{'cupos_formset':formset, 'helper': helper, 'cupos': cupos})

        i=0
        for form in formset:
            if form.is_valid():
                degree = degrees[i]
                i+=1
                p1 = form.cleaned_data['practica1']
                p2 = form.cleaned_data['practica2']
                p3 = form.cleaned_data['practica3']
                memoria = form.cleaned_data['memoria']
                ft = form.cleaned_data['fulltime']
                pt = form.cleaned_data['partime']


                requirement_id = request.session['requirement_id']

                requirement = models.RequirementsCompanies.objects.get(id=requirement_id)

                if p1 and p1!=0:
                    p1_data = models.CuposCarrera(companie_requirement=requirement, degree=degree, tipo='P1', cupos=p1)
                    p1_data.save()
                if p2 and p2!=0:
                    p2_data = models.CuposCarrera(companie_requirement=requirement, degree=degree, tipo='P2', cupos=p2)
                    p2_data.save()
                if p3 and p3!=0:
                    p3_data = models.CuposCarrera(companie_requirement=requirement, degree=degree, tipo='P3', cupos=p3)
                    p3_data.save()
                if memoria and memoria!=0:
                    m_data = models.CuposCarrera(companie_requirement=requirement, degree=degree, tipo='ME', cupos=memoria)
                    m_data.save()
                if ft and ft!=0:
                    tr_data = models.CuposCarrera(companie_requirement=requirement, degree=degree, tipo='FT', cupos=ft)
                    tr_data.save()
                if pt and pt!=0:
                    pt_data = models.CuposCarrera(companie_requirement=requirement, degree=degree, tipo='PT', cupos=pt)
                    pt_data.save()

            else:
                return render(request, "requirements/cupos.html",{'cupos_formset':formset, 'helper': helper, 'cupos': cupos})

        return redirect("requirements:exito")
    else:
        formset = CuposFormSet(form_kwargs={'degrees' : verb_degree,'cupos': cupos})
        helper = forms.CuposFormSetHelper()
        helper.template = 'requirements/table_inline_formset2.html'
        helper.add_input(Submit("submit", "Guardar"))

        return render_to_response('requirements/cupos.html',{'cupos_formset': formset, 'helper': helper, 'cupos': cupos},
                      context_instance=RequestContext(request))

					
					
class RequirementsInvitadas(generic.TemplateView): #la idea aqui es omitir stand y preferencias, asi determinar cuales son invitadas 
    template_name = "requirements/requirements.html"
    http_method_names = ['get','post']

    def get(self, request, *args, **kwargs):

        if "requirement_form" not in kwargs:
            kwargs['requirement_form'] = forms.RequirementsFormInvitadas()
            return super(RequirementsInvitadas,self).get(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):

        requirement_form = forms.RequirementsFormInvitadas(request.POST)

        if not (requirement_form.is_valid()):
            return super(RequirementsInvitadas, self).get(request,requirement_form=requirement_form)

        #producerName = requirement_form.cleaned_data['producerName']
        #producerSponsor = requirement_form.cleaned_data['producerSponsor']
        #producerPhone = requirement_form.cleaned_data['producerPhone']
        #producerEmail = requirement_form.cleaned_data['producerEmail']
        requirement = requirement_form.save(commit=False)
      #  if producerName and producerPhone and producerName:
       #     producer = models.Producer(name=producerName,person=producerSponsor,phone=producerPhone, email=producerEmail)
        #    producer.save()
         #   requirement.producer = producer
        requirement.ini_date = timezone.now()
        requirement.numeroentrevistadores = requirement_form.cleaned_data['numeroentrevistadores'] 
        requirement.save()

        degrees = requirement_form.cleaned_data['degree']
        stand_type = requirement_form.cleaned_data['stand_type']
        entrevistadores = requirement_form.cleaned_data['numeroentrevistadores']
        tiempoentrevista = requirement_form.cleaned_data['tiempoxentrevista']
        tipoentrevista = requirement_form.cleaned_data['tipoentrevista']
        if entrevistadores and tiempoentrevista and tipoentrevista=="1":
            cupos = int(26*(15/tiempoentrevista)*entrevistadores)
        else:
            cupos = 2 #esto es para que omita la matriz si es que cambia el tipo de entrvista
        request.session['degrees'] = degrees
        request.session['cupos'] = cupos
        request.session['requirement_id'] = requirement.id
        return redirect("requirements:cupos")


