from storages.backends.azure_storage import AzureStorage
from pathlib import Path
import os
import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    
account_key = os.environ['account_key']


class AzureMediaStorage(AzureStorage):
    account_name = 'portfolioguillaume'
    account_key = account_key
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'portfolioguillaume'
    account_key = account_key
    azure_container = 'static'
    expiration_secs = None