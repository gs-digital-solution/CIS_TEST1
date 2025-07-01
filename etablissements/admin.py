from django.contrib import admin
from .forms import EleveForm, EtablissementForm
from django.shortcuts import render  # Ajoutez cette ligne
from django.http import HttpResponseRedirect  # Si pas déjà présent
# Register your models here.
from .models import Etablissement, Eleve

class EleveInline(admin.TabularInline):
    model = Eleve
    extra = 1  # Nombre de formulaires vides affichés

@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ville', 'lycee_bilingue')
    list_filter = ('ville', 'lycee_bilingue')
    search_fields = ('nom',)
    inlines = [EleveInline]
    
    actions = ['modifier_etablissement']  # Ajoutez cette ligne
    def modifier_etablissement(self, request, queryset):
        if 'apply' in request.POST:
            form = EtablissementForm(request.POST)
            if form.is_valid():
                queryset.update(
                    nom=form.cleaned_data['nom'],
                    ville=form.cleaned_data['ville'],
                    lycee_bilingue=form.cleaned_data['lycee_bilingue']
                )
                self.message_user(request, "Mise à jour effectuée")
                return HttpResponseRedirect(request.get_full_path())
        else:
            form = EtablissementForm(initial={
                'nom': queryset.first().nom,
                'ville': queryset.first().ville
            })

        return render(request,
            'admin/modifier_etablissement.html',
            context={'etablissements': queryset, 'form': form})

    modifier_etablissement.short_description = "Modifier les établissements sélectionnés"

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'genre', 'etablissement')
    list_filter = ('genre', 'etablissement')
    search_fields = ('nom', 'prenom')

    actions = ['modifier_eleve']  # Ajoutez cette ligne

    def modifier_eleve(self, request, queryset):
        if 'apply' in request.POST:
            form = EleveForm(request.POST)
            if form.is_valid():
                queryset.update(
                    nom=form.cleaned_data['nom'],
                    prenom=form.cleaned_data['prenom'],
                    genre=form.cleaned_data['genre'],
                    etablissement=form.cleaned_data['etablissement']
                )
                self.message_user(request, "Mise à jour effectuée")
                return HttpResponseRedirect(request.get_full_path())
        else:
            form = EleveForm(initial={
                'nom': queryset.first().nom,
                'prenom': queryset.first().prenom,
                'genre': queryset.first().genre
            })

        return render(request,
            'admin/modifier_eleve.html',
            context={'eleves': queryset, 'form': form})

    modifier_eleve.short_description = "Modifier les élèves sélectionnés"