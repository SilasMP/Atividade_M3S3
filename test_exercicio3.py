import pytest
import exercicio3 as ex3

class TestFuncoesComArgumentos:
    #Classe responsável por testar as funções que precisam receber valores nos argumentos.
       
    def test_funcao_calcular_preco_volume(self):
        resultado = ex3.calcular_preco_volume(30000)
        assert resultado == 20.0

    def test_funcao_calcular_multiplicador_peso(self):
        resultado = ex3.calcular_multiplicador_peso(1.0)
        assert resultado == 2.0

    def test_funcao_calcular_multiplicador_rota(self):
        resultado = ex3.calcular_multiplicador_rota('sr')
        assert resultado == 1.0

    def test_funcao_validar_medida(self):
        resultado = ex3.validar_medida(3)
        assert resultado == 3
    
    def test_funcao_calcular_frete(self):
        resultado = ex3.calcular_frete(20.0, 2.0, 1.0)
        assert resultado == 40

class TestFuncoesComInputs:
    #Classe responsável por testar as Funções que precisam de input manual do usuario
    #a lista e os métodos mock abaixo fornecem valores sem a necessidade de input manual via terminal.

    lista_inputs = [10, 15, 20] #[altura_lida, comprimento_lido, largura_lida]

    def mock_input(self, input):
        #remove um valor da lista a cada nova chamada (input) do mock
        return self.lista_inputs.pop(0)

    def mock_input2(self, input):    
        return 1 #valor referente a 1kg
    
    def mock_input3(self, input):    
        return 'sr' #opção de rota para o teste

    def test_funcao_ler_dimensoes_objeto(self, monkeypatch):
        #uso do método monkeypatch do pytest para informar os valores de input para o teste
        monkeypatch.setattr('builtins.input', self.mock_input)
        resultado = ex3.ler_dimensoes_objeto()
        assert resultado == 20.0

    def test_funcao_ler_peso_objeto(self, monkeypatch):
        monkeypatch.setattr('builtins.input', self.mock_input2)
        resultado = ex3.ler_peso_objeto()
        assert resultado == 2.0

    def test_funcao_ler_rota(self, monkeypatch):
        monkeypatch.setattr('builtins.input', self.mock_input3)
        resultado = ex3.ler_rota()
        assert resultado == 1.0