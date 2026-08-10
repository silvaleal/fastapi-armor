from database import Database
from dotenv import load_dotenv

load_dotenv()

seeders = [
    """
    CREATE TABLE IF NOT EXISTS queue (
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        field VARCHAR(30) NOT NULL,
        data TEXT NOT NULL,
        status INT DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS api_requests (
        id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        api_token VARCHAR(255) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """,
]

for seed in seeders:
    Database().commit(seed)