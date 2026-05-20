import streamlit as st
import random

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("🎯 Number Guessing Game")

guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    st.session_state.attempts += 1
    if guess > st.session_state.number:
        st.warning("Too high!")
    elif guess < st.session_state.number:
        st.warning("Too low!")
    else:
        st.success(f"🎉 Correct! You guessed in {st.session_state.attempts} attempts.")
