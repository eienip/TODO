import streamlit as st

st.set_page_config(
    page_title="할일 목록 관리",
)

home = st.Page(page="pages/web.py", title="TODO", default=True)
about = st.Page(page="pages/about.py", title="MANUAL")

pg = st.navigation([home, about])

pg.run()
