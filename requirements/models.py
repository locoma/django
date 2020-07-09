from django.db import models
from . import choices
# Create your models here.

class RequirementsCompanies(models.Model):

    companieName = models.CharField("Nombre Compañia", max_length=50)
    companieDescription = models.TextField("Breve Descripción", max_length=5000, null=True) 
    representantename= models.CharField("Nombre de la persona de su empresa a cargo de la Feria", max_length=30, default="")
    representantecelular= models.IntegerField("Celular de la persona de su empresa a cargo de la Feria")
    representantecorreo= models.CharField("Email de la persona de su empresa a cargo de la Feria", max_length=50,null=False, default="")
    stand_type = models.CharField("Tipo de Stand", max_length=1,choices=choices.STAND_TYPE_CHOICES, default=None)
    require_stand = models.CharField("¿Utilizará Stand Propio o Stand Feria?", max_length=2, choices=choices.BRING_STAND_CHOICES, default="0")
    producer = models.ForeignKey('Producer',on_delete=models.CASCADE, null=True)
    veggie_lunch_number = models.IntegerField("Almuerzos Vegetarianos", default=0)
    lunch_number = models.IntegerField("Almuerzos Normales", default=0)
    numeroentrevistadores = models.IntegerField("Numero de Entrevistadores",default=1)
    tipoentrevista=models.CharField("Tipo entrevistas",max_length=20, choices=choices.TIPE_CHOICES,null=False)
    tiempoxentrevista = models.IntegerField("Tiempo de Entrevista", default=15,  null=True, blank=True)
   
    stand_preference_1 = models.CharField("Stand de Preferencia 1", max_length=2, choices=choices.STAND_CHOICES,null=False)
    stand_preference_2 = models.CharField("Stand de Preferencia 2", max_length=2, choices=choices.STAND_CHOICES,null=False)
    stand_preference_3 = models.CharField("Stand de Preferencia 3", max_length=2, choices=choices.STAND_CHOICES,null=False)

    day_preference_1 = models.CharField("Día de Participación", max_length=20, choices=choices.DAY_CHOICES,null=False)
    day_preference_2 = models.CharField("Día Preferencia 2", max_length=20, choices=choices.DAY_CHOICES,null=False)
    day_preference_3 = models.CharField("Día Preferencia 3", max_length=20, choices=choices.DAY_CHOICES,null=False)

    
   

   
   
    ini_date = models.DateTimeField('Fecha Envio',auto_created=True)
    preseleccion = models.BooleanField('Mañana o Tarde', auto_created=False, choices=choices.TIME_CHOICES) #no se estaba usando esto, adaptamos para mañana o tarde
	


class Producer(models.Model):


    name = models.CharField("Nombre Productora", max_length=50,null=False)
    person= models.CharField("Nombre contacto", max_length=30, null=False, default="")
    email = models.CharField("Email", max_length=50,null=False)
    phone = models.IntegerField("Telefono", max_length=12,null=True)
    producerName = models.CharField("Nombre productor", max_length=50, null=False, default="")
    producerSponsor= models.CharField("Nombre Sponsor", max_length=50, null=False, default="")
    producerPhone = models.IntegerField("Telefono",null=True)
    producerEmail = models.CharField("Mail", max_length=50, default="", null=False)


class CuposCarrera(models.Model):

    companie_requirement = models.ForeignKey('RequirementsCompanies')
    degree = models.CharField('Carrera',max_length=2,choices=choices.DEGREE_CHOICES)
    tipo = models.CharField('Tipo Trabajo',max_length=2,choices=choices.TYPES_CHOICES)
    cupos = models.IntegerField("Cupos",max_length=2)
    preseleccion= models.BooleanField(default=False)	
