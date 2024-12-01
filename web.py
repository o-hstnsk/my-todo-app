import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("This is my Todo app")
st.subheader("Can you believe that?!")
st.write("It's just WOW. I literally did it myself. So proud.")
st.write("Now I can put here any shit I want. No one can stop me.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add new todo: ",
              on_change=add_todo, key='new_todo')

