__all__ = ['Config']

import os


class Config:
    API_ID=os.getenv('api_id')
    API_HASH=os.getenv('api_hash')
