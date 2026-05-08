def calcular(valor):
    numeros = []
    operadores = []
    num_temp = ""

    if not valor or valor[-1] in ["-","+","/","*"]:
        return valor

    for num in valor:
        if num in ["-","+","/","*"]:
            if num_temp == "":
                return
            numeros.append(float(num_temp))
            operadores.append(num)
            num_temp=""
        else:
            num_temp += num
    if num_temp:
        numeros.append(float(num_temp))
    if not operadores:
        return valor
    
    i=0
    while i < len(operadores):
        try:
            if operadores[i] == "*":
                numeros[i] *= numeros[i+1]
                del numeros[i+1]
                del operadores[i]
            
            elif operadores[i] == "/":
                if numeros[i+1] == 0:
                    return "Infinity"
                numeros[i] /= numeros[i+1]
                del numeros[i+1]
                del operadores[i]
            else:
                i+=1
        except Exception:
            return "ERRO"
    resultado = numeros[0]
    for i, op in enumerate(operadores):
        if op == "+":
            resultado += numeros[i+1]
        elif op =="-":
            resultado -= numeros[i+1]

    resultado = round(resultado, 5)
    if resultado == int(resultado):
        return int(resultado)
    return resultado