import os
from datetime import *

os.system('git add --a')
	
def default():
	os.system(f"git commit -m 'Commited'")

try:
	commit = input('\nCommit = ')
	if commit == '':
		print(default())
	os.system(f"git commit -m {commit}")
	os.system("git push -u origin main")
	
except KeyboardInterrupt:
	print('Process cancled.')