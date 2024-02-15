def get_todos(filepath = "todos.txt"):
    """
    Read a text file and reads the to-do items
    """
    with open("todos.txt", 'r') as file:
        lines = file.readlines()
    return lines
def write_todos(todos, filepath = "todos.txt"):
    """
    Write the items
    """
    with open("todos.txt", 'w') as file:
        write = file.writelines(todos)
