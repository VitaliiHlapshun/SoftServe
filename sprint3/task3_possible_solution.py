def validate_pwd(pwd: str):
    spec_chars = [
        '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\\', '|', '}', '{', '~', ':']
    upper_letter_exists = [i for i in pwd if i.isupper()]
    lower_letter_exists = [i for i in pwd if i.islower()]
    is_len_valid = len(pwd) >= 6
    digit_exists = [i for i in pwd if i.isdigit()]
    spec_char_exists = [i for i in pwd if i in spec_chars]
    if not (upper_letter_exists and lower_letter_exists and is_len_valid and digit_exists and spec_char_exists):
        raise ValueError('Password does not match its requirements. Check them out, please.')


def are_secrets_valid(base_secrets, secrets_to_check):
    if len(base_secrets) != len(secrets_to_check):
        return False
    for word in secrets_to_check:
        for letter in word:
            for secret in base_secrets:
                matched_len = 0
                for s_letter in secret:
                    if s_letter == letter:
                        matched_len += 1
                if matched_len < len(secret) - 1:
                    return False
    return True


def create_account(user_name: str, password: str, secret_words: list):
    def check(pwd_to_check: str, secrets_to_check: list):
        if password != pwd_to_check or not are_secrets_valid(secret_words, secrets_to_check):
            return False
        return True
    validate_pwd(password)
    return check
