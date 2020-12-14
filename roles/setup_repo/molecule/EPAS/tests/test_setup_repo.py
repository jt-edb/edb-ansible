"""Role testing files using testinfra."""
import os

def test_epel_repo(host):
    cmd = host.run("yum repolist")
    assert 'Extra Packages for Enterprise Linux' in cmd.stdout

def test_edb_repo(host):
    cmd = host.run("yum repolist")
    assert 'EnterpriseDB RPMs' in cmd.stdout
