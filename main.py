import pickle
# from flasgger import Swagger
import streamlit as st

pickle_in = open("rfmodel_pkl", "rb")
rf = pickle.load(pickle_in)

def main():


    st.title("ThunderX Product Recommender")
    html_temp = """

    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Machine Learning App </h2>
    </div>
    """
    st.markdown("""<style>body{background-color: White;}</style>""",unsafe_allow_html=True)
    st.markdown(html_temp, unsafe_allow_html=True)
    name = st.text_input("Name", "Type Here")
    email = st.text_input("E-mail", "Type Here")
    gender = st.radio("Select Gender: ", ('Male', 'Female'))
    city = st.text_input("City", "Type Here")
    age = st.number_input("Age", step=1)
    prod = {'RS955': 'Torque Plus', 'AU116': 'Alpha Apache TR160', 'ML1125': 'Lithnoid S20', 'AP134': 'Sigma Pro',
            'RR99': 'Neon 0A2', 'YT978': 'Torque Plus Pro', 'SH1154': 'Sugoi A1'}
    if st.button("Predict"):
        a, b, c = product(gender, age, city)
        d = a[0]
        st.success('Hi, ' + name + '\n The recommended product for you is {}'.format(prod[d]))
        st.text('Customers like you from ' + city + ' bought')
        st.text(prod[b[0]])
        st.text(prod[b[1]])
        st.text(prod[b[2]])

    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


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
    le_city_mapping = {'Ahemdabad': 0, 'Banglore': 1, 'Chennai': 2, 'Mumbai': 3, 'Pune': 4}
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

