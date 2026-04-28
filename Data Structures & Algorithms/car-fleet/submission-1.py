class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = list(zip(positions, speeds))
        cars.sort(reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)