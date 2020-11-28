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


def create_account(user_name: str, password: str, secret_words: list):
    def check(pwd_to_check: str, secrets_to_check: list):
        matched_secrets = [i for i in secrets_to_check if i in secret_words]
        if password != pwd_to_check or len(secret_words) != len(secrets_to_check):
            return False
        elif len(matched_secrets) >= len(secret_words)-1:
            return True
        else:
            return False
    validate_pwd(password)
    return check
