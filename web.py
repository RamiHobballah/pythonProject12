import streamlit as st
import needs


todos = needs.get_todos()


def add_todo():
    new_todo = st.session_state["-add-todo"]
    todos.append(new_todo+'\n')
    needs.write_todos(todos)


def delete_todo():
    new_todo = st.session_state[todo]
    todos.remove(new_todo)
    needs.write_todos(todos)

st.title("To-dos")
st.text_input(label="", placeholder="Enter your todo", on_change=add_todo, key="-add-todo")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        needs.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


