import re


_EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)


def is_valid_email(email):
    if not isinstance(email, str):
        return False
    return _EMAIL_PATTERN.fullmatch(email) is not None


is_valid = is_valid_email


def get_domain(address):
    if not is_valid_email(address):
        raise ValueError("Invalid email address")
    return address.rsplit("@", 1)[1]


def local_part(address):
    if not is_valid_email(address):
        raise ValueError("Invalid email address")
    return address.rsplit("@", 1)[0]


def masked_email(address, show=2):
    if not isinstance(show, int) or isinstance(show, bool) or show < 0:
        raise ValueError("show must be a non-negative integer")
    if not is_valid_email(address):
        raise ValueError("Invalid email address")

    local = local_part(address)
    domain = get_domain(address)
    visible = local[:show]
    masked = visible + "*" * max(len(local) - show, 0)
    return masked + "@" + domain