from HRANHSUnittests.HRANHSConstantsTests import HRANHSConstantsTests
class HRANHSTestCases:
    USER_SIGNUP_ADMIN_TEST_CASE = {
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": HRANHSConstantsTests.EMAIL,
            "password": HRANHSConstantsTests.PASSWORD,
            "role": "admin",
            "department": "Engineering",
            "phone_number": "+1234567890",
            "status": "active",
            "last_login": "2025-04-23T12:34:56",
            "created_at": "2024-12-01T09:15:30",
            "updated_at": "2025-04-22T17:45:10"
            }
    POST_ASSET_TEST_CASE = {
                "medicine_asset": HRANHSConstantsTests.MEDICINE_ASSET,
                "description": "Pain reliever and anti-inflammatory",
                "vendor_id": "{vendor_id}",
                "category": "Pain Relief",
                "lot_number": "AB12345",
                "manufacture_date": "2023-05-10",
                "purchase_cost": 12.99,
                "vendor": "Pharma Inc.",
                "storage_location": "Shelf A1",
                "status": "Active",
                "expiration_date": "2025-05-10",
                "last_reviewed": "2024-04-15",
                "next_review": "2025-04-15",
                "storage_conditions": "Cool and dry place",
                "useful_life_years": 2,
                "current_stock": 100,
                "image_url": "https://example.com/images/aspirin.jpg"
                }
    UPDATE_VENDOR_TEST_CASES=[
  {
    "vendor_name": "Tech Supplies Ltd.",
    "vendor_address": "123 Tech Street, Silicon Valley, CA",
    "contact_person": "John Doe",
    "contact_number": "+1-800-555-1234",
    "email": "johndoe@techsupplies.com",
    "status": "Active"
  },
  {
    "vendor_name": "Global Electronics",
    "vendor_address": "456 Global Plaza, New York, NY",
    "contact_person": "Jane Smith",
    "contact_number": "+1-212-555-9876",
    "email": "janesmith@globelec.com",
    "status": "Inactive"
  },
  {
    "vendor_name": "Green Energy Corp.",
    "vendor_address": "789 Green Way, Houston, TX",
    "contact_person": "Mark Johnson",
    "contact_number": "+1-832-555-4567",
    "email": "markjohnson@greenenergy.com",
    "status": "Pending"
  },
  {
    "vendor_name": "Fashion Distributors",
    "vendor_address": "101 Fashion Avenue, Los Angeles, CA",
    "contact_person": "Linda Williams",
    "contact_number": "+1-310-555-2345",
    "email": "lindawilliams@fashiondistrib.com",
    "status": "Active"
  },
  {
    "vendor_name": "Alpha Technologies",
    "vendor_address": "200 Alpha Building, Boston, MA",
    "contact_person": "David Lee",
    "contact_number": "+1-617-555-6789",
    "email": "davidlee@alphatech.com",
    "status": "Suspended"
  }
]

    UPDATE_ASSET_TEST_CASES = [
  {
    "description": "Hello World",
    "category": "Analgesic",
    "lot_number": "LTPM500-2024A",
    "manufacture_date": "2024-01-15",
    "purchase_cost": 0.10,
    "storage_location": "Shelf A1",
    "status": "active",
    "expiration_date": "2026-01-15",
    "last_reviewed": "2025-04-01",
    "next_review": "2025-10-01",
    "storage_conditions": "Store at room temperature",
    "useful_life_years": 2,
    "current_stock": 5000,
    "image_url": "https://example.com/images/paracetamol.png"
  },
  {
    "medicine_asset": "Amoxicillin 250mg",
    "description": "Broad-spectrum antibiotic",
  },
  {
    "lot_number": "IBU200-C34",
    "manufacture_date": "2024-03-05",
    "purchase_cost": 0.15,
    "status": "active",
    "expiration_date": "2026-03-05",
    "last_reviewed": "2025-04-10",
    "next_review": "2025-10-10",
    "storage_conditions": "Store in a cool, dry place",
    "useful_life_years": 2,
    "current_stock": 3000,
    "image_url": "https://example.com/images/ibuprofen.png"
  }
]
