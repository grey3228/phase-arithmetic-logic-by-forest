from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.api import QuantumComputer

def compile_and_run(program: Program, qc: QuantumComputer, data_region_name: str):
    """
        Компиляция переданной программы и запуск скомпилированного кода на симуляторе кв. компьютера.
        Результат считывается из заранее выделенной области памяти.
    """

    # компиляция составленной программы
    executable = qc.compile(program)
    # запуск программы на симуляторе квантового компьютера
    result = qc.run(executable)
    # чтение результата из памяти
    return result.readout_data.get(data_region_name).flatten()