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
        is_valid = False
        for secret in base_secrets:
            if len(word) == len(secret):
                matched_len = 0
                for letter in word:
                    if letter in secret:
                        matched_len += 1
                # matched_data.append(matched_len)
                if matched_len >= len(secret) - 1:
                    is_valid = True
                    break
        if not is_valid:
            return False
    return True


def create_account(user_name: str, password: str, secret_words: list):
    def check(pwd_to_check: str, secrets_to_check: list):
        if password != pwd_to_check or not are_secrets_valid(secret_words, secrets_to_check):
            return False
        return True
    validate_pwd(password)
    return check


val1 = create_account('test', 'Qa!1asddsf', ['123', '133', '33312'])
print(val1('Qa!1asddsf', ['123', '933', '33012']))
