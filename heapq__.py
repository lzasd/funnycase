import heapq

heap = []
heapq.heappush(heap,[1,2,3])
heapq.heappush(heap,[2,3,2])
heapq.heappush(heap,[1,2,3])
print(heap)
l1 = [100,1,3,2,5,3,6,4,3,99,20,10,11,12,13,14]
print(heapq.heapify(l1))
print(l1)