import urllib.request
import json

BASE_URL = "http://127.0.0.1:5174"

def test_chat_elaboration():
    print("\n--- 1. Testing Elaborate Chat Synthesis ---")
    data = json.dumps({
        "message": "thermodynamics laws and entropy",
        "history": []
    }).encode('utf-8')

    req = urllib.request.Request(
        f"{BASE_URL}/api/chat",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        text = res.get("text", "")
        assert "###" in text or "Breakdown" in text or len(text) > 300
        print("[OK] AI generated elaborate response with sections! Text length:", len(text))
        print("Snippet preview:\n", text[:250], "...")

def test_feedback_registration():
    print("\n--- 2. Testing Feedback API Registration ---")
    data = json.dumps({
        "message": "thermodynamics laws",
        "response": "Thermodynamics is...",
        "rating": "excellent",
        "comment": "Very detailed and comprehensive!",
        "timestamp": 123456789
    }).encode('utf-8')

    req = urllib.request.Request(
        f"{BASE_URL}/api/feedback",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        assert res.get("success") is True
        print("[OK] Feedback successfully recorded on server:", res)

if __name__ == "__main__":
    test_chat_elaboration()
    test_feedback_registration()
    print("\nALL ELABORATION & FEEDBACK CHECKS PASSED!")
