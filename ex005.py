# algoritmo empresa com 10 funcionários

Laco1 = 1
Laco2 = True
Laco3 = True

while Laco1 <= 10:

    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = input("Digite o código do funcionário: ")
    HoraTrabalhada = float(input("Informe as horas trabalhadas: "))

    while Laco2:
        Categoria = input("Digite a categoria: ")
        if Categoria == "O" or Categoria == "G":
            Laco2 = False
        else:
            print("As categorias possíveis são O e G. Digite novamente: ")
            continue
        break

    while Laco3:
        Turno = input("Informe o seu turno: ")
        if Turno == 'M' or Turno == 'V' or Turno == 'N':
            Laco3 = False
        else:
            print("Os turnos possíveis são M, V ou N. Digite novamente: ")
            continue
        break
    if Categoria == "G" and Turno == "N":
        ValorHora = SalarioMinimo * 0.18
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 600:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if Categoria == "G" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.15
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 600:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if Categoria == "O" and Turno == "N":
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 600:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    if Categoria == "O" and Turno == "M" or Turno == "V":
        ValorHora = SalarioMinimo * 0.10
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 600:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    print("Código do funcionário:", Codigo, "Hora trabalhada:", HoraTrabalhada, "Categoria:", Categoria, "Turno:",
          Turno)
    print("Valor da hora: R$", ValorHora, "Salário Inicial: R$", SalarioInicial, "Auxílio Alimentação: R$",
          AuxilioAlimentacao, "Salário Final: R$", SalarioFinal)

    print("Número do laço principal: ", Laco1)
    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True
