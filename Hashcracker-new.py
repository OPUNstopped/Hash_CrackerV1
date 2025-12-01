#script made by OPUNstopped on github

import hashlib
import time

# Symbols
SYMBOL_PATTERNS = ["!?!", "?!?", "!!??", "??!!", "!", "?", "!?","?!", "!!!", "???"]

def password_generator(file_path='rockyou.txt', max_number=10000):
    """
    Generator that yields one password variation at a time.
    """
    with open(file_path, 'r', encoding='latin-1', errors='ignore') as f:
        for base_word in f:
            base_word = base_word.strip()
            if not base_word:
                continue

            base_word_bytes = base_word.encode()

            for n in range(1, max_number + 1):
                num_bytes = str(n).encode()

                yield base_word_bytes + num_bytes

                for sym in SYMBOL_PATTERNS:
                    yield base_word_bytes + num_bytes + sym.encode()


def get_hash_function(hash_type):
    """
    Returns a hashlib function based on user input.
    """
    if hash_type == "md5":
        return hashlib.md5
    if hash_type == "sha1":
        return hashlib.sha1
    if hash_type == "sha256":
        return hashlib.sha256
    if hash_type == "sha512":
        return hashlib.sha512

    raise ValueError("this hash is unsupported.")


def crack_local_hash(target_hash, hash_type, print_attempts=False, delay=0.0):
   #This goes through passwords tring to match the local hash
    attempts = 0
    start = time.time()

    hash_func = get_hash_function(hash_type)

    for pwd_bytes in password_generator():
        attempts += 1

        # optional print of each attempt
        if print_attempts:
            print(pwd_bytes.decode(errors='ignore'))
            if delay > 0:
                time.sleep(delay)

        if hash_func(pwd_bytes).hexdigest() == target_hash:
            elapsed = time.time() - start
            return pwd_bytes.decode(errors='ignore'), attempts, elapsed

    return None, attempts, time.time() - start

if __name__ == "__main__":
    target = input("Target hash: ").strip()
    hash_type = input("Hash type (sha256, md5, sha1, sha512): ").lower().strip()

    show = input("Print every attempt? (y/n): ").lower().strip()
    if show == "y":
        delay = float(input("Delay between prints (seconds): ").strip())
        print_attempts = True
    else:
        print_attempts = False
        delay = 0.0

    found, attempts, seconds = crack_local_hash(
        target, hash_type, print_attempts, delay
    )

    if found:
        print("\nMatch found!")
        print("Password:", found)
        print(f"Attempts: {attempts:,}")
        print(f"Time: {seconds:.2f} seconds\n")
    else:
        print(f"\nNo match found after {attempts:,} attempts.")
        print(f"Time: {seconds:.2f} seconds\n")