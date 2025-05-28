from tortoise import Tortoise
import os
from dotenv import load_dotenv


# Get the directory where this file is located
current_dir = os.path.dirname(__file__)

# Go one directory up to project root, where .env lives
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# Build path to .env file
dotenv_path = os.path.join(project_root, '.env')

# Load .env variables
load_dotenv(dotenv_path)

built_db_url = (
    f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@{os.getenv('POSTGRES_HOST')}:{int(os.getenv('POSTGRES_PORT'))}/{os.getenv('POSTGRES_DB')}"
)

print(built_db_url)

async def init_db():
    await Tortoise.init(
        db_url=built_db_url,
        modules={"models": ["db.models"]}
    )
    await Tortoise.generate_schemas()
    print('connection established')
