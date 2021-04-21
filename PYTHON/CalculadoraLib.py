#LIBRERIA CALCULADORA
def formato1(s):
    r = str(s).split(".")
    if r[1] == "0":
        return int(r[0])
    return s

def formato2(s):
    r = s.split(".")
    if r[1] == "0":
        return r[0]
    return s

def esOperacion(c):
    if c != "":
        return (c in "+-*/")
    else:
        return False

def prioridad(c):
    if c in "+-":
        return 0
    if c in "*/":
        return 1
    
def esNumero(c):
    if c != "":
        return (c in "0123456789.")
    else:
        return False

def operacion(op, num1, num2):
    if op == "+":
        return str(float(num1) + float(num2))
    if op == "-":
        return str(float(num1) - float(num2))
    if op == "*":
        return str(float(num1) * float(num2))
    if op == "/":
        return str(float(num1) / float(num2))

def Calcular(expresion):
    expresion = list(expresion)
    pilaChr = list()
    pilaNum = list()
    pilaNum.append("0")
    num = ""
    while len(expresion) > 0:
        c = expresion.pop(0)
        if len(expresion) > 0: d = expresion[0]
        else: d = ""
        if esNumero(c):
            num += c
            if not esNumero(d):
                pilaNum.append(num)
                num = ""
        elif esOperacion(c):
            while True:
                if len(pilaChr) > 0: top = pilaChr[-1]
                else: top = ""
                if esOperacion(top):
                    if not prioridad(c) > prioridad(top):
                        num2 = pilaNum.pop()
                        op = pilaChr.pop()
                        num1 = pilaNum.pop()
                        pilaNum.append(operacion(op, num1, num2))
                    else:
                        pilaChr.append(c)
                        break
                else:
                    pilaChr.append(c)
                    break
        elif c == "(":
            pilaChr.append(c)
        elif c == ")":
            while len(pilaChr) > 0:
                c = pilaChr.pop()
                if c == "(":
                    break
                elif esOperacion(c):
                    num2 = pilaNum.pop()
                    num1 = pilaNum.pop()
                    pilaNum.append(operacion(c, num1, num2))

    while len(pilaChr) > 0:
        c = pilaChr.pop()
        if c == "(":
            break
        elif esOperacion(c):
            num2 = pilaNum.pop()
            num1 = pilaNum.pop()
            pilaNum.append(operacion(c, num1, num2))
    return pilaNum.pop()


