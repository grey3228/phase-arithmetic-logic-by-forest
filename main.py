from phase_logic import *
from arithmetic_operations import *
from numpy import array

def main():    
    test_not()
    test_or()
    test_nor()
    test_and()
    test_nand()
    test_xor()

    test_increment()
    test_decrement()
    test_sum()
    test_sign_inversion()

def test_not():
    print(f"not(0) = {not_operation(0)}")
    print(f"not(1) = {not_operation(1)}")
    sep()

def test_or():
    print(f"0 or 0 = {or_operation(0, 0)}")
    print(f"0 or 1 = {or_operation(0, 1)}")
    print(f"1 or 0 = {or_operation(1, 0)}")
    print(f"1 or 1 = {or_operation(1, 1)}")
    sep()

def test_nor():
    print(f"0 nor 0 = {nor_operation(0, 0)}")
    print(f"0 nor 1 = {nor_operation(0, 1)}")
    print(f"1 nor 0 = {nor_operation(1, 0)}")
    print(f"1 nor 1 = {nor_operation(1, 1)}")
    sep()

def test_and():
    print(f"0 and 0 = {and_operation(0, 0)}")
    print(f"0 and 1 = {and_operation(0, 1)}")
    print(f"1 and 0 = {and_operation(1, 0)}")
    print(f"1 and 1 = {and_operation(1, 1)}")
    sep()

def test_nand():
    print(f"0 nand 0 = {nand_operation(0, 0)}")
    print(f"0 nand 1 = {nand_operation(0, 1)}")
    print(f"1 nand 0 = {nand_operation(1, 0)}")
    print(f"1 nand 1 = {nand_operation(1, 1)}")
    sep()

def test_xor():
    print(f"0 xor 0 = {xor_operation(0, 0)}")
    print(f"0 xor 1 = {xor_operation(0, 1)}")
    print(f"1 xor 0 = {xor_operation(1, 0)}")
    print(f"1 xor 1 = {xor_operation(1, 1)}")
    sep()

def test_increment():
    qubit_register = array([0, 0, 0, 0])
    for i in range (0, 16):
        incremented_qubit_register = increment_operation(qubit_register)
        print(f"increment: {qubit_register}++ = {incremented_qubit_register}")
        qubit_register = incremented_qubit_register
    sep()

def test_decrement():
    qubit_register = array([0, 0, 0, 0])
    for i in range (0, 16):
        decremented_qubit_register = decrement_operation(qubit_register)
        print(f"decrement: {qubit_register}-- = {decremented_qubit_register}")
        qubit_register = decremented_qubit_register
    sep()

def test_sum():
    print(f"sum: [0, 0, 0, 0] + [0, 0, 0, 0] = {sum_operation(array([0, 0, 0, 0]), array([0, 0, 0, 0]))}")
    print(f"sum: [0, 0, 0, 0] + [1, 0, 0, 0] = {sum_operation(array([0, 0, 0, 0]), array([1, 0, 0, 0]))}")
    print(f"sum: [0, 0, 0, 1] + [1, 0, 0, 0] = {sum_operation(array([0, 0, 0, 1]), array([1, 0, 0, 0]))}")
    print(f"sum: [1, 0, 0, 1] + [1, 0, 0, 0] = {sum_operation(array([1, 0, 0, 1]), array([1, 0, 0, 0]))}")
    print(f"sum: [1, 1, 0, 1] + [1, 0, 0, 0] = {sum_operation(array([1, 1, 0, 1]), array([1, 0, 0, 0]))}")
    print(f"sum: [1, 1, 0, 1] + [1, 0, 1, 0] = {sum_operation(array([1, 1, 0, 1]), array([1, 0, 1, 0]))}")
    sep()

def test_sign_inversion():
    qubit_register = array([0, 0, 0, 0])
    for i in range (0, 16):
        qubit_register = increment_operation(qubit_register)
        inversed_qubit_register = sign_inversion_operation(qubit_register)
        print(f"sign inversion: ~{qubit_register} = {inversed_qubit_register}")
    sep()

def sep():
    print("\n----//----\n")

if __name__ == "__main__":
    main()