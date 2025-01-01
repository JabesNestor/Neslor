# Neslor

Neslor es una biblioteca de Python para trabajar con paletas de colores. Proporciona funciones para obtener y mostrar diferentes paletas de colores.

## Instalación

Para instalar las dependencias del proyecto, ejecuta:

## Uso 
**Obtenemos una paleta de colores**
puedes obtener una paleta de colores especifica utilizando [get_palett]:
ejemplo:

from core import get_palette

palette = get_palette("coorp")
print(palette)

**Mostrar todas las paletas de colores**
Puedes mostrar todas las paletas de colores disponible utilizando la funcion [show_palettes]:

**Obetener una paleta de colores aletoria**
Puedes obtener una paleta de colores aleatoria utilizando la funcion [get_random_palette]:

from core import show_palettes

show_palettes()

## Paletas de colores disponibles actualmente



# Contribuir

Collecting workspace information

Claro, aquí tienes un ejemplo de cómo podrías estructurar tu archivo 

README.md

 para tu proyecto:

```markdown
# Neslor

Neslor es una biblioteca de Python para trabajar con paletas de colores. Proporciona funciones para obtener y mostrar diferentes paletas de colores.

## Instalación

Para instalar las dependencias del proyecto, ejecuta:

```sh
pip install -r requirements.txt
```

## Uso

### Obtener una paleta de colores

Puedes obtener una paleta de colores específica utilizando la función 

get_palette

:

```python
from core import get_palette

palette = get_palette("coorp")
print(palette)
```

### Mostrar todas las paletas de colores

Puedes mostrar todas las paletas de colores disponibles utilizando la función 

show_palettes

:

```python
from core import show_palettes

show_palettes()
```

### Obtener una paleta de colores aleatoria

Puedes obtener una paleta de colores aleatoria utilizando la función 

get_random_palette

:

```python
from core import get_random_palette

palette_name, palette = get_random_palette()
print(f"Paleta aleatoria '{palette_name}': {palette}")
```

## Paletas de colores disponibles

- 

coorp


- 

budapest


- 

fox


- 

city


- 

primary



## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para mas detalles.

