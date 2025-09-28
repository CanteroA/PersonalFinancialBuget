import os
from supabase import create_client, Client

def supabase_connector():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url,key)
    return supabase