def get_todo(filename="todos.txt"):
    with open(filename,"r") as f:
        return f.readlines()

def write_todo(content,filename="todos.txt"):
    with open(filename, "w") as f:
        f.writelines(content)
