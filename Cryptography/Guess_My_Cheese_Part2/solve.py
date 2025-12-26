import hashlib
import sys

# 🔐 Your target hash
target_hash = "2d3612ea1ece0dac0ae7c2a8c3038bdf45787413da2aaccab25d95babac0d2ea"

# Encodings and case variants to try
encodings = ["utf-8", "utf-16-le", "utf-16-be", "latin-1"]
case_variants = {
    "original": lambda s: s,
    "lower": lambda s: s.lower(),
    "upper": lambda s: s.upper(),
}

# Load cheese list
try:
    with open("cheese_list.txt", "r") as f:
        cheeses = [line.strip() for line in f if line.strip()]
    print(f"[+] Loaded cheese_list.txt ({len(cheeses)} entries)")
except FileNotFoundError:
    print("[-] cheese_list.txt not found")
    sys.exit(1)

found = False

def test_candidate(candidate_bytes, method, extra, cheese, case_name, enc, salt):
    global found
    digest = hashlib.sha256(candidate_bytes).hexdigest()
    if digest == target_hash:
        print("\n[+] MATCH FOUND!")
        print(f"Cheese       : {cheese}")
        print(f"Case variant : {case_name}")
        print(f"Encoding     : {enc}")
        print(f"Salt         : {salt} (0x{salt:02x})")
        print(f"Method       : {method} ({extra})")
        found = True
        return True
    return False

# Brute-force everything
for cheese in cheeses:
    for case_name, case_func in case_variants.items():
        cheese_variant = case_func(cheese)

        for enc in encodings:
            try:
                cheese_bytes = cheese_variant.encode(enc)
            except Exception:
                continue

            for salt in range(256):
                salt_raw = bytes([salt])
                salt_hex = f"{salt:02x}".encode("utf-8")

                # A) Raw byte prepend / append
                if test_candidate(cheese_bytes + salt_raw, "append_raw", "raw byte", cheese, case_name, enc, salt):
                    break
                if test_candidate(salt_raw + cheese_bytes, "prepend_raw", "raw byte", cheese, case_name, enc, salt):
                    break

                # B) Hex string prepend / append
                if test_candidate(cheese_bytes + salt_hex, "append_hex", "hex string", cheese, case_name, enc, salt):
                    break
                if test_candidate(salt_hex + cheese_bytes, "prepend_hex", "hex string", cheese, case_name, enc, salt):
                    break

                # C) Insert raw byte anywhere
                for i in range(len(cheese_bytes) + 1):
                    candidate = cheese_bytes[:i] + salt_raw + cheese_bytes[i:]
                    if test_candidate(candidate, "insert_raw", f"index {i}", cheese, case_name, enc, salt):
                        break
                if found:
                    break

                # D) Insert hex string anywhere
                for i in range(len(cheese_bytes) + 1):
                    candidate = cheese_bytes[:i] + salt_hex + cheese_bytes[i:]
                    if test_candidate(candidate, "insert_hex", f"index {i}", cheese, case_name, enc, salt):
                        break
                if found:
                    break

            if found:
                break
        if found:
            break
    if found:
        break

if not found:
    print("\n[-] No matching cheese and salt combination found.")
