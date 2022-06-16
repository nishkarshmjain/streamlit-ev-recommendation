import pickle
# from flasgger import Swagger
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

pickle_in = open("rfmodel_pkl", "rb")
rf = pickle.load(pickle_in)


def main():
    st.set_page_config(layout="wide")

    st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
    st.sidebar.image('images/logo_l.png', use_column_width=True)
    
    with st.sidebar:
        tabs = on_hover_tabs(tabName=['About Us', 'Product Recomendation', 'Contact Us'],
                             iconName=['dashboard', 'money', 'economy'], default_choice=0)

    if tabs == 'About Us':
        st.title("About Us")
        cola1, cola2, cola3 = st.columns([0.2, 5, 0.2])
        cola2.image('images/thunder.JPG', width=1000, use_column_width=True)
        #st.image('images/thunder.JPG', width=1000)
        st.subheader('ThunderX is an electric vehicle manufacturing company that manufactures premium and economical bikes for consumers and businesses.')
        st.title("Our Technologies")
        cola11, cola21, cola31 = st.columns([0.2, 5, 0.2])
        cola21.image('images/arch.JPG', width=1000, use_column_width=True)


    elif tabs == 'Product Recomendation':
        # -----------------------------Recommendation Page--------------------------------

        st.image('images/logo1.png', width=150)
        colf1, colf2, colf21 = st.columns(3)
        with colf1:
            name = st.text_input("Name")
        with colf2:
            email = st.text_input("E-mail")
        with colf21:
            email = st.text_input("Contact Number")
        colf3, colf4, colf5 = st.columns(3)
        with colf3:
            gender = st.selectbox("Select Gender: ", ('Male', 'Female'))
        with colf4:
            city = st.selectbox("Select City",
                                ["Bangalore", "Chennai", "Hyderabad", "Mumbai", "Pune"])
        with colf5:
            age = st.number_input("Age", step=1)
        prod = {'RS955': 'Torque Plus', 'AU116': 'Alpha Apache TR160', 'ML1125': 'Lithnoid S20', 'AP134': 'Sigma Pro',
                'RR99': 'Neon 0A2', 'YT978': 'Torque Plus', 'SH1154': 'Sugoi A1'}
        if st.button("Predict"):
            a, b, c = product(gender, age, city)
            d = a[0]
            st.success('Hi ' + name + ','+ "\n" + 'The recommended product for you is {}.'.format(prod[d]))
            st.image('images/1.jpg', caption=prod[d])
            st.success(' Our nearest dealership will reach out to you for a test drive.')
            st.subheader('Customers like you from ' + city + ' bought')
            col1, col2, col3 = st.columns(3)

            with col1:
                st.header(prod[b[0]])
                st.image("images/2.jpg")

            with col2:
                st.header(prod[b[1]])
                st.image("images/3.jpg")

            with col3:
                st.header(prod[b[2]])
                st.image("images/4.jpg")


    elif tabs == 'Contact Us':
        st.title("Our Team")

        colc1, colc2, colc3 = st.columns([0.2, 5, 0.2])
        colc2.image('images/team.JPG', width=1000, use_column_width=True)
        #st.image('images/team.jpg', width=800)
        #st.image('images/dbt.png', width=800)
        #st.text('Customers like you from ' + city + ' bought')
        #st.text(prod[b[0]])
        #st.image('images/2.jpg', caption=prod[b[0]])
        #st.text(prod[b[1]])
        #st.image('images/3.jpg', caption=prod[b[1]])
        #st.text(prod[b[2]])
        #st.image('images/4.jpg', caption=prod[b[2]])
    #if st.button("About"):
        #st.text("Lets LEarn")
        #st.text("Built with Streamlit")



def product(gender, age, city):
    recommended_prod = rf.predict([convert_input(gender, age, city)])

    if age in range(20, 30):
        r, q = prod2030()
    elif age in range(30, 40):
        r, q = prod3040()
    elif age in range(40, 50):
        r, q = prod4050()
    else:
        r, q = prod2030()

    return recommended_prod, r, q


def convert_input(gender, age, city):
    le_city_mapping = {'Ahemdabad': 0, 'Bangalore': 1, 'Chennai': 2, 'Mumbai': 3, 'Pune': 4}
    le_gender_mapping = {'Female': 0, 'Male': 1,'F': 0, 'M': 1}
    le_city = le_city_mapping[city]
    le_gender = le_gender_mapping[gender]

    return le_city, age, le_gender


def prod2030():
    ranking = ['RR99', 'ML1125', 'RS955']
    qty = {'total': 1217, 'M': 620, 'F': 597}
    return ranking, qty


def prod3040():
    ranking = ['YT978', 'SH1154', 'RR99']
    qty = {'total': 848, 'M': 456, 'F': 392}
    return ranking, qty


def prod4050():
    ranking = ['ML1125', 'YT978', 'RR99']
    qty = {'total': 1763, 'M': 1022, 'F': 741}
    return ranking, qty

if __name__ == '__main__':
    main()

