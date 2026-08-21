"""Conținutul sistemului, separat de generatoare."""
from . import (analitice, corelatii, fluxuri_capitaluri, fluxuri_control,
               fluxuri_imobilizari, fluxuri_salarii, plan)

FLUXURI = (fluxuri_capitaluri.FLUXURI + fluxuri_imobilizari.FLUXURI
           + fluxuri_control.FLUXURI + fluxuri_salarii.FLUXURI_SALARII)
CORELATII = corelatii.CORELATII
ANALITICE = analitice.ANALITICE

__all__ = ["FLUXURI", "CORELATII", "ANALITICE", "plan"]
