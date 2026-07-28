---
name: maintain-concept-registry
description: Create, validate, and update a project's canonical CONCEPT_REGISTRY.json for scientific, technical, legal, policy, analytical, and multilingual concepts. Govern definitions, labels, scope, authority, status, relations, conflicts, and change propagation without forcing general concepts into indicator schemas or resolving substantive conflicts silently. Use only when explicitly invoked as `$maintain-concept-registry`; never invoke implicitly.
---

# Mantener el registro conceptual

Conservar significado estable sin convertir el registro en diccionario universal.

## Procedimiento

1. Leer sólo las entradas pertinentes del registro, el contexto del proyecto y las fuentes de autoridad aplicables.
2. Clasificar la solicitud como alta, aclaración, cambio, deprecación, conflicto o retiro.
3. Aplicar la prueba de materialidad: registrar sólo conceptos cuya variación pueda cambiar interpretación, análisis, obligación, medición o interoperabilidad.
4. Distinguir concepto general, marco, término jurídico, variable, indicador y proceso. Consultar [references/governance.md](references/governance.md).
5. Comparar autoridades según el orden declarado por el proyecto. No elegir silenciosamente entre definiciones incompatibles.
6. Proponer la modificación y sus consecuencias antes de sustituir una entrada material.
7. Actualizar identificadores estables; no reutilizar un identificador para otro significado.
8. Registrar decisiones conceptuales materiales en `KNOWLEDGE_LEDGER.md` mediante enlace, sin duplicar la definición.
9. Ejecutar `scripts/validate_concept_registry.py` contra el registro y el schema.
10. Informar qué documentos o análisis requieren propagación; no reescribirlos salvo autorización.

## Conflictos

Cuando un concepto general entre en conflicto con uno vinculante o aprobado:

- identificar ambos sentidos y sus ámbitos;
- aplicar la definición de mayor autoridad sólo dentro de su alcance;
- conservar el sentido general fuera de ese alcance cuando siga siendo necesario;
- crear identificadores distintos si son conceptos realmente diferentes;
- registrar `conflicts_with` o `related_not_equivalent`;
- solicitar decisión cuando autoridad o alcance no resuelvan el conflicto.

No usar sinónimos para ocultar el conflicto.

## Límites

- No inventar definiciones disciplinarias, jurídicas ni del cliente.
- No inferir aprobación a partir del uso repetido.
- No completar campos de indicadores para conceptos como causalidad o perspectiva de género.
- No aplicar cambios retroactivamente sin evaluar su efecto sobre resultados históricos.
- No tratar la validación estructural como validación científica o jurídica.

## Entrega

Indicar entradas añadidas o modificadas, autoridad, alcance, conflictos, efectos de propagación, elementos no resueltos y resultado de validación.
