import os

with open('version') as file:
    version = file.read().rstrip()

version = '{}+{}'.format(version, os.environ['CIRCLE_BUILD_NUM'])

with open('.env.production', 'a') as file:
    file.write('\nVERSION=' + version)

with open('.env', 'w') as file:
    file.write('\nVERSION=' + version)

with open('version', 'w') as file:
    file.write(version)
