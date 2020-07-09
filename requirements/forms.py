from django import forms
from django.forms import BaseFormSet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Fieldset, Div, HTML
from crispy_forms.bootstrap import InlineCheckboxes
from requirements import models
from . import choices
from django.forms import formset_factory

class RequirementsForm(forms.ModelForm):
    error_css_class = 'error'
    degree = forms.MultipleChoiceField(choices=choices.DEGREE_CHOICES, label ="Carreras Requeridas")
    producerName = forms.CharField(max_length=50, label="Nombre productora", required=False)
    producerSponsor= forms.CharField(max_length=50, label="Persona de contacto de productora", required=False)
    producerPhone = forms.IntegerField(label="Telefono de persona de contacto",required=False)
    producerEmail = forms.CharField(max_length=50, label="Email de persona de contacto", required=False)

    def __init__(self, *args, **kwargs):
        super(RequirementsForm,self).__init__(*args,**kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.error_text_inline = True
        #self.fields['day_preference_1'].initial = '1'
        #self.fields['stand_type'].initial = '2'
        self.fields['stand_preference_2'].required = False
        self.fields['stand_preference_3'].required = False
        self.fields['day_preference_2'].required = False
        self.fields['day_preference_3'].required = False
        #self.fields['producerPhone'].required = False
        

        self.helper.layout = Layout(
            Field('companieName'),
            Field('companieDescription', placeholder="Ingrese una breve descripción de su compañia para ser utilizada en nuestra página web y en la difusión (5000 caracteres máximo)"),
            Field('representantename'),
            Field('representantecelular'),
            Field('representantecorreo'),
			
            Fieldset(
                'Día de Asistencia',
                Div('day_preference_1', css_class='col-md-4'), # borrados los dias de preferencia solo dejando la opcion de dia de asistencia
                Div('day_preference_2', css_class='col-md-4', style="display: none;"),
                Div('day_preference_3', css_class='col-md-4', style="display: none;"),
            ),

            Fieldset(
                "Tipo de Stand",
                Div('stand_type', css_class='col-md-6'),
                Div('require_stand', css_class='col-md-6')
            ),
			
            HTML("<fieldset><legend hidden id='producer_legend'>Datos de la productora que instalará su stand propio.</legend>"),
            Div('producerName', css_class ='col-md-4', id="div_producerName", style="display: none;"),
            Div('producerSponsor', css_class = 'col-md-4',id="div_producerSponsor", style="display: none;"),
            Div('producerPhone', css_class ='col-md-4',id="div_producerPhone", style="display: none;"),
            Div('producerEmail', css_class ='col-md-4',id="div_producerEmail", style="display: none;"),
            HTML("</fieldset>"),
			
            Fieldset(
                'Preferencia de Stand en Layout',
                HTML("<div><p> Para ver el layout de la Feria y los números de stand haga click en el siguiente botón: <button type='button' class='btn btn-primary btn-xs' data-toggle='modal' data-target='#Layout'>Ver Layout</button></p></div>"),
                Div('stand_preference_1', css_class ='col-md-4'),
                Div('stand_preference_2', css_class ='col-md-4'),
                Div('stand_preference_3', css_class ='col-md-4'),
            ),




			

            Fieldset(
                'Cantidad de Almuerzos',
		HTML("<p>Según el porte de su stand, tiene una cantidad máxima de entrevistadores y, por lo tanto, de almuerzos. Si desea agregar algún almuerzo extra, éste tendrá un costo adicional de 1UF.</br></br> La cantidad máxima de entrevistadores son las siguientes: </br> Stand 2x3: 2 almuerzos </br> Stand 3x3: 2 almuerzos  </br> Stand 4x3: 3 almuerzos </br> Stand 5x3: 4 almuerzos </br> Stand 6x3: 4 almuerzos </br> </br> A continuación, por favor indicar la cantidad de entrevistadores y de almuerzos normales y almuerzos vegetarianos para su empresa.</p>"),
				Div('numeroentrevistadores', css_class='col-md-8'),
				Div('lunch_number', css_class='col-md-6'),
				Div('veggie_lunch_number', css_class='col-md-6'),

            ),
            
            Fieldset(
                'Detalle de Entrevista',
		HTML("<p>Las entrevistas por defecto son individuales de 15 minutos. </br> Usted puede decidir otra dinámica de entrevistas, variando el tiempo o modalidad, lo cual tendrá un efecto en la cantidad de participantes que entrevistará al final del día. </br> Para esto, seleccione 'Otra Modalidad' en tipo de entrevista y contacte con su ejecutivo para la determinación de ésta."),

                Div('tipoentrevista', css_class='col-md-6'),
                Div('tiempoxentrevista', css_class='col-md-6', style="display: none;"),
            ),

            Fieldset(
                'Carreras',
		HTML("<p>Puede ver una descripción de las distintas carreras en el siguiente botón:  <a class='btn btn-primary btn-xs' href='http://www.feriaempresarial.cl/static/site/img/PerfilEspecialidades2018.pdf' target='_blank'>carreras</a>.</p>"),
                InlineCheckboxes('degree', template='requirements/checkboxselectmultiple_inline.html'),
            ),
            Submit('siguiente', 'Siguiente', css_class="btn-success")
        )


    def clean(self):
        cleaned_data = super(RequirementsForm,self).clean()
        stand_type = cleaned_data.get('stand_type')
        interviewers = cleaned_data.get('numeroentrevistadores')
        lunch_number = cleaned_data.get('lunch_number')
        veggie_lunch_number = cleaned_data.get('veggie_lunch_number')
        dp1 = cleaned_data.get('day_preference_1')
        st1 = cleaned_data.get('stand_preference_1')
        st2 = cleaned_data.get('stand_preference_2')
        st3 = cleaned_data.get('stand_preference_3')
        rs = cleaned_data.get('require_stand')
        pn = cleaned_data.get('producerName')
        pp = cleaned_data.get('producerPhone')
        pe = cleaned_data.get('producerEmail')
        
        total_lunch = lunch_number + veggie_lunch_number

        #if stand_type and total_lunch:
         #   if stand_type == "1" and total_lunch > 2:
          #      raise forms.ValidationError(
           #         "La cantidad de almuerzos totales no pueden ser mayor a 2"
            #    )
            #if stand_type == "2" and  total_lunch > 4:
             #   raise forms.ValidationError(
              #      "La cantidad de almuerzos totales no puede ser mayor a 4"
               # )

        if interviewers:
           
            if (stand_type == "1" or stand_type == "2") and interviewers > 2:
                raise forms.ValidationError(
                    "La cantidad de entrevistadores no puede superar a la permitida según stand"
                )
            if (stand_type == "4" or stand_type == "5") and interviewers > 4:
                raise forms.ValidationError(
                    "La cantidad de entrevistadores no puede superar a la permitida según stand"
                )
            if stand_type == "3" and interviewers > 3:
                raise forms.ValidationError(
                    "La cantidad de entrevistadores no puede superar a la permitida según stand"
                )
        if total_lunch:
            if (stand_type == "1" or stand_type == "2") and (lunch_number + veggie_lunch_number) < 2:
                raise forms.ValidationError(
                    "La cantidad de almuerzos es menor a la incluida según stand"
                )
            if (stand_type == "4" or stand_type == "5") and (lunch_number + veggie_lunch_number) < 4:
                raise forms.ValidationError(
                    "La cantidad de almuerzos es menor a la incluida según stand"
                )
            if stand_type == "3"  and (lunch_number + veggie_lunch_number) < 3:
                raise forms.ValidationError(
                    "La cantidad de almuerzos es menor a la incluida según stand"
                )
            if lunch_number <0 or veggie_lunch_number<0:
                raise forms.ValidationError(
                    "Los almuerzos no pueden ser negativos"
                )

        #if dp1 and dp2 and dp3:
         #   if dp1 == dp2 or dp1 == dp3 or dp2 == dp3:
          #      raise forms.ValidationError(
           #         "Los días de preferencia deben ser distintos entre sí"
            #    )

        if st1 and st2 and st3:
            if (st1 != 'A' and st1 != 'B'):
                if st1 == st2 or st1 == st3 or st2 == st3 :
                    raise forms.ValidationError(
                        "Los stands de preferencia deben ser distintos entre sí"
                    )

        if rs:
            if rs == "1" and (pn=="" or pp=="" or pe==""):
                raise forms.ValidationError(
                    "Debe ingresar los datos de productora"
                )


    class Meta:
        model = models.RequirementsCompanies
        fields = ['companieName', 'companieDescription','representantename','representantecelular','representantecorreo', 'require_stand', 'stand_type',
                  'stand_preference_1','stand_preference_2', 'stand_preference_3', 'day_preference_1', 'day_preference_2',
                  'day_preference_3', 'lunch_number', 'veggie_lunch_number','numeroentrevistadores','tipoentrevista','tiempoxentrevista', 'degree']

    class Meta1:
        model = models.Producer
        fields = ['producerName', 'producerSponsor', 'producerPhone','producerEmail', 'degree']

class CuposForm(forms.Form):

    formset_index = forms.IntegerField(widget=forms.HiddenInput())

    degree = forms.CharField(label="Carrera", max_length=150, required=False)
    practica1 = forms.IntegerField(initial=0, required=False)
    practica2 = forms.IntegerField(initial=0, required=False)
    practica3 = forms.IntegerField(initial=0, required=False)
    memoria = forms.IntegerField(initial=0, required=False)
    fulltime = forms.IntegerField(initial=0, required=False)
    partime = forms.IntegerField(label="Part-time",initial=0, required=False)

    def __init__(self,*args,**kwargs):
        self.degrees = kwargs.pop('degrees')
        self.cupos = kwargs.pop('cupos')
        self.form_index = 0
        super(CuposForm,self).__init__(*args,**kwargs)


    def set_index(self,index):
        self.fields['formset_index'].initial = index
        self.form_index = index
        car = self.degrees[self.form_index]
        self.fields['degree'].initial = car
        self.fields['degree'].widget.attrs['disabled'] = True
        if car == "Ingeniería Civil en Computación" or car == "Ingeniería Civil Eléctrica" or car == "Geología":
            self.fields['practica3'].widget.attrs['disabled'] = True
        if car == "Ingeniería Civil, Mención Estructuras y Construcción" or car == "Ingeniería Civil, Mención Hidrálica, Sanitaria y Ambiental" or car == "Ingeniería Civil, Mención Transporte":
            self.fields['practica1'].widget.attrs['disabled'] = True
        if car == "Licenciatura en Ciencias, Mención Astronomía" or car == "Licenciatura en Ciencias, Mención Física" or car == "Licenciatura en Ciencias, Mención Geofísica":
            self.fields['practica1'].widget.attrs['disabled'] = True
            self.fields['practica2'].widget.attrs['disabled'] = True
            self.fields['practica3'].widget.attrs['disabled'] = True


class CuposFormSet(BaseFormSet):

    def add_fields(self, form, index):
        super(CuposFormSet,self).add_fields(form,index)
        form.set_index(index)

class CuposFormSetHelper(FormHelper):

    def __init__(self,*args,**kwargs):
        super(CuposFormSetHelper,self).__init__(*args,**kwargs)
        self.form_method = 'post'
        self.layout = Layout(
            'degree',
            'practica1',
            'practica2',
            'practica3',
            'memoria',
            'fulltime',
            'partime',
        )
        self.render_hidden_fields = True
		
		
class RequirementsFormInvitadas(forms.ModelForm):
    error_css_class = 'error'
    degree = forms.MultipleChoiceField(choices=choices.DEGREE_CHOICES, label ="Carreras Requeridas")
   # producerName = forms.CharField(max_length=50, label="Nombre productora", required=False)
    #producerSponsor= forms.CharField(max_length=50, label="Persona de contacto de productora", required=False)
    #producerPhone = forms.IntegerField(label="Telefono de persona de contacto",required=False)
    #producerEmail = forms.CharField(max_length=50, label="Email de persona de contacto", required=False)

    def __init__(self, *args, **kwargs):
        super(RequirementsFormInvitadas,self).__init__(*args,**kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'
        self.helper.error_text_inline = True
        #self.fields['day_preference_1'].initial = '1'
        self.fields['stand_type'].initial = '1'
        self.fields['stand_preference_1'].required = False
        self.fields['stand_preference_2'].required = False
        self.fields['stand_preference_3'].required = False
        self.fields['day_preference_2'].required = False
        self.fields['day_preference_3'].required = False
        self.fields['require_stand'].required = False
        #self.fields['producerPhone'].required = False
        

        self.helper.layout = Layout(
            Field('companieName'),
            Field('companieDescription', placeholder="Ingrese una breve descripción de su compañia para ser utilizada en nuestra página web y en la difusión (5000 caracteres máximo)"),
            Field('representantename'),
            Field('representantecelular'),
            Field('representantecorreo'),

			
            Fieldset(
                'Día de Asistencia',
                Div('day_preference_1', css_class='col-md-4'), # borrados los dias de preferencia solo dejando la opcion de dia de asistencia
                Div('preseleccion', css_class='col-md-4'),
                Div('day_preference_2', css_class='col-md-4', style="display: none;"),
                Div('day_preference_3', css_class='col-md-4', style="display: none;"),
            ),

            Fieldset(
                "Tipo de Stand",
                HTML("<p>El tipo de Stand provisto es de medidas 2m x 3m con disposición estándar de la Feria Laboral </p>"),
            Div('stand_type', css_class='col-md-6', style="display: none;"),
            Div('require_stand', css_class='col-md-6', style="display: none;"),
            ),
			
            #HTML("<fieldset><legend hidden id='producer_legend'>Datos de la productora que instalará su stand propio.</legend>"),
        #    Field('producerName', css_class ='col-md-4', id="div_producerName", style="display: none;"),
         #   Field('producerSponsor', css_class = 'col-md-4',id="div_producerSponsor", style="display: none;"),
          #  Field('producerPhone', css_class ='col-md-4',id="div_producerPhone", style="display: none;"),
           # Field('producerEmail', css_class ='col-md-4',id="div_producerEmail", style="display: none;"),
            #HTML("</fieldset>"),
			
            Fieldset(
                'Stand en Layout',
                HTML("<p>El día en el cual participe, un ejecutivo le indicará su Stand asignado </p>"),
            Div('stand_preference_1', css_class ='col-md-4', style="display: none;"),
            Div('stand_preference_2', css_class ='col-md-4', style="display: none;"),
            Div('stand_preference_3', css_class ='col-md-4', style="display: none;"),
            ),




			

            Fieldset(
                'Número de Entrevistadores',
		HTML("<p>Según el porte de su stand, la cantidad máxima de entrevistadores que puede llevar son dos.</p>"),
				Div('numeroentrevistadores', css_class='col-md-8'),
				Div('lunch_number', css_class='col-md-6', style="display: none;"),
				Div('veggie_lunch_number', css_class='col-md-6', style="display: none;"),

            ),
            
            Fieldset(
                'Detalle de Entrevista',
		HTML("<p>Las entrevistas por defecto son individuales de 15 minutos. </br> Usted puede decidir otra dinámica de entrevistas, variando el tiempo o modalidad, lo cual tendrá un efecto en la cantidad de participantes que entrevistará al final del día. </br> Para esto, seleccione 'Otra Modalidad' en tipo de entrevista y contacte con su ejecutivo para la determinación de ésta."),

                Div('tipoentrevista', css_class='col-md-6'),
                Div('tiempoxentrevista', css_class='col-md-6', style="display: none;"),
            ),

            Fieldset(
                'Carreras',
		HTML("<p>Puede ver una descripción de las distintas carreras en el siguiente botón:  <a class='btn btn-primary btn-xs' href='http://www.feriaempresarial.cl/static/site/img/PerfilEspecialidades2018.pdf' target='_blank'>carreras</a>.</p>"),
                InlineCheckboxes('degree', template='requirements/checkboxselectmultiple_inline.html'),
            ),
            Submit('siguiente', 'Siguiente', css_class="btn-success")
        )


    def clean(self):
        cleaned_data = super(RequirementsFormInvitadas,self).clean()
        stand_type = cleaned_data.get('stand_type')
        interviewers = cleaned_data.get('numeroentrevistadores')
        lunch_number = cleaned_data.get('lunch_number')
        veggie_lunch_number = cleaned_data.get('veggie_lunch_number')
        dp1 = cleaned_data.get('day_preference_1')
        st1 = cleaned_data.get('stand_preference_1')
        st2 = cleaned_data.get('stand_preference_2')
        st3 = cleaned_data.get('stand_preference_3')
        rs = cleaned_data.get('require_stand')
        pn = cleaned_data.get('producerName')
        pp = cleaned_data.get('producerPhone')
        pe = cleaned_data.get('producerEmail')
        
        total_lunch = lunch_number + veggie_lunch_number

        if stand_type and total_lunch:
            if stand_type == "1" and total_lunch > 2:
                raise forms.ValidationError(
                    "La cantidad de almuerzos totales no pueden ser mayor a 2"
                )
            #if stand_type == "2" and  total_lunch > 4:
             #   raise forms.ValidationError(
              #      "La cantidad de almuerzos totales no puede ser mayor a 4"
               # )

        if interviewers:
           
            if (stand_type == "1" or stand_type == "3") and interviewers > 2:
                raise forms.ValidationError(
                    "La cantidad de entrevistadores no puede superar a la permitida según stand"
                )
            if (stand_type == "5" or stand_type == "6") and interviewers > 4:
                raise forms.ValidationError(
                    "La cantidad de entrevistadores no puede superar a la permitida según stand"
                )
            if stand_type == "4" and interviewers > 3:
                raise forms.ValidationError(
                    "La cantidad de entrevistadores no puede superar a la permitida según stand"
                )
        if total_lunch:
            if (stand_type == "1" or stand_type == "3") and (lunch_number + veggie_lunch_number) < 2:
                raise forms.ValidationError(
                    "La cantidad de almuerzos es menor a la incluida según stand"
                )
            if (stand_type == "5" or stand_type == "6") and (lunch_number + veggie_lunch_number) < 4:
                raise forms.ValidationError(
                    "La cantidad de almuerzos es menor a la incluida según stand"
                )
            if stand_type == "4"  and (lunch_number + veggie_lunch_number) < 3:
                raise forms.ValidationError(
                    "La cantidad de almuerzos es menor a la incluida según stand"
                )
            if lunch_number <0 or veggie_lunch_number<0:
                raise forms.ValidationError(
                    "Los almuerzos no pueden ser negativos"
                )

        #if dp1 and dp2 and dp3:
         #   if dp1 == dp2 or dp1 == dp3 or dp2 == dp3:
          #      raise forms.ValidationError(
           #         "Los días de preferencia deben ser distintos entre sí"
            #    )

        if st1 and st2 and st3:
            if (st1 != 'A' and st1 != 'B'):
                if st1 == st2 or st1 == st3 or st2 == st3 :
                    raise forms.ValidationError(
                        "Los stands de preferencia deben ser distintos entre sí"
                    )

        if rs:
            if rs == "1" and (pn=="" or pp=="" or pe==""):
                raise forms.ValidationError(
                    "Debe ingresar los datos de productora"
                )


    class Meta:
        model = models.RequirementsCompanies
        fields = ['companieName', 'companieDescription','representantename','representantecelular','representantecorreo', 'require_stand', 'stand_type',
                  'stand_preference_1','stand_preference_2', 'stand_preference_3', 'day_preference_1', 'day_preference_2',
                  'day_preference_3', 'lunch_number', 'veggie_lunch_number','numeroentrevistadores','tipoentrevista','tiempoxentrevista', 'degree']

    class Meta1:
        model = models.Producer
        fields = ['producerName', 'producerSponsor', 'producerPhone','producerEmail', 'degree']


