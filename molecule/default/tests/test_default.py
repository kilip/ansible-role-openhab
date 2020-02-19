import os
import Socket
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_http_port(host)
    http  = Socket('tcp://0.0.0.0:8080')
    https = Socket('tcp://0.0.0.0:8443')
    assert http.is_listening
    assert https.is_listening
