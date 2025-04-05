import random
from exceptions import InvalidBitsError

class Bits(object):
    """The main parent class that implements a list of bits."""
    def __init__(self, bits):
        self.bits = bits

    def get_bits(self):
        """Getter method for the class.
        Returns the list of bits."""
        return self.bits
    
    def set_bits(self, newbits):
        """Setter method that validates the bits first."""
        self.validate(newbits)
        self.bits = newbits

    def validate(self, bits):
        """Makes sure there are the same number of bits in the provided list as the instance's ``bits`` property and that they are all 0 or 1.
        Returns True if the bits are valid, otherwise raises an InvalidBitsError."""
        if len(self.bits) != len(bits):
            raise InvalidBitsError("The number of bits must be " + str(len(self.bits)))
        for bit in bits:
            if bit not in [0, 1]:
                raise InvalidBitsError("Bits must be either 0 or 1")
            return True
        
    def pad(self, otherBits):
        """Pads two lists of bits with zeroes to make them the same length."""
        selfLen,otherLen = len(self.bits),len(otherBits)
        if selfLen > otherLen:
            for i in range(selfLen - otherLen):
                otherBits.insert(0,0)
        if selfLen < otherLen:
            for i in range(otherLen - selfLen):
                self.bits.insert(0,0)
        if selfLen == otherLen:
            pass
        return otherBits


    def andGate(self, otherBits):
        """Implements a bitwise AND gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results

    def orGate(self, otherBits):
        """Implements a bitwise OR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results

    def nandGate(self, otherBits):
        """Implements a bitwise NAND gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(0)
                else:
                    results.append(1)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(0)
                else:
                    results.append(1)
        return results

    def notGate(self):
        """Implements a bitwise NOT gate.
        Operates on the Bits instance it was called from."""
        results = []
        for i in range(len(self.bits)):
            if self.bits[i]:
                results.append(0)
            else:
                results.append(1)
        return results

    def norGate(self,otherBits):
        """Implements a bitwise NOR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits.bits[i]:
                    results.append(0)
                else:
                    results.append(1)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits[i]:
                    results.append(0)
                else:
                    results.append(1)
        return results
    
    def xorGate(self,otherBits):
        """Implements a bitwise XOR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(0)
                elif self.bits[i] and not otherBits.bits[i]:
                    results.append(1)
                elif not self.bits[i] and otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(0)
                elif self.bits[i] and not otherBits[i]:
                    results.append(1)
                elif not self.bits[i] and otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results
    
    def xnorGate(self, otherBits):
        """Implements a bitwise XNOR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(1)
                elif not self.bits[i] and not otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(1)
                elif not self.bits[i] and not otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results


class TwoBits(object):
    """Implements two single bits and lets you do operations with them."""
    def __init__(self, bit1, bit2):
        self.bits = []
        self.bit = bit1
        self.bits.append(bit1)
        self.bits.append(bit2)

    def get_bits(self):
        """Gets the list of bits from the class instance."""
        return self.bits

    def set_bits(self, newbits):
        """Validates the new bits and then sets them."""
        self.validate(newbits)
        self.bits = newbits

    @staticmethod
    def validate(bits):
        """Makes sure there are only two bits in the provided list and that they are all 0 or 1."""
        if len(bits) != 2:
            raise InvalidBitsError("The TwoBits class can only store two bits. Try using the Bits class.")
        for bit in bits:
            if bit not in [0, 1]:
                raise InvalidBitsError("Bits must be either 0 or 1.")

    def andGate(self):
        """Implements a basic AND gate.
        Operates on the TwoBits instance it was called from."""
        if self.bits[0] and self.bits[1]:
            return 1
        return 0

    def orGate(self):
        """Implements a basic OR gate.
        Operates on the TwoBits instance it was called from."""
        if self.bits[0] or self.bits[1]:
            return 1
        return 0

    def notGate(self):
        """Implements a basic NOT gate.
        Operates on the TwoBits instance it was called from."""
        results = []
        for i in range(len(self.bits)):
            if self.bits[i] == 0:
                results.append(1)
            else:
                results.append(0)
        return results

    def nandGate(self):
        """Implements a basic NAND gate.
        Operates on the TwoBits instance it was called from."""
        if self.notGate() and self.notGate():
            return 1
        return 0

    def norGate(self):
        """Implements a basic NOR gate.
        Operates on the TwoBits instance it was called from."""
        if self.bits[0] or self.bits[1]:
            return 0
        return 1

    def xorGate(self):
        """Implements a basic XOR gate.
        Operates on the TwoBits instance it was called from."""
        if self.bits[0] and not self.bits[1]:
            return 1
        elif not self.bits[0] and self.bits[1]:
            return 1
        return 0

    def xnorGate(self):
        """Implements a basic XNOR gate.
        Operates on the TwoBits instance it was called from."""
        if self.bits[0] and self.bits[1]:
            return 1
        elif not self.bits[0] and not self.bits[1]:
            return 1
        return 0


class RandomBits(Bits):
    """Like ``Bits``, except the bits are randomly generated."""
    def __init__(self, num_of_bits):
        self.bits = [random.randrange(0, 2) for _ in range(num_of_bits)]

    def pad(self, otherBits):
        """Pads two lists of bits with zeroes to make them the same length."""
        selfLen,otherLen = len(self.bits),len(otherBits)
        if selfLen > otherLen:
            for i in range(selfLen - otherLen):
                otherBits.insert(0,0)
        if selfLen < otherLen:
            for i in range(otherLen - selfLen):
                self.bits.insert(0,0)
        if selfLen == otherLen:
            pass
        return otherBits

    def get_bits(self):
        """Getter method for the class.
        Returns the list of bits."""
        return self.bits

    def set_bits(self, newbits):
        """Setter method that validates the bits first."""
        self.validate(newbits)
        self.bits = newbits

    def validate(self, bits):
        """Makes sure there are the same number of bits in the provided list as the instance's ``bits`` property and that they are all 0 or 1.
        Returns True if the bits are valid, otherwise raises an InvalidBitsError."""
        if len(self.bits) != len(bits):
            raise InvalidBitsError("The number of bits must be " + str(len(self.bits)))
        for bit in bits:
            if bit not in [0, 1]:
                raise InvalidBitsError("Bits must be either 0 or 1")
            return True

    def andGate(self, otherBits):
        """Implements a bitwise AND gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results

    def orGate(self, otherBits):
        """Implements a bitwise OR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results

    def nandGate(self, otherBits):
        """Implements a bitwise NAND gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(0)
                else:
                    results.append(1)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(0)
                else:
                    results.append(1)
        return results

    def notGate(self):
        """Implements a bitwise NOT gate."""
        results = []
        for i in range(len(self.bits)):
            if self.bits[i]:
                results.append(0)
            else:
                results.append(1)
        return results

    def norGate(self,otherBits):
        """Implements a bitwise NOR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits.bits[i]:
                    results.append(0)
                else:
                    results.append(1)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] or otherBits[i]:
                    results.append(0)
                else:
                    results.append(1)
        return results
    
    def xorGate(self,otherBits):
        """Implements a bitwise XOR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(0)
                elif self.bits[i] and not otherBits.bits[i]:
                    results.append(1)
                elif not self.bits[i] and otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(0)
                elif self.bits[i] and not otherBits[i]:
                    results.append(1)
                elif not self.bits[i] and otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results
    
    def xnorGate(self, otherBits):
        """Implements a bitwise XNOR gate."""
        results = []
        if type(otherBits) == Bits:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits.bits[i]:
                    results.append(1)
                elif not self.bits[i] and not otherBits.bits[i]:
                    results.append(1)
                else:
                    results.append(0)
        else:
            for i in range(len(self.bits)):
                if self.bits[i] and otherBits[i]:
                    results.append(1)
                elif not self.bits[i] and not otherBits[i]:
                    results.append(1)
                else:
                    results.append(0)
        return results

