from dotenv import load_dotenv
import os
from supabase import create_client, Client


def supabase_loader():
    load_dotenv()

    url: str = os.environ['SUPABASE_URL']
    key: str = os.environ['SUPABASE_API_KEY']
    supabase: Client = create_client(url, key)
    
    return supabase