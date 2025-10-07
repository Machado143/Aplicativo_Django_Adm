from django.contrib import admin
from . import models


class MedicamentoInline(admin.TabularInline):
    model = models.ClienteMedicamento
    extra = 0
    fields = ('medicamento', 'get_fornecedora')
    readonly_fields = ('get_fornecedora',)

    def get_fornecedora(self, obj):
        return obj.medicamento.fornecedora.nome if obj.medicamento.fornecedora else "-"
    get_fornecedora.short_description = 'Fornecedora'


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    inlines = [MedicamentoInline]
    list_display = ('nome', 'email', 'telefone')


@admin.register(models.Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'fornecedora')
    list_filter = ('fornecedora',)


@admin.register(models.Fornecedora)  
class FornecedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'mensagem', 'aprovado')
    list_filter = ('aprovado',)
    actions = ['aprovar_posts']

    def aprovar_posts(self, request, queryset):
        queryset.update(aprovado=True)
    aprovar_posts.short_description = "Aprovar posts selecionados"


admin.site.register(models.ClienteMedicamento)