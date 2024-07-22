import json
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent # 해당 폴더 의미함. 

def get_secret(
	key: str, 
	default_value: Optional[str] = None,
	json_path: str = str(BASE_DIR / "secret.json")
	):

	with open(json_path) as f: 
		s = json.loads(f.read())
	try:
		return s[key]
	except KeyError:
		if default_value:
			return default_value
		raise EnviromentError("set the {key} env variable")

MONGO_DB_NAME = get_secret("MONGO_DB_NAME")
MONGO_URL = get_secret("MONGO_URL")
NAVER_API_ID = get_secret("NAVER_API_ID")
NAVER_API_SECRET = get_secret("NAVER_API_SECRET")
if __name__ == '__main__':
	world = get_secret("hello")
	