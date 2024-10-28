class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    
        for _ in range(iterations):
           der = 2 * init
           init = init - learning_rate * der

        return round(init,5)