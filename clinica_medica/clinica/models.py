from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils import timezone
from datetime import date

# Create your models here.
class paciente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome Completo')
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False,
        verbose_name='CPF',
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='O CPF deve conter exatamente 11 dígitos.',
            )],
    )
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='E-mail')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='Celular')
    nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')

    def __str__(self):
        return self.nome
 
    class Meta:
        ordering = ['nome']

class medico(models.Model):
    UF_CHOICES = [ 
    ('AC','AC'), 
    ('AL','AL'),
    ('AP','AP'),
    ('AM','AM'),
    ('BA','BA'),
    ('CE','CE'),
    ('DF','DF'),
    ('ES','ES'),
    ('GO','GO'),
    ('MA','MA'),
    ('MT','MT'),
    ('MS','MS'),
    ('MG','MG'),
    ('PA','PA'),
    ('PB','PB'),
    ('PR','PR'),
    ('PE','PE'),
    ('PI','PI'),
    ('RJ','RJ'),
    ('RN','RN'),
    ('RS','RS'),
    ('RO','RO'),
    ('RR','RR'),
    ('SC','SC'),
    ('SP','SP'),
    ('SE','SE'),
    ('TO','TO'),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome Completo')
    crm = models.IntegerField(null=False, blank=False, verbose_name='CRM', validators=[
            MinValueValidator(1),
            MaxValueValidator(999999)
        ],
        unique=True,
    )
    crm_uf = models.CharField(max_length=2, choices=UF_CHOICES, default='GO', verbose_name='CRM UF')
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='E-mail')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='Celular')
    funcao = models.CharField(max_length=30, null=True, blank=True, verbose_name='Função')
    
    def __str__(self):
        return self.nome
 
    class Meta:
        ordering = ['nome']

class funcionario(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome Completo')
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False,
        verbose_name='CPF',
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='O CPF deve conter exatamente 11 dígitos.',
            )],
    )
    email = models.CharField(max_length=50, null=False, blank=False, verbose_name='E-mail')
    celular = models.CharField(max_length=20, null=True, blank=True, verbose_name='Celular')
    endereco = models.CharField(max_length=100, null=False, blank=False, verbose_name='Endereço Completo')
    funcao = models.CharField(max_length=30, null=True, blank=True, verbose_name='Função/Cargo')
    salario = models.DecimalField(null=True,blank=False, verbose_name='Salário R$', decimal_places=2, max_digits=8, default=1430)
    ativo = models.BooleanField(default=True, verbose_name='Ativo')


    def __str__(self):
        return self.nome
 
    class Meta:
        ordering = ['nome','cpf','celular',]

class procedimento(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    cid = models.CharField(max_length=20, null=False, blank=False, default=None, verbose_name='CID')
    valor = models.FloatField(null=True, blank=True, default=None, verbose_name='Valor')
    def __str__(self):
        return self.nome
    class Meta:
        ordering = ['nome']
        
class procedimento_executado(models.Model):
    data = models.DateField(null=True, blank=True, verbose_name='Data do Procedimento')
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(medico, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(procedimento, on_delete=models.CASCADE)
    obs = models.CharField(max_length=50, null=True, blank=True, verbose_name='Observação')
    quantidade = models.FloatField(null=True, blank=True, default=None, verbose_name='Quantidade')
    def __str__(self):
        return self.obs
    class Meta:
        ordering = ['-data','paciente']


