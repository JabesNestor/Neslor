# paletas de de colores para los gráficos
# Paleta de colores corporativa
coorp = ['#003366', '#00509E', '#FFC72C', '#A6192E']

# Paletas estilo Wes Anderson
budapest = ['#BB1719','#2C0C1D','#52253D','#841317','#CE736F','#F3BEB4']
fox = ['#AA4C26','#CAA639','#2F7894','#BB4F24','#730A16']
city = ['#AABBA3', '#D8D6A4', '#CC7420', '#864E1B']

# Colores primarios
primary = ['#652C7D', '#CF3830', '#F58C38', '#F58C38', '#D1D1CF', '#5D6266']


""" 
# Paletas pastel
primary_cake = ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF']
cake_1 = ['#F4CCCC', '#FCE5CD', '#FFF2CC', '#D9EAD3', '#D0E0E3']
cake_2 = ['#CFE2F3', '#F4CCCC', '#D9EAD3', '#FFF2CC', '#D0E0E3']
cake_3 = ['#FCE5CD', '#D9EAD3', '#FFF2CC', '#CFE2F3', '#F4CCCC']

# Oscuros
primary_light = ['#586F7C', '#B8B3C3', '#AFD2E9', '#C1D6E1']
primary_dark = ['#1D2B36', '#404E4D', '#586F7C', '#6E8898']
dark_1 = ['#2E2E2E', '#484848', '#6B6B6B', '#8E8E8E', '#B1B1B1']
dark_2 = ['#1C1C1C', '#373737', '#555555', '#737373', '#929292']
dark_3 = ['#121212', '#303030', '#505050', '#707070', '#909090']

# Tableau
tableau = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948']

# Power BI
power_bi = ['#E06666', '#6FA8DC', '#FFD966', '#93C47D', '#6AA84F']

# Videojuegos
games = ['#FF4E50', '#FC913A', '#F9D423', '#EDE574', '#E1F5C4']




def paletta_colors(category=None):
    palettes = {
        "corporate": coorp,
        "wes_anderson": {
            "budapest": budapest,
            "fox": fox,
            "city": city,
        },
        "pastel": {
            "primary": primary_cake,
            "cake_1": cake_1,
            "cake_2": cake_2,
            "cake_3": cake_3,
        },
        "dark": {
            "primary_light": primary_light,
            "primary_dark": primary_dark,
            "dark_1": dark_1,
            "dark_2": dark_2,
            "dark_3": dark_3,
        },
        "tableau": tableau,
        "power_bi": power_bi,
        "games": games,
    }
    
    if category is None:
        return palettes  # Devuelve todas las categorías si no se especifica una
    
    # Busca la categoría especificada
    palette = palettes.get(category)
    if palette is None:
        print(f"Categoría '{category}' no encontrada. Opciones disponibles: {list(palettes.keys())}")
        return None
    
    return palette

    """