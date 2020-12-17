import os

os.system('cp -r pushc /usr/bin/')
os.system('cp -r push /usr/bin/')
os.system('cp -r pus /usr/bin/')
os.system('cp -r status /usr/bin/')
os.system('cp -r .gitignore ..')
os.system('cp -r .commit_push.py ..')
os.system('cp -r .push.py ..')
os.chdir('/usr/bin')
os.system('chmod +x push')
os.system('chmod +x pushc')
os.system('chmod +x pus')
os.system('chmod +x status')
