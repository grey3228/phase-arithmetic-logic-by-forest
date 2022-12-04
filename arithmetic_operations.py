from pyquil import Program, get_qc
from pyquil.gates import *
from util import compile_and_run
from numpy import ndarray

def increment_operation(qubits: ndarray):
    """
        Инкремент 4-кубитного числа
    """
    qubits_given = qubits.size
    if qubits_given != 4:
        raise Exception('Передайте значения 4 кубитов.')
    p = Program()
    ro = p.declare('ro', 'BIT', 4)
    qc = get_qc('8q-qvm')

    for idx, q in enumerate(qubits):
        if q:
            p += X(idx)
    
    # 5-ый кубит используется для реализации контролируемого вентиля NOT с 3 контролирующими кубитами.
    p += CCNOT(0, 1, 4)
    p += CCNOT(4, 2, 3)
    p += CCNOT(0, 1, 2)
    p += CNOT(0, 1)
    p += X(0)

    for i in range (0, qubits_given):
        p += MEASURE(i, ro[i])

    return compile_and_run(p, qc, 'ro')

def decrement_operation(qubits: ndarray):
    """
        Декремент 4-кубитного числа
    """
    qubits_given = qubits.size
    if qubits_given != 4:
        raise Exception('Передайте значения 4 кубитов.')
    p = Program()
    ro = p.declare('ro', 'BIT', 4)
    qc = get_qc('8q-qvm')

    for idx, q in enumerate(qubits):
        if q:
            p += X(idx)
    
    # 5-ый кубит используется для реализации контролируемого вентиля NOT с 3 контролирующими кубитами.
    p += X(0)
    p += CNOT(0, 1)
    p += CCNOT(0, 1, 2)
    p += CCNOT(0, 1, 4)
    p += CCNOT(4, 2, 3)

    for i in range (0, qubits_given):
        p += MEASURE(i, ro[i])

    return compile_and_run(p, qc, 'ro')

def sum_operation(qubits_reg_1: ndarray, qubits_reg_2: ndarray):
    """
        Сложение 2-ух 4-кубитных чисел
    """
    qubits_reg_1_size = qubits_reg_1.size
    qubits_reg_2_size = qubits_reg_2.size
    
    if qubits_reg_1_size != 4 or qubits_reg_2_size != 4:
        raise Exception('Передайте значения двух 4-кубитных регистров.')
    p = Program()
    ro = p.declare('ro', 'BIT', 4)
    # 12-кубитный компьютер выбран, т.к. помимо двух кубитовых регистров используется 4 вспомогательных кубита для реализации
    # контролируемых вентилей NOT с 3 и 4 контролирующими кубитами.  
    qc = get_qc('12q-qvm')

    for idx, q in enumerate(qubits_reg_1):
        if q:
            p += X(idx)

    for idx, q in enumerate(qubits_reg_2):
        if q:
            p += X(idx + 4)
    
    p += CCNOT(0, 1, 8)
    p += CCNOT(2, 8, 9)
    p += CCNOT(4, 9, 3)
    p += CCNOT(0, 1, 10)
    p += CCNOT(4, 10, 2)
    p += CCNOT(0, 4, 1)
    p += CNOT(4, 0)
    p += CCNOT(0, 1, 11)
    p += CCNOT(5, 11, 3)
    p += CCNOT(1, 5, 2)
    p += CNOT(5, 1)
    p += CCNOT(2, 6, 3)
    p += CNOT(6, 2)
    p += CNOT(7, 3)

    for i in range (0, 4):
        p += MEASURE(i, ro[i])

    return compile_and_run(p, qc, 'ro')

def sign_inversion_operation(qubits: ndarray):
    '''Изменение знака 4-кубитного числа в дополнительном коде'''
    qubits_given = qubits.size
    if qubits_given != 4:
        raise Exception('Передайте значения 4 кубитов.')
    p = Program()
    ro = p.declare('ro', 'BIT', 4)
    qc = get_qc('8q-qvm')

    for idx, q in enumerate(qubits):
        if q:
            p += X(idx)
    
    p += X(0)
    p += X(1)
    p += X(2)
    p += X(3)

    p += CCNOT(0, 1, 4)
    p += CCNOT(4, 2, 3)
    p += CCNOT(0, 1, 2)
    p += CNOT(0, 1)
    p += X(0)

    for i in range (0, qubits_given):
        p += MEASURE(i, ro[i])

    return compile_and_run(p, qc, 'ro')