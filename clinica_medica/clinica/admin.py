from django.contrib import admin
from .models import *

class PacienteCustomizado(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'celular', 'nascimento', 'calcula_idade')
    @admin.display(description='Idade')
    def calcula_idade(self, obj):
        from datetime import date
        hoje = date.today()
        idade = hoje.year - obj.nascimento.year
        return idade
    
class ProcedimentoCustomizado(admin.ModelAdmin):
    list_display = ('paciente','medico','procedimento','data','calcula_dia')
    @admin.display(description='Realizado Há')
    def calcula_dia(self, obj):
        from datetime import date
        dias = (date.today() - obj.data).days
        return f"{dias} dias"

class MedicoCustomizado(admin.ModelAdmin):
    list_display = ('nome','crm','crm_uf','email','celular','funcao')

class FuncionarioCustomizado(admin.ModelAdmin):
    list_display = ('nome','cpf','email','celular','funcao','salario')

#admin.site.register(paciente)
admin.site.register(paciente, PacienteCustomizado)
admin.site.register(medico, MedicoCustomizado)
admin.site.register(funcionario, FuncionarioCustomizado)
admin.site.register(procedimento)
admin.site.register(procedimento_executado, ProcedimentoCustomizado)