import pytest
from pytest import mark
import sys
sys.path.append("Sprint07/bytebank-tdd")
from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_12_01_1995_deve_retornar_28(self):

        entrada = "12/01/1995" #Contexto
        esperado = 28

        funcionario_teste = Funcionario("Gabriel", entrada, 1000)
        resultado = funcionario_teste.idade() #Ação

        assert resultado == esperado #Desfecho

    def test_quando_sobrenome_recebe_Gabriel_Silva_deve_retornar_Silva(self):
        entrada = " Gabriel Silva "
        esperado = "Silva"

        gabriel = Funcionario(entrada, "12/01/1995", 2000)
        resultado = gabriel.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, 11/11/2000, entrada_salario)

        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_1000(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario("teste", 11/11/2000, entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000

            funcionario_teste = Funcionario("teste", 11 / 11 / 2000, entrada_salario)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

