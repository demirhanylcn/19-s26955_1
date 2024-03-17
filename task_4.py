import math
import task_3

SG = task_3.SquareGenerator
squares = SG.generate_square(SG,1,10)
for square in squares:
    print(math.sqrt(square))