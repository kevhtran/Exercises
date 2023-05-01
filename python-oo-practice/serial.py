"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """Make a new generator, starting at start."""
        self.start = self.next = start
    
    def generate(self):
        """Returns next serial"""
        self.next += 1
        return self.next
    
    def reset(self):
        """Returns original start number"""
        self.next = self.start
        return self.next




