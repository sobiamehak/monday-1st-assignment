# --- Libraries Import ---
import streamlit as st
import random

# --- OOP Concept #1: Class creation (Blueprint) ---
# WordScramble aik class hai (blueprint) jo ek scrambled word game ka core logic rakhta hai.
class WordScramble:
    # --- Constructor / Initializer method ---
    def __init__(self):
        # --- OOP Concept #2: Attribute ---
        # self.words aik attribute hai — class ke andar variable jo object ka hissa hota hai
        self.words = ["python", "streamlit", "computer", "decorators", "program", "polymorphism", 
                      "variable", "loop", "syntax", "keyboard", "attribute", "method", 
                      "encapsulation", "enheritence", "abstraction"]

        # Original word randomly choose kiya jata hai — encapsulation ka example
        self.original = random.choice(self.words)

        # Shuffle kiya gaya word set kiya jata hai — abstraction ka part (details chhupai ja rahi hain)
        self.scrambled = self.shuffle_word(self.original)

    # --- OOP Concept #3: Method (Function inside a class) ---
    # Shuffle karne wali functionality ko method banakar alag rakh diya gaya hai (abstraction)
    def shuffle_word(self, word):
        scrambled = list(word)
        random.shuffle(scrambled)
        return ''.join(scrambled)

    # --- Method to check user input vs correct word ---
    def check_answer(self, user_input):
        return user_input.lower().strip() == self.original


# --- Second Class: ScrambleGame handles game state and interaction ---
class ScrambleGame:
    def __init__(self):
        # Encapsulation: Data ko safely manage karna using session_state
        if 'score' not in st.session_state:
            st.session_state.score = 0  # Initial score set karte hain

        if 'scramble' not in st.session_state:
            # OOP Concept #4: Object Creation
            # WordScramble ka object create kar ke uska reference session mein store karte hain
            st.session_state.scramble = WordScramble()

        if 'submitted' not in st.session_state:
            st.session_state.submitted = False

    # --- Method to generate new word ---
    def new_question(self):
        st.session_state.scramble = WordScramble()  # New WordScramble object
        st.session_state.submitted = False

    # --- Method to check answer ---
    def check(self, user_input):
        if st.session_state.scramble.check_answer(user_input):
            st.success("🎉 Correct! Great job!")  # Feedback for correct answer
            st.session_state.score += 1          # Score increase
        else:
            correct = st.session_state.scramble.original
            st.error(f"❌ Wrong! The correct word was: **{correct}**")
        st.session_state.submitted = True

    # --- Method to give up and show answer ---
    def give_up(self):
        correct = st.session_state.scramble.original
        st.info(f"ℹ️ The correct word was: **{correct}**")
        st.session_state.submitted = True


# --- Streamlit App Interface (Functional programming part) ---
def main():
    st.title("🧠 Word Scramble Game (Sharpen Your Mind!)")

    # ScrambleGame class ka object banaya gaya (OOP concept: object instantiation)
    game = ScrambleGame()

    st.markdown(f"### 🔤 Scrambled Word: `{st.session_state.scramble.scrambled}`")

    if not st.session_state.submitted:
        user_input = st.text_input("💡 Unscramble this word:")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Submit"):
                if user_input.strip() != "":
                    game.check(user_input)  # game object ke method ko call kar rahe hain
                else:
                    st.warning("⚠️ Please enter something!")
        with col2:
            if st.button("❓ I Give Up"):
                game.give_up()
    else:
        if st.button("➡️ Next Word"):
            game.new_question()
            st.rerun()

    st.markdown(f"**⭐ Score: {st.session_state.score}**")

    if st.button("🔁 Reset Game"):
        for key in ['score', 'scramble', 'submitted']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()


# Entry point: Jab file run hoti hai to yahan se start hota hai
if __name__ == "__main__":
    main()
