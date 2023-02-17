from cl_Stack import Stack

to_check1 = "[[{())}]"

def if_balanced(to_check):
    brackets = {")":"(", "}":"{", "]":"["}
    temp_stack = Stack()
    for item in to_check:
        if temp_stack.is_empty():
            temp_stack.push(item)
        elif brackets.get(item) == temp_stack.peek():
            temp_stack.pop()
        else:
            temp_stack.push(item)
           
    if temp_stack.is_empty():
        return "сбалансировано"
    else:
        return "не сбалансировано" 

if __name__ == "__main__":
    print(if_balanced(to_check1))
   

