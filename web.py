import streamlit as st
import functions
def add_todo():
    todo=st.session_state["new_todo"]
    todos1 = functions.get_todo()
    todos1.append(todo+"\n")
    functions.write_todo(todos1)

todos=functions.get_todo()

st.title("Todo App")
st.subheader("Todos")

for i in todos:
    checkbox=st.checkbox(i,key=i)
    if checkbox:
        todos.remove(i)
        functions.write_todo(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="Enter a todo",placeholder="Add new todo ...",on_change=add_todo,key="new_todo")