"""Nython: programa en espanol, ejecuta en Python."""

from .importador import instalar_importador
from .traductor import traducir_codigo

__version__ = "0.1.0"

__all__ = ["instalar_importador", "traducir_codigo"]
