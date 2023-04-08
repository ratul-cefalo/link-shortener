import random
import string
from .create_db import Link
def generate_short_code():
    letters = string.ascii_uppercase
    short_code = ''.join(random.choice(letters) for i in range(6))
    # Check if the short code already exists in the database and generate a new one if necessary
    while db.query(Link).filter(Link.short_code == short_code).first() is not None:
        short_code = ''.join(random.choice(letters) for i in range(6))
    return short_code
