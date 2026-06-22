from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_points_lower():
    # Reverse-hints bug: a guess above the secret must tell the player to go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_points_higher():
    # Reverse-hints bug: a guess below the secret must tell the player to go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message
