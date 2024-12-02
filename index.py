def convertir_longitud(valor, origen, unidad_destino):
    conversion_a_metros = {
        "km": valor * 1000,
        "m": valor,
        "cm": valor * 0.01,
        "mm": valor * 0.001,
        "in": valor * 0.0254,
        "ft": valor * 0.3048,
        "yd": valor * 0.9144,
        "mi": valor * 1609.34
    }
    
    conversion_desde_metros = {
        "km": lambda m: m / 1000,
        "m": lambda m: m,
        "cm": lambda m: m * 100,
        "mm": lambda m: m * 1000,
        "in": lambda m: m * 39.3701,
        "ft": lambda m: m * 3.28084,
        "yd": lambda m: m * 1.09361,
        "mi": lambda m: m / 1609.34
    }
    
    metros = conversion_a_metros.get(origen)
    if metros is not None and unidad_destino in conversion_desde_metros:
        return conversion_desde_metros[unidad_destino](metros)
    return None

def convertir_masa(valor, unidad_origen, unidad_destino):
    
    conversion_a_kg = {
        "kg": valor,
        "g": valor * 0.001,
        "mg": valor * 1e-6,
        "lb": valor * 0.453592,
        "oz": valor * 0.0283495
    }
    
    conversion_desde_kg = {
        "kg": lambda kg: kg,
        "g": lambda kg: kg * 1000,
        "mg": lambda kg: kg * 1e6,
        "lb": lambda kg: kg * 2.20462,
        "oz": lambda kg: kg * 35.274
    }
    
    kg = conversion_a_kg.get(unidad_origen)
    if kg is not None and unidad_destino in conversion_desde_kg:
        return conversion_desde_kg[unidad_destino](kg)
    return None

def convertir_tiempo(valor, unidad_origen, unidad_destino):
    conversion_a_segundos = {
        "s": valor,
        "min": valor * 60,
        "h": valor * 3600,
        "d": valor * 86400,
        "ms": valor * 0.001
    }
    
    conversion_desde_segundos = {
        "s": lambda s: s,
        "min": lambda s: s / 60,
        "h": lambda s: s / 3600,
        "d": lambda s: s / 86400,
        "ms": lambda s: s * 1000
    }
    
    segundos = conversion_a_segundos.get(unidad_origen)
    if segundos is not None and unidad_destino in conversion_desde_segundos:
        return conversion_desde_segundos[unidad_destino](segundos)
    return None

def convertir_temperatura(valor, unidad_origen, unidad_destino):
    match unidad_origen:
        case "K":
            kelvin = valor
        case "C":
            kelvin = valor + 273.15
        case "F":
            kelvin = (valor - 32) * 5/9 + 273.15
        case _:
            return None
    

    match unidad_destino:
        case "K":
            return kelvin
        case "C":
            return kelvin - 273.15
        case "F":
            return (kelvin - 273.15) * 9/5 + 32
        case _:
            return None

def convertir_corriente(valor, de_origen, al_destino):
    conversion_a_amperios = {
        "A": valor,
        "mA": valor * 0.001,
        "µA": valor * 1e-6,
        "kA": valor * 1000
    }
    
    conversion_desde_amperios = {
        "A": lambda a: a,
        "mA": lambda a: a * 1000,
        "µA": lambda a: a * 1e6,
        "kA": lambda a: a / 1000
    }
    
    amperios = conversion_a_amperios.get(de_origen)
    if amperios is not None and al_destino in conversion_desde_amperios:
        return conversion_desde_amperios[al_destino](amperios)
    return None

def convertir_cantidad_sustancia(valor, unidad_origen, unidad_destino):
    conversion_a_moles = {
        "mol": valor,
        "mmol": valor * 0.001,
        "µmol": valor * 1e-6,
        "kmol": valor * 1000
    }
    
    conversion_desde_moles = {
        "mol": lambda m: m,
        "mmol": lambda m: m * 1000,
        "µmol": lambda m: m * 1e6,
        "kmol": lambda m: m / 1000
    }
    
    moles = conversion_a_moles.get(unidad_origen)
    if moles is not None and unidad_destino in conversion_desde_moles:
        return conversion_desde_moles[unidad_destino](moles)
    return None

def convertir_intensidad_luminosa(valor, unidad_origen, unidad_destino):
    conversion_a_candelas = {
        "cd": valor,
        "mcd": valor * 0.001,
        "kcd": valor * 1000
    }
    
    conversion_desde_candelas = {
        "cd": lambda c: c,
        "mcd": lambda c: c * 1000,
        "kcd": lambda c: c / 1000
    }
    
    candelas = conversion_a_candelas.get(unidad_origen)
    if candelas is not None and unidad_destino in conversion_desde_candelas:
        return conversion_desde_candelas[unidad_destino](candelas)
    return None

def convertir_unidades(valor, unidad_origen, unidad_destino, tipo_magnitud):
    match tipo_magnitud.lower():
        case "longitud":
            return convertir_longitud(valor, unidad_origen, unidad_destino)
        case "masa":
            return convertir_masa(valor, unidad_origen, unidad_destino)
        case "tiempo":
            return convertir_tiempo(valor, unidad_origen, unidad_destino)
        case "temperatura":
            return convertir_temperatura(valor, unidad_origen, unidad_destino)
        case "corriente":
            return convertir_corriente(valor, unidad_origen, unidad_destino)
        case "sustancia":
            return convertir_cantidad_sustancia(valor, unidad_origen, unidad_destino)
        case "luminosa":
            return convertir_intensidad_luminosa(valor, unidad_origen, unidad_destino)
        case _:
            return None

if __name__ == "__main__":
    print("Ejemplos de conversiones:")
    
    resultado = convertir_unidades(1, "km", "m", "longitud")
    print(f"1 km = {resultado} m")
    
    resultado = convertir_unidades(1000, "g", "kg", "masa")
    print(f"1000 g = {resultado} kg")

    resultado = convertir_unidades(0, "C", "K", "temperatura")
    print(f"0°C = {resultado} K")
    
    resultado = convertir_unidades(1, "h", "min", "tiempo")
    print(f"1 h = {resultado} min")
    
    resultado = convertir_unidades(1, "A", "mA", "corriente")
    print(f"1 A = {resultado} mA")
    
    resultado = convertir_unidades(1, "mol", "mmol", "sustancia")
    print(f"1 mol = {resultado} mmol")

    resultado = convertir_unidades(1, "cd", "mcd", "luminosa")
    print(f"1 cd = {resultado} mcd")