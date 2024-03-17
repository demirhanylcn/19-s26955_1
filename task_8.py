import task_5


class CubicGenerator(task_5.SquareGenerator):

    def generate_cube(self, start, end):
        generated_cubes = []
        for i in range(start, end):
            generated_cubes.append(i ** 3)
        return generated_cubes
