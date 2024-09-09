from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

############
# PACIENTE #
############
from django_tables2 import SingleTableView
class paciente_menu(SingleTableView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.view_paciente"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para ver pacientes")
    from .models import paciente
    from .tables import paciente_table
    model = paciente
    table_class = paciente_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'clinica/paciente_menu.html'

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class paciente_create(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.create_paciente"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para criar pacientes")
    from .models import paciente
    model = paciente
    fields = ['nome','cpf', 'email', 'celular', 'nascimento']
    def get_success_url(self):
        return reverse_lazy('paciente_menu')

from django.views.generic.edit import UpdateView
class paciente_update(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.update_paciente"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para atualizar pacientes")
    from .models import paciente
    model = paciente
    fields = ['nome','cpf', 'email', 'celular', 'nascimento']
    def get_success_url(self):
        return reverse_lazy('paciente_menu')   

from django.views.generic.edit import DeleteView
class paciente_delete(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.delete_paciente"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para exlcuir pacientes")
    from .models import paciente
    model = paciente
    fields = ['nome','cpf', 'email', 'celular', 'nascimento']
    template_name_suffix = '_delete'
    def get_success_url(self):
        return reverse_lazy('paciente_menu')


###############
# FUNCIONARIO #
###############

from django.contrib.auth import authenticate, login, logout
def index(request):
    usuario = request.POST.get('username')
    senha = request.POST.get('password')
    user = authenticate(username=usuario, password=senha)
    if (user is not None):
        login(request, user)
        request.session['username'] = usuario
        request.session['password'] = senha
        request.session['usernamefull'] = user.get_full_name()

        from django.shortcuts import redirect
        return redirect('procedimento_menu')
    else:       
        return render(request, 'index.html')

from django_tables2 import SingleTableView
class funcionario_menu(SingleTableView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.view_funcionario"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para ver funcionários")    
    from .models import funcionario
    from .tables import funcionario_table
    model = funcionario
    table_class = funcionario_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'clinica/funcionario_menu.html'
    queryset = funcionario.objects.filter(ativo=True)

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class funcionario_create(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.create_funcionario"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para criar funcionários")    
    from .models import funcionario
    model = funcionario
    fields = ['nome', 'cpf', 'email', 'celular', 'endereco', 'funcao', 'salario', 'ativo']
    def get_success_url(self):
        return reverse_lazy('funcionario_menu')

from django.views.generic import ListView
class funcionario_list(ListView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.view_funcionario"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para ver funcionários")    
    from .models import funcionario
    model = funcionario
    queryset = funcionario.objects.filter(ativo=True)

from django.views.generic.edit import UpdateView
class funcionario_update(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.update_funcionario"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para atualizar funcionários")    
    from .models import funcionario
    model = funcionario
    fields = ['nome', 'cpf', 'email', 'celular', 'endereco', 'funcao', 'salario', 'ativo']
    def get_success_url(self):
        return reverse_lazy('funcionario_menu')   

from django.views.generic.edit import DeleteView
class funcionario_delete(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.delete_funcionario"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para excluir funcionários")    
    from .models import funcionario
    model = funcionario
    fields = ['nome', 'cpf', 'email', 'celular', 'endereco', 'funcao', 'salario', 'ativo']
    template_name_suffix = '_delete'
    def get_success_url(self):
        return reverse_lazy('funcionario_menu')
        
##########
# MEDICO #
##########
from django_tables2 import SingleTableView
class medico_menu(SingleTableView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.view_medico"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para ver médicos")    
    from .models import medico
    from .tables import medico_table
    model = medico
    table_class = medico_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'clinica/medico_menu.html'

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class medico_create(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.create_medico"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para criar médicos")  
    from .models import medico
    model = medico
    fields = ['nome','crm','crm_uf','email','celular','funcao']
    def get_success_url(self):
        return reverse_lazy('medico_menu')

from django.views.generic.edit import UpdateView
class medico_update(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.update_medico"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para atualizar médicos")  
    from .models import medico
    model = medico
    fields = ['nome','crm','crm_uf','email','celular','funcao']
    def get_success_url(self):
        return reverse_lazy('medico_menu')   

from django.views.generic.edit import DeleteView
class medico_delete(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.delete_medico"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para excluir médicos")  
    from .models import medico
    model = medico
    fields = ['nome','crm','crm_uf','email','celular','funcao']
    template_name_suffix = '_delete'
    def get_success_url(self):
        return reverse_lazy('medico_menu')

################
# PROCEDIMENTO #
################
from django_tables2 import SingleTableView
class procedimento_menu(SingleTableView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.view_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para ver procedimentos")  
    from .models import procedimento
    from .tables import procedimento_table
    model = procedimento
    table_class = procedimento_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'clinica/procedimento_menu.html'

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class procedimento_create(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.create_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para criar procedimentos")  
    from .models import procedimento
    model = procedimento
    fields = ['nome','cid','valor']
    def get_success_url(self):
        return reverse_lazy('procedimento_menu')

from django.views.generic.edit import UpdateView
class procedimento_update(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.update_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para atualizar procedimentos")  
    from .models import procedimento
    model = procedimento
    fields = ['nome','cid','valor']
    def get_success_url(self):
        return reverse_lazy('procedimento_menu')   

from django.views.generic.edit import DeleteView
class procedimento_delete(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.delete_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para excluir procedimentos")  
    from .models import procedimento
    model = procedimento
    fields = ['nome','cid','valor']
    template_name_suffix = '_delete'
    def get_success_url(self):
        return reverse_lazy('procedimento_menu')


##########################
# PROCEDIMENTO EXECUTADO #
##########################
from django_tables2 import SingleTableView
class procedimento_executado_menu(SingleTableView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.view_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para ver procedimentos")  
    from .models import procedimento_executado
    from .tables import procedimento_executado_table
    model = procedimento_executado
    table_class = procedimento_executado_table
    template_name_suffix = '_menu'
    table_pagination = {"per_page": 5}
    template_name = 'clinica/procedimento_executado_menu.html'

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
class procedimento_executado_create(CreateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.create_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para criar procedimentos")  
    from .models import procedimento_executado
    model = procedimento_executado
    fields = ['data','paciente','medico','procedimento','obs','quantidade']
    def get_success_url(self):
        return reverse_lazy('procedimento_executado_menu')

from django.views.generic.edit import UpdateView
class procedimento_executado_update(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.update_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para atualizar procedimentos")  
    from .models import procedimento_executado
    model = procedimento_executado
    fields = ['data','paciente','medico','procedimento','obs','quantidade']
    def get_success_url(self):
        return reverse_lazy('procedimento_executado_menu')   

from django.views.generic.edit import DeleteView
class procedimento_executado_delete(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm("clinica.delete_procedimento"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Sem permissão para excluir procedimentos")  
    from .models import procedimento_executado
    model = procedimento_executado
    fields = ['data','paciente','medico','procedimento','obs','quantidade']
    template_name_suffix = '_delete'
    def get_success_url(self):
        return reverse_lazy('procedimento_executado_menu')

from django.db.models import Count  # Importar Count para contagem
from clinica.models import funcionario, paciente, procedimento, medico, procedimento_executado
def orm_sql(request):
    # SELECT f.nome, f.cpf
    # FROM funcionario f
    # WHERE f.cpf IN (SELECT p.cpf FROM paciente p);

    #Lista com todos os cpfs dos pacientes
    pacientes_cpfs = paciente.objects.values_list('cpf', flat=True)
    #Filtrar funcionários com o cpf na lista
    funcionarios_pacientes = funcionario.objects.filter(cpf__in=pacientes_cpfs)

    procedimento_mais_caro = procedimento.objects.order_by('-valor').first()
    funcionario_maior_salario = funcionario.objects.order_by('salario').last()
    funcionarios_mais_que = funcionario.objects.filter(salario__gt=3500,salario__lt=5500)

    dict = {
        'funcionarios_pacientes': funcionarios_pacientes,
        'procedimento_mais_caro': procedimento_mais_caro,
        'funcionario_maior_salario': funcionario_maior_salario,
        'funcionarios_mais_que': funcionarios_mais_que,
    }
    return render(request, 'orm_sql.html', dict)


def exportar(request):
    import pandas as pd
    from .models import procedimento_executado
    eixo_y = []
    p = procedimento_executado.objects.all()
    for _regs in p:
        eixo_x = []
        eixo_x.append(_regs.id)
        eixo_x.append(_regs.data)
        eixo_x.append(_regs.paciente)
        eixo_x.append(_regs.medico)
        eixo_x.append(_regs.procedimento)
        eixo_x.append(_regs.obs)
        eixo_x.append(_regs.quantidade)
        eixo_y.append(eixo_x)
        _rotulos_colunas = []
        _rotulos_colunas.append("id")
        _rotulos_colunas.append("data de realização")
        _rotulos_colunas.append("nome do paciente")
        _rotulos_colunas.append("nome do médico")
        _rotulos_colunas.append("procedimento")
        _rotulos_colunas.append("observações")
        _rotulos_colunas.append("quantidade")
        df = pd.DataFrame(eixo_y, columns=_rotulos_colunas)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=procedimentos_executados.csv'
        df.to_csv(path_or_buf=response)
    return response

