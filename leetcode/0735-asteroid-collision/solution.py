class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = []
        free = []
        i = 0
        for asteroid in asteroids:
            if asteroid > 0:
                right.append(asteroid)
            else:
                asteroid *= -1
                destroyed = False
                while len(right) > 0:
                    if right[-1] > asteroid:
                        destroyed = True
                        break
                    elif right[-1] == asteroid:
                        destroyed = True
                        del right[-1]
                        break
                    else:
                        del right[-1]
                if not destroyed:
                    free.append(asteroid * -1)
        return free + right


        
