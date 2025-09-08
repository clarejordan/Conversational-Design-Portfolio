# Simple CBT Self-Help Coach prototype
# Note: This is a demo only, not medical advice.

def cbt_checkin():
    print("Welcome to a quick CBT check-in.")
    situation = input("What happened? ")
    thought = input("What thought came to mind? ")
    evidence_for = input("What evidence supports that thought? ")
    evidence_against = input("What evidence does not support it? ")
    reframe = f"It seems like you thought '{thought}', but you also noticed: {evidence_against}. A more balanced view could be: you had a challenge, but you also have strengths."
    print("Balanced reframe:", reframe)
    action = input("What is one small action you can take today? ")
    print("Great. You chose:", action, ". Remember this reframe when you need it.")

if __name__ == "__main__":
    cbt_checkin()
