'''test pysftp.Connection.getcwd - uses py.test
until you issue a .chdir/cwd command paramiko returns None for .getcwd,
unless you have set default_path in the Connection args'''

# pylint: disable = W0142
# pylint: disable=E1101
from common import *


def test_getcwd_none(sftpserver):
    '''test .getcwd as the first operation - need pristine connection
    and no default_path arg'''
    with sftpserver.serve_content(VFS):
        cn = conn(sftpserver)
        cn['default_path'] = None
        with pysftp.Connection(**cn) as sftp:
            assert sftp.getcwd() is None


def test_getcwd_default_path(sftpserver):
    '''test .getcwd when using default_path arg'''
    with sftpserver.serve_content(VFS):
        with pysftp.Connection(**conn(sftpserver)) as sftp:
            assert sftp.getcwd() == '/home/test'


def test_getcwd_after_chdir(sftpserver):
    '''test getcwd after a chdir operation'''
    with sftpserver.serve_content(VFS):
        cn = conn(sftpserver)
        cn['default_path'] = None
        with pysftp.Connection(**cn) as sftp:
            sftp.chdir('/home/test/pub/foo1')
            assert sftp.getcwd() == '/home/test/pub/foo1'
