from fabric.api import task
from fabric.api import local, lcd


@task
def pip():
    with lcd("python"):
        local("rm -rf dist jrs.egg-info")
        local("./setup.py sdist")
        local("twine upload dist/{}".format(local("ls dist", capture=True).strip()))
