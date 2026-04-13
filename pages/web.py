import functions
import streamlit as st

st.set_page_config(
    page_title="할일 목록 관리",
)


if "todo_list" not in st.session_state:
    try:
        st.session_state.todo_list = functions.file_read()
    except FileNotFoundError:
        st.session_state.todo_list = []
        functions.file_write(st.session_state.todo_list)


def add_todo():
    if st.session_state.TODO:
        st.session_state.todo_list.append(st.session_state.TODO)
        functions.file_write(st.session_state.todo_list)
        st.session_state.TODO = ""


def complete_todo(index):
    del st.session_state.todo_list[index]
    functions.file_write(st.session_state.todo_list)


st.title("Todo App :heavy_check_mark:")
st.write("당신의 **생산성**을 크게 향상시킵니다.")


st.text_input(
    label="",
    placeholder="할일을 입력하고 Enter키를 누르세요.",
    key="TODO",
    on_change=add_todo,
)

for i, todo in enumerate(st.session_state.todo_list):
    st.checkbox(label=todo, on_change=complete_todo, args=(i,))
