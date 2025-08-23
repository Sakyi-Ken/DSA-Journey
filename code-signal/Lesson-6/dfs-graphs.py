def DFS(graph, start, visited):
  visited.add(start)
  print(start, end=' ')
  
  for next_node in graph[start]:
    if next_node not in visited:
      DFS(graph, next_node, visited)

graph = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A']),
  'D': set(['B']),
  'E': set(['B']),
}

visited = set()
DFS(graph, 'A', visited)  # Output: A B D E C

graph = {
  'Washington': set(['California', 'Nevada']),
  'California': set(['Washington', 'Oregon']),
  'Nevada': set(['Washington', 'Oregon']),
  'Oregon': set(['California', 'Nevada'])
}

def DFS(graph, start, visited):
  if start in visited:  # if the node has already been visited, just return the visited set
    return
  
  visited.add(start)
  print(start, end=" ")

  for state in graph[start]:
    if state not in visited:
      DFS(graph, state, visited)

# Call the DFS function starting with 'Washington'
visited = set()
DFS(graph, 'Washington', visited)  # Output: Washington Nevada Oregon California
print('\nVisited states:', visited)  # Print all visited states


university_courses = {
  'Math': set(['Physics', 'Computer Science']),
  'Physics': set(['Math', 'Chemistry']),
  'Chemistry': set(['Physics']),
  'Computer Science': set(['Math']),
}

def DFS(courses, start_course, passed_courses):
  """
  Function implementing the DFS algorithm to traverse the graph.
  """
  if start_course in passed_courses: # Check if the course was taken earlier
    return

  passed_courses.add(start_course) # Add the course to the set of passed courses
  print(start_course, end=' --> ')

  for next_course in courses.get(start_course, []):
    DFS(courses, next_course, passed_courses)

passed_courses = set()
# Call the DFS function, start the traversal with 'Math'
DFS(university_courses, 'Math', passed_courses)