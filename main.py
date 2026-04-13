import streamlit as st

home = st.Page(page="pages/web.py", title="TODO", default=True)
about = st.Page(page="pages/about.py", title="MANUAL")

pg = st.navigation([home, about])

pg.run()
