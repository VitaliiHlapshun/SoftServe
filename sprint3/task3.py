def create_account(user_name: str, password: str, secret_words: list):
    def check(password_2: str, secret_words_2: list):
        # spec_char = ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/','\\', '|', '}', '{', '~', ':']
        if len(secret_words) != len(secret_words_2):
            return False
        elif password == password_2 and len(set(secret_words) & set(secret_words_2)) >= len(secret_words)-1:
            return True
        else:
            return False
    return check
