import os

os.system('cp -r pushc /bin/')
os.system('cp -r push /bin/')
os.system('cp -r pus /bin/')
os.system('cp -r status /bin/')
os.system('cp -r .gitignore ..')
os.system('cp -r .commit_push.py ..')
os.system('cp -r .push.py ..')
os.chdir('/bin')
os.system('chmod +x push')
os.system('chmod +x pushc')
os.system('chmod +x pus')
os.system('chmod +x status')
