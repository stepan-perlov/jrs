from fabric.api import task
from fabric.api import local, lcd


@task
def pip():
    with lcd("tools"):
        local("rm -rf dist jrstools.egg-info")
        local("./setup.py sdist")
        local("twine upload dist/{}".format(local("ls dist", capture=True).strip()))

@task
def mezzo():
    local("mkdir -p build/jrstools")
    local("cp -r tools/jrstools build/jrstools/jrstools")
    local("cp tools/setup.py build/jrstools/setup.py")
    with lcd("build"):
        local("tar cf jrstools.tar.gz jrstools")
        local("cp jrstools.tar.gz /opt/mezzo/dependencies/jrstools.tar.gz")
