from colors import *
import random
import matplotlib.pyplot as plt


def get_palette(palette_name):
    palettes = {
        "coorp": coorp,
        "budapest": budapest,
        "fox": fox,
        "city": city,
        "primary": primary
    }
    
    if palette_name in palettes:
        return palettes[palette_name]
    else:
        raise ValueError(f"Palette '{palette_name}' not found. Available palettes: {list(palettes.keys())}")

def show_palettes():
    palettes = {
        "coorp": coorp,
        "budapest": budapest,
        "fox": fox,
        "city": city,
        "primary": primary
    }

    for name, colors in palettes.items():
        print(f"Palette '{name}': {colors}")



def get_random_palette():
    from colors import coorp, budapest, fox, city, primary

    palettes = {
        "coorp": coorp,
        "budapest": budapest,
        "fox": fox,
        "city": city,
        "primary": primary
    }

    palette_name = random.choice(list(palettes.keys()))
    return palette_name, palettes[palette_name]


palette = get_palette("budapest")

# Datos de la gráfica
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# Crear la gráfica
plt.figure(figsize=(9, 3))

# Aplica la paleta de colores directamente
colors = palette[:len(values)]  # Asegúrate de que los colores coincidan con la cantidad de barras
plt.subplot(131)
plt.bar(names, values, color=colors)  # Asigna los colores aquí

# Configuración de la gráfica
plt.suptitle('Categorical Plotting')
plt.show()