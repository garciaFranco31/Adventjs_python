"""Santa ha recibido una lista de regalos, pero algunos están defectuosos. Un regalo es defectuoso si su nombre contiene el carácter #.

Ayuda a Santa escribiendo una función que reciba una lista de nombres de regalos y devuelva una nueva lista que solo contenga los regalos sin defectos."""


regalos = ["#"]

def regalo_ok(regalos):
    regalos_ok = []

    for regalo in regalos:
        if ("#" not in regalo):
            regalos_ok.append(regalo)

    return regalos_ok


print(regalo_ok(regalos))