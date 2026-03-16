nums = [1,2,3,2]

cache = {}
result = []
for i in nums:
    cache[i] = cache.get(i, 0) + 1
print(cache)
for k,v in cache.items():
    if v == 1:
        result.append(k)
print(sum(result))
