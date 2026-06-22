import os

from streamlit.testing.v1 import AppTest

APP_PATH = os.path.join(os.path.dirname(__file__), "..", "app.py")


def test_new_game_revives_after_round_over():
    """Regression: clicking "New Game" after a round must make the game playable again.

    The original bug left st.session_state.status as "won"/"lost", so the
    game-over guard kept calling st.stop() and the button looked unresponsive.
    """
    at = AppTest.from_file(APP_PATH)
    at.run()

    # Simulate a finished round (player won the previous game)
    at.session_state.status = "won"
    at.run()
    assert at.session_state.status == "won"  # game-over guard is active

    # Click "New Game 🔁" (second button on the page)
    at.button[1].click().run()

    # A new game must reset status back to "playing" so the round can continue
    assert at.session_state.status == "playing"
    assert at.session_state.attempts == 0
