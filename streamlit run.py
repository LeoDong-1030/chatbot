import streamlit as st

import random

# REPLACE THE WORDS HERE WITH ONES THAT YOU THOUGHT OF (they are probably better)
def initialization():
    if "word" not in st.session_state:
        st.session_state.word_list = ['roblox', 'fries', 'legos', 'School', 'drinks', 'computer']
        st.session_state.word = random.choice(st.session_state.word_list)
        st.session_state.attempts_remaining = 6
        st.session_state.correct_attempts = ['_' for _ in st.session_state.word]
        st.session_state.wrong_attempts = []  # Keep track of wrong guesses

def display():
    st.write("--------------------------------------")
    st.write("Current word state:")
    st.write(' '.join(st.session_state.correct_attempts))
    st.write("Incorrect guesses:")
    st.write(' '.join(st.session_state.wrong_attempts))
    st.write("Attempts remaining:",st.session_state.attempts_remaining)

def guess_letter(guess, attempts_remaining):
    if guess in st.session_state.word:
        for i in range(len(st.session_state.word)):
            letter = st.session_state.word[i]
            if letter == guess:
                st.session_state.correct_attempts[i] = guess
    else:
        st.session_state.wrong_attempts.append(guess)
        attempts_remaining -= 1
    return attempts_remaining


initialization()
with st.form(key="my_form"):
    guess = st.text_input("Guess a letter").lower()
    sumbit_button = st.form_submit_button("Sumbit the letter")
    if sumbit_button:
        if guess in st.session_state.wrong_attempts or guess in st.session_state.correct_attempts:
            st.write("letter already guessed")
        else:
            # Show if they got the letter correct or incorrect and update visually
            # if correct, fill in the letter blanks with guessed letter
            # if wrong, say they got it wrong and draw the dude
            st.session_state.attempts_remaining = guess_letter(guess, st.session_state.attempts_remaining)
        
        display()


# while attempts_remaining > 0 and '_' in correct_attempts:
    # GAME LOOP TASK
    # display()
    # guess = st.text_input("Guess a Letter").lower()
    # if guess in wrong_attempts or guess in correct_attempts:
    #     st.write("letter already guessed")
    # else:
    #     attempts_remaining = guess_letter(guess, attempts_remaining)
        
if '_' not in st.session_state.correct_attempts:
    st.success("Congratulations! You've guessed the word: " + st.session_state.word)
elif st.session_state.attempts_remaining == 0:

    st.error("Out of attempts! The word was: " + st.session_state.word)
