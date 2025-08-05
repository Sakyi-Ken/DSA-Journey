# Queue Interleaving
from collections import deque

def interleave_queue(queue):
  half_size = len(queue) // 2
  first_half = deque()

  for _ in range(half_size):
    first_half.append(queue.popleft())
  
  while first_half:
    queue.append(first_half.popleft())
    if queue:
      queue.append(queue.popleft())

  return queue

# Example usage
print(interleave_queue(deque([1, 2, 3, 4, 5, 6]))) # Output: [1, 4, 2, 5, 3, 6]

# Problem2: Moving Average from Data Stream
class MovingAverage:
  def __init__(self, size):
    self.queue = deque()
    self.size = size
    self.total = 0

  def calculate_moving_average(self, val):
    if len(self.queue) == self.size:
      self.total -= self.queue.popleft()
    self.queue.append(val)
    self.total += val
    return round(self.total / len(self.queue), 2)

# Example
moving_average = MovingAverage(5)

for _ in range(8):
  print(moving_average.calculate_moving_average(_))

# Wrong Approach
# Firstly I tackled this problem by combining queue1 and queue2 to make one
# And found the half_size after combining

# Right Approach
# See the two queues already divided queues and the half_size is the length
# of one of the queues since they are of the same size.
def interleave_queues(queue1, queue2):
  interleave_queue = deque()
  # implement this
  half_size = len(queue1)
      
  for i in range(half_size):
    interleave_queue.append(queue1.popleft())
    interleave_queue.append(queue2.popleft())
      
  return list(interleave_queue)

# Test cases
print(interleave_queues(deque([1, 2, 3, 4, 5]), deque([6, 7, 8, 9, 10]))) 
# Expected output: [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
print(interleave_queues(deque([1]), deque([2])))
# Expected output: [1, 2]
print(interleave_queues(deque([1, 3, 5]), deque([2, 4, 6]))) 
# Expected output: [1, 2, 3, 4, 5, 6]


class TextMovingAverage:
  def __init__(self, size):
    self.queue = deque()
    self.size = size
    self.total = 0

  def calculate_moving_average(self, word):
    # implement this
    if len(self.queue) == self.size:
      self.total -= self.queue.popleft()
    self.queue.append(len(word))
    self.total += len(word)
    return round(self.total / len(self.queue), 2)
        


# Test samples
ma = TextMovingAverage(3)
print(ma.calculate_moving_average('one'))  # Expected: 3.0
print(ma.calculate_moving_average('two'))  # Expected: 3.0
print(ma.calculate_moving_average('three'))  # Expected: 3.67
print(ma.calculate_moving_average('four'))  # Expected: 4.0
print(ma.calculate_moving_average('five'))  # Expected: 4.33
print(ma.calculate_moving_average('six'))  # Expected: 3.67