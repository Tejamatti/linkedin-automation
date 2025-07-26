def handle_reply(profile_id, reply):
    if "interested" in reply.lower():
        print(f"[+] Positive reply from {profile_id}")
    else:
        print(f"[-] No strong intent from {profile_id}")
