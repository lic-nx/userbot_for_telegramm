__all__ = ['Config']

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')


print(API_ID)
print(API_HASH)
