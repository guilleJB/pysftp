'''test pysftp module - uses py.test'''

# pylint: disable = W0142
# pylint: disable=E1101
from common import *

def test_connection_with():
    '''connect to a public sftp server'''
    with pysftp.Connection(**SFTP_PUBLIC) as sftp:
        assert sftp.listdir() == ['pub', 'readme.sym', 'readme.txt']


def test_connection_bad_host():
    '''attempt connection to a non-existing server'''
    with pytest.raises(pysftp.ConnectionException):
        sftp = pysftp.Connection(host='',
                                 username='demo',
                                 password='password')
        sftp.close()

def test_connection_bad_credentials():
    '''attempt connection to a non-existing server'''
    with pytest.raises(pysftp.SSHException):
        copts = SFTP_PUBLIC.copy()
        copts['password'] = 'badword'
        with pysftp.Connection(**copts) as sftp:
            pass

def test_connection_good():
    '''connect to a public sftp server'''
    sftp = pysftp.Connection(**SFTP_PUBLIC)
    sftp.close()


def test_getcwd():
    '''test .getcwd'''
    sftp = pysftp.Connection(**SFTP_PUBLIC)
    assert sftp.getcwd() == None
    sftp.chdir('pub')
    assert sftp.getcwd() == '/home/test/pub'
    sftp.close()


