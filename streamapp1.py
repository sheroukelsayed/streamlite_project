import streamlit as st
import pickle



# Load the model
with open('sentiment_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the app
st.sidebar.title("Navigation")
selection = st.sidebar.radio(
    "Select a Category",
    ["Home", "Action Movies", "Family Movies", "Cartoon Movies", "Romantic Movies", "Arabic Movies"]
)

if selection == "Home":
    
    st.title('Home Page')
    st.image("welcome_img.jpg", caption="Welcome to the Sentiment Analysis app!", width=600)

elif selection == "Action Movies":
    st.title('Sentiment Analysis for Action Movies')
  
    st.image("action.jpeg", width=600)
    st.write("This app predicts the sentiment of a given text (positive or negative).")
    user_input1 = st.text_area("Enter the name of the movie", key="action_movie_name")
    user_input = st.text_area("Enter your review:", key="action_movie_review")
    if st.button("Predict", key="action_movie_predict"):
        
            # Predict the sentiment and the prediction score
            prediction = model.predict([user_input])
            prediction_proba = model.predict_proba([user_input])
            sentiment = "Positive" if prediction[0] == 'pos' else "Negative"
            prediction_score = prediction_proba[0][1] if prediction[0] == 'pos' else prediction_proba[0][0]

            # Display the results
            st.write(f"The predicted sentiment is: **{sentiment}**")
            st.write(f"Prediction score: **{prediction_score:.4f}**")
       

elif selection == "Family Movies":
    st.title('Sentiment Analysis for Family Movies')
    st.image("family.jpg", width=600)
   
    st.write("This app predicts the sentiment of a given text (positive or negative).")
    user_input1 = st.text_area("Enter the name of the movie", key="family_movie_name")
    user_input = st.text_area("Enter your review:", key="family_movie_review")
    if st.button("Predict", key="family_movie_predict"):
            # Predict the sentiment and the prediction score
            prediction = model.predict([user_input])
            prediction_proba = model.predict_proba([user_input])
            sentiment = "Positive" if prediction[0] == 'pos' else "Negative"
            prediction_score = prediction_proba[0][1] if prediction[0] == 'pos' else prediction_proba[0][0]

            # Display the results
            st.write(f"The predicted sentiment is: **{sentiment}**")
            st.write(f"Prediction score: **{prediction_score:.4f}**")

elif selection == "Cartoon Movies":
    st.title('Sentiment Analysis for Cartoon Movies')
    st.image("cartoon.jpg", width=600)

    st.write("This app predicts the sentiment of a given text (positive or negative).")
    user_input1 = st.text_area("Enter the name of the movie", key="cartoon_movie_name")
    user_input = st.text_area("Enter your review:", key="cartoon_movie_review")
    if st.button("Predict", key="cartoon_movie_predict"):
            # Predict the sentiment and the prediction score
            prediction = model.predict([user_input])
            prediction_proba = model.predict_proba([user_input])
            sentiment = "Positive" if prediction[0] == 'pos' else "Negative"
            prediction_score = prediction_proba[0][1] if prediction[0] == 'pos' else prediction_proba[0][0]

            # Display the results
            st.write(f"The predicted sentiment is: **{sentiment}**")
            st.write(f"Prediction score: **{prediction_score:.4f}**")

elif selection == "Romantic Movies":
    st.title('Sentiment Analysis for Romantic Movies')
    st.image("romantic.jpeg", width=600)

    st.write("This app predicts the sentiment of a given text (positive or negative).")
    user_input1 = st.text_area("Enter the name of the movie", key="romantic_movie_name")
    user_input = st.text_area("Enter your review:", key="romantic_movie_review")
    if st.button("Predict", key="romantic_movie_predict"):
            # Predict the sentiment and the prediction score
            prediction = model.predict([user_input])
            prediction_proba = model.predict_proba([user_input])
            sentiment = "Positive" if prediction[0] == 'pos' else "Negative"
            prediction_score = prediction_proba[0][1] if prediction[0] == 'pos' else prediction_proba[0][0]

            # Display the results
            st.write(f"The predicted sentiment is: **{sentiment}**")
            st.write(f"Prediction score: **{prediction_score:.4f}**")

elif selection == "Arabic Movies":
    st.title('Sentiment Analysis for Arabic Movies')
    st.image("arabic.jpg", width=600)
    st.write("This app predicts the sentiment of a given text (positive or negative).")
    user_input1 = st.text_area("Enter the name of the movie", key="arabic_movie_name")
    user_input = st.text_area("Enter your review:", key="arabic_movie_review")
    if st.button("Predict", key="arabic_movie_predict"):
            # Predict the sentiment and the prediction score
            prediction = model.predict([user_input])
            prediction_proba = model.predict_proba([user_input])
            sentiment = "Positive" if prediction[0] == 'pos' else "Negative"
            prediction_score = prediction_proba[0][1] if prediction[0] == 'pos' else prediction_proba[0][0]

            # Display the results
            st.write(f"The predicted sentiment is: **{sentiment}**")
            st.write(f"Prediction score: **{prediction_score:.4f}**")