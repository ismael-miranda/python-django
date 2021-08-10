from typing import List
from pypro.modulos.models import Modulo


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por titulo
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug) -> Modulo:
    return Modulo.objects.get(slug=slug)
