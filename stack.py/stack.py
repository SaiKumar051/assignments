# def newStack():
#     stack = []
#     return stack

# def isEmpty(stack): # checking if the stack is empty
#     return len(stack) == 0


# # adding elements
# def push(stack,item):
#     stack.append(item)

# # popping elements
# def pop(stack):
#     if isEmpty(stack):
#         return("nothing to pop")
#     else:
#         stack.pop()

# stack = newStack()
# push(stack, "SR")
# push(stack, "AS")
# push(stack, "MC")
# push(stack, "PNM")
# push(stack, "SR")
# push(stack, "RP")
# push(stack, "SR")
# pop(stack)
# push(stack, "AS")
# print(stack)



class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "nothing to pop"
        else:
            self.stack.pop()

stack = Stack()

stack.push("SR")
stack.push("AS")
stack.push("MC")
stack.push("PNM")
stack.push("SR")
stack.push("RP")
stack.push("SR")
stack.pop()
stack.push("AS")

print(stack.stack)
