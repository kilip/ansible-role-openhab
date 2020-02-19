import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_package(host):
    java = host.package('zulu-8')
    openhab = host.package('openhab2')
    assert java.is_installed
    assert openhab.is_installed


def test_openhab_service(host):
    openhab = host.service('openhab2')
    assert openhab.is_running


def test_http_port(host):
    http = host.socket('tcp://0.0.0.0:8080')
    https = host.socket('tcp://0.0.0.0:8443')
    assert http.is_listening
    assert https.is_listening
