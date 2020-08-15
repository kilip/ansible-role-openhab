def test_user(host):
    toni = host.user('toni')
    openhab = host.user('openhab')

    assert host.group('openhab').exists
    assert host.group('toni').exists

    assert toni.exists
    assert openhab.exists


def test_directory(host):
    config = host.file('/srv/openhab/config')
    userdata = host.file('/srv/openhab/userdata')

    assert config.exists
    assert config.user == 'toni'
    assert config.group == 'openhab'

    assert userdata.exists
    assert userdata.user == 'openhab'
    assert userdata.group == 'openhab'


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
    assert openhab.is_enabled
    assert openhab.is_running


def test_http_port(host):
    http = host.socket('tcp://0.0.0.0:8080')
    https = host.socket('tcp://0.0.0.0:8443')
    assert http.is_listening
    assert https.is_listening
