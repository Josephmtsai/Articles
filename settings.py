# settings.py
from os.path import join, dirname
import dotenv


def init():
    dotenv_path = join(dirname(__file__), '.env')
    dotenv.load_dotenv(dotenv_path)
