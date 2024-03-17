from abc import ABC,abstractmethod

class SquareGenerator(ABC):
    @abstractmethod
    def generate_square(self,start,end):
        pass


class CubicGenerator(SquareGenerator):
    def generate_square(self,start,end):
        generated_squares = []
        for i in range(start, end):
            generated_squares.append(i ** 2)
        return generated_squares