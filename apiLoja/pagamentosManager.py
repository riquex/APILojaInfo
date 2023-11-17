from dbManager import DBManager        

class PagamentosManager:
    def __init__(self, valor_total):
        self.valor_total = valor_total

    def realizar_pagamento(self, metodo, parcelas=1):
        if metodo == "Pix":
            return self.pagar_com_pix()
        elif metodo == "CartaoDebito":
            return self.pagar_com_cartao_debito()
        elif metodo == "CartaoCredito":
            return self.pagar_com_cartao_credito(parcelas)
        elif metodo == "BoletoBancario":
            return self.gerar_boleto_bancario()
        else:
            return "Método de pagamento não suportado."

    def pagar_com_pix(self):
        # Lógica para pagamento com Pix
        return "Pagamento realizado com Pix. Valor: R$ {:.2f}".format(self.valor_total)

    def pagar_com_cartao_debito(self):
        # Lógica para pagamento com Cartão de Débito
        return "Pagamento realizado com Cartão de Débito. Valor: R$ {:.2f}".format(self.valor_total)

    def pagar_com_cartao_credito(self, parcelas):
        if parcelas > 1 and parcelas <= 3:
            valor_parcela = self.valor_total / parcelas
            return "Pagamento realizado com Cartão de Crédito em {} parcelas. Valor da parcela: R$ {:.2f}".format(parcelas, valor_parcela)
        elif parcelas == 1:
            return "Pagamento realizado com Cartão de Crédito. Valor: R$ {:.2f}".format(self.valor_total)
        else:
            return "Parcelamento em até 3 vezes disponível apenas."

    def gerar_boleto_bancario(self):
        # Lógica para geração de boleto bancário
        return "Boleto bancário gerado. Valor: R$ {:.2f}".format(self.valor_total)

if __name__=="__main__":
    # Exemplo de uso:
    valor_compra = 100.50
    gerenciador_pagamentos = PagamentosManager(valor_compra)

    # Escolhendo o método de pagamento e o número de parcelas
    metodo_pagamento = "CartaoCredito"
    num_parcelas = 3

    # Realizando o pagamento
    resultado_pagamento = gerenciador_pagamentos.realizar_pagamento(metodo_pagamento, num_parcelas)
