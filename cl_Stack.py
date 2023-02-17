class Stack:
    def __init__(self):
        self.body = []

    def is_empty(self):
        if len(self.body) == 0:
            return True
        else:
            return False

    def push(self, new_elem):
        self.body.append(new_elem)
        return

    def pop(self):
        x = self.body.pop()
        return x

    def peek(self):
        return self.body[len(self.body)-1]  

    def size(self):
        return len(self.body)

    def __str__(self):     
        return f'{self.body}'   



