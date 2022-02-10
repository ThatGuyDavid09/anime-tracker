import os
import pyperclip
from pprint import pprint

from backend.apis.funimation import Funimation

fn = Funimation(os.environ.get("CRUNCHYROLL_EMAIL"), os.environ.get("FUNIMATION_PSWD"))
# pyperclip.copy(fn.r.text)
# print(fn.token)
r = fn.search("tensei slime")
print(r.status_code)
pyperclip.copy(r.text)
pprint(r.text)
