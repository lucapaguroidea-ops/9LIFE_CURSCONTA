"""Conținutul sistemului, separat de generatoare."""
from . import analitice, corelatii, fluxuri_capitaluri, fluxuri_imobilizari, plan

FLUXURI = fluxuri_capitaluri.FLUXURI + fluxuri_imobilizari.FLUXURI
CORELATII = corelatii.CORELATII
ANALITICE = analitice.ANALITICE

__all__ = ["FLUXURI", "CORELATII", "ANALITICE", "plan"]
