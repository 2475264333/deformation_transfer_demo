import streamlit as st
import time

# define the paths of the photos
photo_s0_path = "demo/s0.png"
photo_s1_path = "demo/s1.png"
photo_t0_path = "demo/t0.png"
photo_t1_path = "demo/t1.png"
photo_t0_new_path = "demo/t0_new.png"
photo_t0_new_align_deformed_path = "demo/t0_new_align_deformed.png"
photo_t0_new_deformed_path = "demo/t0_new_deformed.png"

# set the title of the page
st.title("Deformation Transfer")
st.markdown("<hr>", unsafe_allow_html=True)

# add some custom CSS styles to make the title larger
st.markdown(
    """
    <style>
    .title {
        font-size: 4rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# display the first photo
st.markdown("## Source Model")
image1 = st.image(photo_s0_path, width = 200)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## Target Model (Easy Version)")
image2 = st.image(photo_t0_path, width = 200)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## Target Model (Difficult Version && Align First)")
image3 = st.image(photo_t0_new_path, width = 200)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("## Target Model (Difficult Version && Exchange Input)")
image4 = st.image(photo_t0_new_path, width = 200)

# loop through displaying both photos
while True:
    # wait for 5 seconds
    time.sleep(1)

    # display the second photo
    image1.image(photo_s1_path, width = 200)
    image2.image(photo_t1_path, width = 200)
    image3.image(photo_t0_new_align_deformed_path, width = 200)
    image4.image(photo_t0_new_deformed_path, width = 200)

    # wait for 5 seconds
    time.sleep(1)

    # display the first photo
    image1.image(photo_s0_path, width = 200)
    image2.image(photo_t0_path, width = 200)
    image3.image(photo_t0_new_path, width = 200)
    image4.image(photo_t0_new_path, width = 200)