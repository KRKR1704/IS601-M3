"""Operation functions for the calculator"""
class Operations:
    """
    This is the container which has the basic math operations
    """
    @staticmethod
    def addition(a:float,b:float)->float:
        """
        This methos take 2 numbers and return their sum
        """
        return a+b
    
    @staticmethod
    def subtraction(a:float,b:float)->float:
        """
        This methos take 2 numbers and return their difference
        """
        return a-b
    
    @staticmethod
    def multiplication(a:float,b:float)->float:
        """
        This methos take 2 numbers and return their product
        """
        return a*b
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """
        This methos take 2 numbers and return their quotient
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a/b