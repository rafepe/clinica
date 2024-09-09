import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html
from .models import paciente, funcionario, medico, procedimento

class paciente_table(tables.Table):
    nome = tables.LinkColumn("paciente_update", args=[A("pk")])
    cpf = tables.LinkColumn("paciente_update", args=[A("pk")])
    email = tables.LinkColumn("paciente_update", args=[A("pk")])
    celular = tables.LinkColumn("paciente_update", args=[A("pk")])
    nascimento = tables.LinkColumn("paciente_update", args=[A("pk")])
    id = tables.LinkColumn("paciente_delete", args=[A("pk")], verbose_name="Excluir")


    class Meta:
        model = paciente
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome','cpf', 'email', 'celular', 'nascimento')

class funcionario_table(tables.Table):
    nome = tables.LinkColumn("funcionario_update", args=[A("pk")])
    cpf = tables.LinkColumn("funcionario_update", args=[A("pk")])
    email = tables.LinkColumn("funcionario_update", args=[A("pk")])
    celular = tables.LinkColumn("funcionario_update", args=[A("pk")])
    endereco = tables.LinkColumn("funcionario_update", args=[A("pk")])
    funcao = tables.LinkColumn("funcionario_update", args=[A("pk")])
    salario = tables.LinkColumn("funcionario_update", args=[A("pk")])
    ativo = tables.Column()
    id = tables.LinkColumn("funcionario_delete", args=[A("pk")], verbose_name="Excluir")


    class Meta:
        model = funcionario
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome', 'cpf', 'email', 'celular', 'endereco', 'funcao', 'salario', 'ativo')

class medico_table(tables.Table):    
    nome = tables.LinkColumn("medico_update", args=[A("pk")])
    crm = tables.LinkColumn("medico_update", args=[A("pk")])
    crm_uf = tables.LinkColumn("medico_update", args=[A("pk")])
    email = tables.LinkColumn("medico_update", args=[A("pk")])
    celular = tables.LinkColumn("medico_update", args=[A("pk")])
    funcao = tables.LinkColumn("medico_update", args=[A("pk")])
    id = tables.LinkColumn("medico_delete", args=[A("pk")], verbose_name="Excluir")


    class Meta:
        model = medico
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome','crm','crm_uf','email','celular','funcao')

class procedimento_table(tables.Table):
    nome = tables.LinkColumn("procedimento_update", args=[A("pk")])
    cid = tables.LinkColumn("procedimento_update", args=[A("pk")])
    valor = tables.LinkColumn("procedimento_update", args=[A("pk")])
    id = tables.LinkColumn("procedimento_delete", args=[A("pk")], verbose_name="Excluir")

    class Meta:
        model = procedimento
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('nome','cid','valor')


class procedimento_executado_table(tables.Table):
    data = tables.LinkColumn("procedimento_executado_update", args=[A("pk")])
    paciente = tables.LinkColumn("procedimento_executado_update", args=[A("pk")])
    medico = tables.LinkColumn("procedimento_executado_update", args=[A("pk")])
    procedimento = tables.LinkColumn("procedimento_executado_update", args=[A("pk")])
    obs = tables.LinkColumn("procedimento_executado_update", args=[A("pk")])
    quantidade =tables.LinkColumn("procedimento_executado_update", args=[A("pk")])
    id = tables.LinkColumn("procedimento_executado_delete", args=[A("pk")], verbose_name="Excluir")

    class Meta:
        model = procedimento
        attrs = {"class": "table thead-light table-striped table-hover"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ('data','paciente','medico','procedimento','obs','quantidade')