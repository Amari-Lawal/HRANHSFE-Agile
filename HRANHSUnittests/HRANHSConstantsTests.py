import os
from dotenv import load_dotenv
load_dotenv("./env")
class HRANHSConstantsTests:
    EMAIL = "alice.johnson@example.com"
    PASSWORD = "hello" 
    PUBLIC_URI="https://hranhsmedicineassets-qqbn26mgpa-uc.a.run.app"
    LOCAL_URI="http://127.0.0.1:8080"
    URI=os.getenv("URI") or PUBLIC_URI
    MEDICINE_ASSET="Aspirin"
    VENDOR_NAME="GSK Pharmaceuticals"
