import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load('xgboost_model.pkl')
st.markdown(
    """
<style>
button {
    height: auto;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

def preprocess_input(age, workclass, education_level, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country):
    # Create a DataFrame with the user inputs
    input_data = pd.DataFrame({
        'age': [age],
        'workclass': [workclass],
        'education_level': [education_level],
        'education-num': [education_num],
        'marital-status': [marital_status],
        'occupation': [occupation],
        'relationship': [relationship],
        'race': [race],
        'sex': [sex],
        'capital-gain': [capital_gain],
        'capital-loss': [capital_loss],
        'hours-per-week': [hours_per_week],
        'native-country': [native_country]
    })

    # Perform label encoding on the categorical columns
    label_encoder = LabelEncoder()
    categorical_columns = ['workclass', 'education_level', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
    for column in categorical_columns:
        input_data[column] = label_encoder.fit_transform(input_data[column])

    return input_data


def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "About"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Home":
        st.markdown('<h1 style="text-align: center;">Finding Donor</h1>', unsafe_allow_html=True)
        st.markdown('Please provide the required information to predict the income level.')

        # Add user input fields
        default_age = 39  # Average value of 'age' field
        default_education_num = 9  # Average value of 'education-num' field
        default_capital_gain = 7.68  # Average value of 'capital-gain' field
        default_capital_loss = 0.0  # Average value of 'capital-loss' field
        default_hours_per_week = 40  # Average value of 'hours-per-week' field

        col1, col2 = st.columns(2)

        with col1:
            age = st.slider('Age', min_value=0, max_value=100, value=default_age, step=1)
            workclass = st.selectbox('Workclass', ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', 'Self-emp-inc', 'Without-pay'])
            education_level = st.selectbox('Education Level', ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college',
                                                              'Assoc-acdm', '7th-8th', 'Doctorate', 'Assoc-voc', 'Prof-school',
                                                              '5th-6th', '10th', 'Preschool', '12th', '1st-4th'])
            education_num = st.slider('Education Number', min_value=1, max_value=20, value=default_education_num, step=1)
            marital_status = st.selectbox('Marital Status', ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-spouse-absent',
                                                             'Separated', 'Married-AF-spouse', 'Widowed'])
            occupation = st.selectbox('Occupation', ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty',
                                                     'Other-service', 'Sales', 'Transport-moving', 'Farming-fishing',
                                                     'Machine-op-inspct', 'Tech-support', 'Craft-repair', 'Protective-serv',
                                                     'Armed-Forces', 'Priv-house-serv'])
            relationship = st.selectbox('Relationship', ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried',
                                                         'Other-relative'])
        with col2:
            race = st.selectbox('Race', ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
            sex = st.selectbox('Sex', ['Male', 'Female'])
            capital_gain = st.number_input('Capital Gain', min_value=0.0, max_value=20.0, value=default_capital_gain, step=0.01)
            capital_loss = st.number_input('Capital Loss', min_value=0.0, max_value=20.0, value=default_capital_loss, step=0.01)
            hours_per_week = st.slider('Hours per Week', min_value=0, max_value=100, value=default_hours_per_week, step=1)
            native_country = st.selectbox('Native Country', ['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'Puerto-Rico',
                                                             'Honduras', 'England', 'Canada', 'Germany', 'Iran', 'Philippines',
                                                             'Poland', 'Columbia', 'Cambodia', 'Thailand', 'Ecuador', 'Laos',
                                                             'Taiwan', 'Haiti', 'Portugal', 'Dominican-Republic', 'El-Salvador',
                                                             'France', 'Guatemala', 'Italy', 'China', 'South', 'Japan', 'Yugoslavia',
                                                             'Peru', 'Outlying-US(Guam-USVI-etc)', 'Scotland', 'Trinadad&Tobago',
                                                             'Greece', 'Nicaragua', 'Vietnam', 'Hong', 'Ireland', 'Hungary',
                                                             'Holand-Netherlands'])

        # Perform prediction when the 'Predict' button is clicked
        
        if st.button('Predict', help='Click to predict the income level', key='predict_button'):
                # Preprocess the input data
            input_data = preprocess_input(age, workclass, education_level, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country)

                # Make predictions using the loaded model
            prediction = model.predict(input_data)

            st.subheader('Prediction Result:')
            result = 'Income Level: Greater than 50K' if prediction and prediction[0] == 1 else 'Income Level: Less than or equal to 50K'
            st.success(result)

    elif choice == "About":
        st.markdown('<h1 style="text-align: center;">About</h1>', unsafe_allow_html=True)
        st.write('This web app predicts the likelihood of finding a donor based on income level.')
        st.write('The model is trained on a dataset of income data using XGBoost algorithm.')
        st.write('The purpose of this app is to demonstrate the usage of machine learning in identifying potential donors.')
        st.write('Made with Streamlit.')

if __name__ == '__main__':
    main()
