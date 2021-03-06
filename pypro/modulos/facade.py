from typing import List
from pypro.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por titulo
    :return:
    """
    return list(Modulo.objects.order_by('titulo').all())


def encontrar_modulo(slug) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulos_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)


def listar_modulos_com_aulas():
    return Modulo.objects.order_by('order').prefetch_related('aula_set').all()
