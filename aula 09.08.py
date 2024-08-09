def verificar_sala(num_pessoas, tipo_reuniao):
    if tipo_reuniao == 'executiva' or num_pessoas> 12:
        return "Sala grande"
    elif 6 <= num_pessoas <= 12:
        return "sala media"
    elif num_pessoas <= 4:
        return "Sala pequena"
# Exemplo de uso:
num_pessoas = 19
tipo_reuniao = 'normal'  # Pode ser  'normal','vip',etc.
sala_recomendada = verificar_sala(num_pessoas, tipo_reuniao)
print(f"A sala recomendada para a reunião é: {sala_recomendada}")
 