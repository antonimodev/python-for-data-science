---
name: meta-skill-creator
description: Genera automáticamente la estructura de carpetas y el archivo SKILL.md para nuevas habilidades (skills) siguiendo el estándar oficial de Antigravity. Úsalo cuando el usuario diga "Crea una skill para..." o "Necesito una skill de...".
---

# Meta Skill Creator

Eres un experto diseñando "Agent Skills" para Google Antigravity. Tu objetivo es generar el código y la documentación necesaria para crear una nueva habilidad basada en la descripción del usuario.

## When to use this skill

- Úsalo cuando el usuario solicite explícitamente crear, generar o diseñar una nueva "skill", "habilidad" o "herramienta" para el agente.
- Úsalo para estandarizar el formato de todos los skills del proyecto.

## How to use it

Para generar la nueva skill, debes seguir estos pasos rigurosamente:

### 1. Análisis de requisitos
Analiza la petición del usuario para determinar:
- **Nombre del skill:** Debe ser en `kebab-case` (ej: `python-typehints`, `django-crud-generator`).
- **Propósito:** Una frase corta para la `description` del YAML.
- **Instrucciones:** Los pasos lógicos que la IA debería seguir para ejecutar esa tarea.

### 2. Generación de Estructura
Debes generar un bloque de código con el comando de terminal para crear el directorio correcto:
`mkdir -p .agent/skills/<nombre-del-skill>`

### 3. Generación del contenido (SKILL.md)
Debes redactar el contenido del archivo `SKILL.md` usando **estrictamente** la siguiente plantilla estándar. No cambies los títulos de las secciones (`##`).

**Plantilla a rellenar:**

```markdown
---
name: <nombre-del-skill>
description: <descripción corta en tercera persona>
---

# <Título del Skill (Nombre legible)>

<Breve introducción del rol que adopta el agente (ej: Eres un experto en...)>

## When to use this skill

- Use this when... <Rellena con 2-3 puntos clave basados en la petición>
- This is helpful for... <Beneficio principal>

## How to use it

<Aquí redacta las instrucciones paso a paso que el agente debe seguir.>
<Si el usuario dio ejemplos concretos, inclúyelos aquí.>
<Si es un skill de código, incluye reglas de estilo o snippets.>