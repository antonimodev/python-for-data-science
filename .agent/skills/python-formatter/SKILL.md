---
name: python-formatter
description: Formatea código Python siguiendo PEP 8 y buenas prácticas de estilo (Flake8).
---

# Python Formatter Expert

Eres un experto en Python que combina el tipado estático (PEP 484) con un estilo de código impecable (PEP 8). Tu objetivo es transformar código sucio o dinámico en código profesional, legible y bien estructurado.

## When to use this skill

- Use this when creating or refactoring Python code to ensure both type safety and consistent styling.
- Use this to fix linting issues like incorrect spacing, missing newlines, or poorly organized imports.
- This is helpful for maintaining a "clean code" standard across the microservices.

## How to use it

### 1. Type Hinting (PEP 484)
- **Firma de funciones**: Siempre incluye tipos para argumentos y retorno.
- **Modern Typing**: Prioriza siempre la sintaxis de Python 3.10+ (`str | None`, `list[str]`) frente a la antigua (`Optional`, `List` de `typing`).
- **Especifidad**: Evita `Any`. Prefiere protocolos o tipos genéricos.

### 2. Style & Formatting (PEP 8 / Django Style)
Sigue estas reglas de espaciado y estructura:
- **Naming & Shadowing**:
  - NUNCA uses nombres que oculten built-ins de Python (ej: no uses `id`, `type`, `list` como nombres de variables). Usa `user_id`, `obj_type`, `user_list`.
- **Espaciado en funciones**:
  - Dos líneas en blanco entre funciones de nivel superior y clases.
- **Imports (Estilo Django)**:
  - Agrupa en este orden: 1) Stdlib, 2) Third-party, 3) Django Framework, 4) Local imports.
- **Espacios en operadores**:
  - `x = 1` (espacio alrededor de asignación).
  - `def func(a: int = 1)`: CON espacios si HAY type hint.
- **Longitud de línea**:
  - Permite hasta **120 caracteres** (Estándar Django/GitHub) para evitar rupturas de línea innecesarias en modelos complejos.

## Ejemplos

**Código sucio:**
```python
import os
from .models import User
def create_user(name,age=None):
    u=User(name=name,age=age)
    u.save()
    return u
def delete_user(id):
    User.objects.get(id=id).delete()
```

Código limpio (con esta Skill):

```python
import os

from .models import User


def create_user(name: str, age: int | None = None) -> User:
    user = User(name = name, age = age)
    user.save()
    return user


def delete_user(user_id: int) -> None:
    User.objects.get(id=user_id).delete()
```