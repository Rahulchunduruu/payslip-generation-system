import os
from dotenv import load_dotenv
load_dotenv()

class Config:    
    DB_DRIVER=os.getenv('DB_DRIVER')
    DB_SERVER=os.getenv('DB_SERVER')
    DB_DATABASE=os.getenv('DB_DATABASE')
    DB_Trusted_Connection=os.getenv('DB_Trusted_Connection')