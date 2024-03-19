

class TimeMap:
    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = {}
        self.dct[key][value] = timestamp
        print(self.dct)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ""
        value_ts = self.dct[key]
        sorted_ts = dict(
            sorted(value_ts.items(), key=lambda item: item[1], reverse=True)
        )

        for value, ts_prev in sorted_ts.items():
            if ts_prev <= timestamp:
                return value
        return ""


TimeMap = TimeMap()
TimeMap.set("foo", "bar", 1)
TimeMap.get("foo", 1)
TimeMap.get("foo", 3)
TimeMap.set("foo", "bar2", 4)
TimeMap.get("foo", 4)
TimeMap.get("foo", 5)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
