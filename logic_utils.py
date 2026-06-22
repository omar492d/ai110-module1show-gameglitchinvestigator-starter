def get_range_for_difficulty(difficulty: str):
    """Return the inclusive guessing range for a difficulty level.

    Args:
        difficulty: Difficulty name. One of "Easy", "Normal", or "Hard".

    Returns:
        tuple[int, int]: A ``(low, high)`` pair giving the inclusive bounds.
        Unknown difficulties fall back to the "Normal" range ``(1, 100)``.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse raw user input into an integer guess.

    Accepts plain integers as well as decimal strings, which are truncated
    toward zero (e.g. ``"3.9"`` becomes ``3``).

    Args:
        raw: The raw input string, or ``None``.

    Returns:
        tuple[bool, int | None, str | None]: A ``(ok, guess, error)`` triple.
        On success, ``ok`` is ``True``, ``guess`` holds the parsed integer, and
        ``error`` is ``None``. On failure, ``ok`` is ``False``, ``guess`` is
        ``None``, and ``error`` is a human-readable message.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare a guess against the secret number.

    Args:
        guess: The player's guess.
        secret: The target number to match.

    Returns:
        tuple[str, str]: An ``(outcome, message)`` pair. ``outcome`` is one of
        ``"Win"``, ``"Too High"``, or ``"Too Low"``, and ``message`` is the
        display string shown to the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Used Claude to fix the misleading hints bug
    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the running score based on the latest guess outcome.

    A win awards points that decrease with each attempt, floored at 10.
    A "Too Low" outcome always costs 5 points; a "Too High" outcome awards
    5 points on even attempts and costs 5 on odd attempts.

    Args:
        current_score: The score before this guess.
        outcome: The guess outcome, as returned by :func:`check_guess`.
        attempt_number: Zero-based index of the current attempt.

    Returns:
        int: The updated score.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
