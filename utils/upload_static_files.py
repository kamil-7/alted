import os
from ftplib import FTP_TLS
from ftplib import error_perm


def upload_files(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("STOR", name, localpath)
            ftp.storbinary('STOR ' + name, open(localpath, 'rb'))
        elif os.path.isdir(localpath):
            print("MKD", name)
            try:
                ftp.mkd(name)
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    raise

            print("CWD", name)
            ftp.cwd(name)
            upload_files(ftp, localpath)
            print("CWD", "..")
            ftp.cwd("..")


ftp_username = os.environ['FTP_USERNAME']
ftp_password = os.environ['FTP_PASSWORD']
tag = os.environ['VERSION']

working_directory = os.getcwd()

ftp = FTP_TLS("ftp.keycdn.com")
ftp.login(user=ftp_username, passwd=ftp_password)

ftp.cwd('alted')
ftp.mkd(tag)
ftp.cwd(tag)

upload_files(ftp, '{}/{}'.format(working_directory, 'static'))

ftp.quit()
