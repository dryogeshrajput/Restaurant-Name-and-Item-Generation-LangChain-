import streamlit as st
from LangChainHelper import get_res_name_item

st.title("Restaurant Name and Menu Generation")

cuisines = ["Indian", "Italian", "Mexican", "Japanese", "French", "Chinese", "Thai", "Spanish"]
cuisine = st.sidebar.selectbox("Pick a Cuisine", cuisines)

if cuisine:
    response = get_res_name_item(cuisine)

    restaurant_name = response['restaurant_name'].strip()

    if restaurant_name:  # Check if the restaurant name is not empty
        st.header(restaurant_name)

        menu_items = response['menu_items'].strip().split(",")
        st.header("** Menu Items **")

        for item in menu_items:
            st.write(" ", item)
    else:
        st.warning("No restaurant name available for the selected cuisine.")
