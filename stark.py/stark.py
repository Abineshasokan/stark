import streamlit as st


st.set_page_config(page_title="Editor Portfolio", page_icon=":clapper:", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])


if page == "Home":
    st.title("🎬 Editor & Designer Portfolio")
    st.subheader("Hi, I'm Abinesh - A Passionate Video Editor & Creative Designer")
    st.write("""
    Welcome to my portfolio. Here, you can explore my work in video editing, graphic design, and creative projects.
    """)

    st.header("About Me")
    st.write("""
    I'm a video editor and designer skilled in turning ideas into stunning visuals. 
    I specialize in editing, motion graphics, branding, and storytelling. 
    Let's collaborate and create something amazing!
    """)

    st.header("Skills")
    st.write("""
    - 🎞 Video Editing (Premiere Pro, After Effects)
    - 🎨 Graphic Design (Photoshop, Illustrator)
    - 🚀 Motion Graphics
    - 📖 Storytelling
    - 🎯 Branding & Visual Identity
    """)



elif page == "Projects":
    st.title("🎥 My Projects")
    st.subheader("my channel link")
  

    st.markdown("[Visit my youtube channel ](https://youtube.com/@timetodayshorts?si=j5rh2jVDMD2JRziC)")


    col1, col2, col3 = st.columns(3)

    with col1:
       
        st.subheader("Project 1")
        st.write("Short description.")
        st.video("https://youtube.com/shorts/ACz5D9UKyHA?si=NYmupwIGohxgrz12")
        st.markdown("[Visit my youtube video ](https://youtube.com/shorts/ACz5D9UKyHA?si=NYmupwIGohxgrz12)")

    with col2:
    
        st.subheader("Project 2")
        st.write("Short description.")
        st.video("https://youtube.com/shorts/khKi9T0i3TI?si=qEardU-zCLA6ezBE")
        st.markdown("[Visit my youtube video](ttps://youtube.com/shorts/khKi9T0i3TI?si=qEardU-zCLA6ezBE)")




elif page == "Contact":
    st.title("📬 Contact Me")

    st.write("Feel free to reach out if you'd like to work together or just say hi!")

    contact_form = """
    <form action="" method="POST">
         <input type="text" name="name" placeholder="Your Name" required>
         <input type="email" name="email" placeholder="Your Email" required>
         <textarea name="message" placeholder="Your Message" required></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    st.markdown("""
    <style>
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            width: 100%;
            border: none;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)


st.write("Emails:abineshabinesh46406@gmail.com")
st.write("Contact number :9342601198")