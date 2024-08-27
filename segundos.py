
total_segundos = int( input( 'Por favor, entre com o número de segundos que deseja converter: ' ) )

def converter_segundos(segundos):
    dias = segundos // (24 * 3600)
    segundos %= (24 * 3600)
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    
    return dias, horas, minutos, segundos

dias, horas, minutos, segundos = converter_segundos(total_segundos)
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos")
