import streamlit as st
from functions.webcam import play_webcam
from functions.video_upload import upload_video, detect_video, save_file
from functions.upload_image import image_upload, image_detection
from functions.redundant.upload_multiple import upload_multiple
from streamlit_option_menu import option_menu
from pathlib import Path
from functions import settings, helper

st.set_page_config(layout='wide')




# web cam
# st.markdown(""" <style> .font {
#     font-size:20px ; font-family: 'Cooper Black'; color: black;} 
#     </style> """, unsafe_allow_html=True)
# st.markdown('<p class="font">Open webcam</p>', unsafe_allow_html=True)






# Upper sidebar
with st.sidebar:
    choose = option_menu("Upload Menu", [ "Webcam","Video","Image", "Info"],
                         icons=['camera-video', 'film', 'camera', 'clipboard'],
                         menu_icon="cast", default_index=0,
                         styles={
                             "container": {"padding": "5!important", "background-color": "white"},
                             "icon": {"color": "black", "font-size": "25px"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                          "--hover-color": "orange"}
                         }
                         )
    
if choose == "Webcam":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: black;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">WebCam</p>', unsafe_allow_html=True)
    # confidence chooser
    confidence = float(st.slider(
    "Select Model Confidence", 25, 100, 40)) / 100
    # path
    model_path = Path(settings.DETECTION_MODEL)
    # Load Pre-trained ML Model
    try:
        model = helper.load_model(model_path)
    except Exception as ex:
        st.error(f"Unable to load model. Check the specified path: {model_path}")
        st.error(ex)
    
    play_webcam(confidence, model)
    



elif choose == "Video":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: black;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Video</p>', unsafe_allow_html=True)

    # path
    model_path = Path(settings.DETECTION_MODEL)

    # Load Pre-trained ML Model
    try:
        model = helper.load_model(model_path)
    except Exception as ex:
        st.error(f"Unable to load model. Check the specified path: {model_path}")
        st.error(ex)


    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100
    
    detect_video(confidence=confidence, model=model)
    

    
    


elif choose == "Image":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: black;} 
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload an Image</p>', unsafe_allow_html=True) # For image
    uploaded_file = image_upload()

    # Run object detection when an image or video is uploaded
    if uploaded_file is not None:
        # Perform object detection using YOLOv5
        detected_output = image_detection(uploaded_file)

        # # Display the original and detected images/videos in the app
        # if detected_output is not None:
        #         st.image(detected_output, caption='Detected Objects', use_column_width=True)


# elif choose == "Multiple Images":
#     st.markdown(""" <style> .font {
#         font-size:30px ; font-family: 'Cooper Black'; color: black;} 
#         </style> """, unsafe_allow_html=True)
#     st.markdown('<p class="font">Multiple Images</p>', unsafe_allow_html=True)
#     upload_multiple()


elif choose=="Info":
    with st.sidebar:
        info = option_menu("Info Menu", [ "About the app","Developer"],
                            icons=['book', 'person lines fill'],
                            menu_icon="cast", default_index=0,
                            styles={
                                "container": {"padding": "5!important", "background-color": "white"},
                                "icon": {"color": "black", "font-size": "25px"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                            "--hover-color": "orange"},
                                            "nav-link-selected": {"background-color": "orange"},
                            }
                            )


    if info == "About the app":
        st.markdown(""" <style> .font {
            font-size:30px ; font-family: 'Cooper Black'; color: black;} 
            </style> """, unsafe_allow_html=True)
        st.markdown('<h2 class="font"> About the App </h2>', unsafe_allow_html=True)
        st.markdown('''
        <style>
            .nice-div {
            font-family: 'Pacifico', cursive;
            font-size: 20px;
            color: #003366;
            padding: 10px;
            margin: 20px;
            border: 2px solid #003366;
            border-radius: 10px;
            }
            .links {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            a {
                margin: 10px;
                color: #000;
                text-decoration: none;
            }
        </style>''', unsafe_allow_html= True)

        st.write("This application... ")

    elif info == "Developer":
        st.markdown(""" <style> .font {
                font-size:30px ; font-family: 'Cooper Black'; color: black;} 
                </style> """, unsafe_allow_html=True)
        st.markdown('<h2 class="font"> About the Developer </h2>', unsafe_allow_html=True)
        st.markdown('''
        <style>
            .nice-div {
            font-family: 'Pacifico', cursive;
            font-size: 20px;
            color: #003366;
            padding: 10px;
            margin: 20px;
            border: 2px solid #003366;
            border-radius: 10px;
            }
            .links {
                display: flex;
                font-family: 'Pacifico', cursive;
                font-size: 20px;
                color: #003366;
                
                height: 100vh;
            }
            a {
                margin: 10px;
                color: #000;
                text-decoration: none;
            }
        </style>''', unsafe_allow_html= True)
        st.markdown('''
        <div class="nice-div">          
                    <br/>   
                    I am a passionate and results-driven Data Scientist with a strong background in analyzing complex data sets and deriving valuable insights to drive business growth. With a deep understanding of machine learning algorithms, and data visualization techniques,
                    I thrive on solving intricate problems and uncovering hidden patterns to optimize decision-making processes.
                    <br/>

        <b> Education: </b>
                    <br/>
                    I am an Engineering student at the University of Ibadan. My academic journey has assisted in developing a solid foundation in mathematics, engineering, programming and problem solving skills, which I have further honed through hands-on experience in various real-world projects.

        <b> Professional Experience: </b>
                    <br/>
                    I have 3 years of experience as a Data Scientist, working with diverse organizations as an intern. In my previous role at Zummit Africa, I successfully worked on several projects that involved developing predictive models and Natural language processing. My work directly contributed to the success of my team.

        Furthermore, I collaborated closely with cross-functional teams, including data engineers and machine learning engineers, to work on numerous projects including Large Language Models and computer vision. My expertise in programming languages such as Python and SQL, coupled with my proficiency in data manipulation and analysis tools, allowed me to effectively extract, clean, and transform large datasets for analysis.

        <b> Skills: </b>
        <ul>
                <li> command line </li>
                <li> Data analysis and interpretation </li>
                <li> Machine learning algorithms and predictive modeling </li>
                <li> ComputerVision </li>
                <li> Data visualization </li>
                <li> Programming languages: Python, SQL </li>
                <li> Data manipulation and analysis tools: Pandas, NumPy </li>
                <li> Data Visualization tools: Matplotlib, seaborn </li>
                <li> Deep learning framework:PyTorch </li>
                <li> Data extraction and transformation </li>
        </ul>

        If you are seeking a dedicated and experienced Data Scientist who can bring valuable insights to your organization, feel free to reach out. I am eager to explore new opportunities, contribute to impactful projects, and be part of a team that shares a vision for harnessing the power of data to drive success.
            </div>
                ''', unsafe_allow_html=True)
        st.markdown('''
        <head>
                <!-- Add font awesome icon library -->
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        </head>   
                <div class="links">
                    <b> Follow/Reach out to me on:<b>
                    <ul>
                        <li><a href="https://github.com/Taoheed-O/" target="_blank"><i class="fa fa-github"></i>  Github</a></li>
                        <li><a href="https://www.linkedin.com/in/taoheed-oyeniyi/" target="_blank"><i class="fa fa-linkedin"></i>  LinkedIn</a></li>
                    </ul>
                </div>
                ''', unsafe_allow_html=True)
    else:
        pass

    pass




# Lower sidebar


# Image code with encoder ---  not needed here
# # Set the background image using a local image
# # You need to encode the image as base64 first
# import base64
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# # Use the function
# set_png_as_page_bg('images/artificial-intelligence.jpg')