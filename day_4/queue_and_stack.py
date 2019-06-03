rzeczy = ["doniczka", "kwiatek", "ziemia", "woda"]

# FIFO - kolejka
queue = rzeczy.copy()
element = queue.pop(0)
print(element)
element = queue.pop(0)
print(element)
queue.append("grabie")
element = queue.pop(0)
print(element)
element = queue.pop(0)
print(element)
element = queue.pop(0)
print(element)
print("---------------")

# LIFO - stos
stack = rzeczy.copy()
element = stack.pop()
print(element)
element = stack.pop()
print(element)
stack.append("grabie")
element = stack.pop()
print(element)
element = stack.pop()
print(element)
element = stack.pop()
print(element)