class TimeMap:

    def __init__(self):
        self.mp = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp: self.mp[key] = []
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp: return ""
        store = self.mp[key]
        low, high, ans = 0, len(store) - 1, ""
        while low <= high:
            mid = low + (high - low) // 2
            if store[mid][0] <= timestamp:
                ans = store[mid][1]
                low = mid + 1
            else: high = mid - 1
        return ans

        
