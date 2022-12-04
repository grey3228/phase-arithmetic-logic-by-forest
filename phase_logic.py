from pyquil import Program, get_qc
from pyquil.gates import *
from util import compile_and_run

def xor_operation(q1, q2):
    """Сложение по модулю 2 (XOR)"""
    # подготовка программы
    p = Program()
    # выделение области памяти, в которую будет записан результат операции (см. функцию MEASURE)
    ro = p.declare('ro', 'BIT', 1)
    # создание объекта для работы с симулятором квантового компьютера
    qc = get_qc('8q-qvm')

    # заполнение регистра кубитов в соответствии с переданными аргументами
    if q1:
        p += X(0)
    if q2:
        p += X(1)

    # применение вентиля CNOT
    p += CNOT(0, 1)    
    # считывание значения кубита 1 в заранее выделенную область памяти
    p += MEASURE(1, ro[0])
    return compile_and_run(p, qc, 'ro')

def not_operation(q):
    """Отрицание"""
    p = Program()
    ro = p.declare('ro', 'BIT', 1)
    qc = get_qc('8q-qvm')
    
    if q:
        p += X(0)

    p += X(0)
    p += MEASURE(0, ro[0])
    return compile_and_run(p, qc, 'ro')

def or_operation(q1, q2):
    """Дизъюнкция"""
    p = Program()
    ro = p.declare('ro', 'BIT', 1)
    qc = get_qc('8q-qvm')

    if q1:
        p += X(0)
    if q2:
        p += X(1)

    p += X(0)
    p += X(1)
    p += CCNOT(0, 1, 2)
    p += X(0)
    p += X(1)
    p += X(2)
    
    p += MEASURE(2, ro[0])
    return compile_and_run(p, qc, 'ro')

def nor_operation(q1, q2):
    """Стрелка Пирса"""
    p = Program()
    ro = p.declare('ro', 'BIT', 1)
    qc = get_qc('8q-qvm')

    if q1:
        p += X(0)
    if q2:
        p += X(1)

    p += X(0)
    p += X(1)
    p += CCNOT(0, 1, 2)
    p += X(0)
    p += X(1)
    
    p += MEASURE(2, ro[0])
    return compile_and_run(p, qc, 'ro')

def and_operation(q1, q2):
    """Конъюнкция"""
    p = Program()
    ro = p.declare('ro', 'BIT', 1)
    qc = get_qc('8q-qvm')

    if q1:
        p += X(0)
    if q2:
        p += X(1)

    p += CCNOT(0, 1, 2)
    
    p += MEASURE(2, ro[0])
    return compile_and_run(p, qc, 'ro')

def nand_operation(q1, q2):
    """Штрих Шеффера"""
    p = Program()
    ro = p.declare('ro', 'BIT', 1)
    qc = get_qc('8q-qvm')

    if q1:
        p += X(0)
    if q2:
        p += X(1)

    p += CCNOT(0, 1, 2)
    p += X(2)
    p += MEASURE(2, ro[0])
    return compile_and_run(p, qc, 'ro')    