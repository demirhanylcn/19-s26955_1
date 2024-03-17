class SquareGenerator:
    def generate_square(self,start,end):

        if end < start:
            raise ValueError('end can not be smaller than start')

        generated_squares = []
        for i in range(start, end):
            generated_squares.append(i ** 2)
        return generated_squares

