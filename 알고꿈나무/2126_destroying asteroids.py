class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        #quicksort to sort in ascending order
        for asteroid in asteroids:
            if asteroid > mass:
                # find the most optimal, local solution
                return False 
            mass += asteroid

        return True
    # Greedy Algorithms