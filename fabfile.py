from fabric.api import *
from fabric.colors import green, yellow
from fabric.contrib.files import upload_template
from fabric.decorators import task
from fabric.operations import local


env.hosts = ['54.69.251.2']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/portfolio.pem'
env.shell = "/bin/bash -l -i -c"

@task
def hello():
    print(green("I'm alive!"))

@task
def create_file(file_name):
    local('touch ~/Desktop/{}.txt'.format(file_name))

@task
def new_directory():
    local('mkdir ~/Desktop/my_directory')

@task
def mk_directory_with_path(dir, dir_path):
    local('mkdir {}/{}'.format(dir_path, dir))

@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))


def restart_app():
    sudo("service supervisor restart")
    sudo("service nginx restart")


@task
def deploy():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
            run("git pull origin master")
            run("pip install -r requirements.txt")
            run("./manage.py migrate")
            run("./manage.py collectstatic --noinput")
            restart_app()

@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))

@task
def setup_nginx(project_name, server_name):
    upload_template("./deploy/nginx",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)

    restart_app()

@task
def setup_gunicorn(project_name, number_of_workers):
    with prefix("workon blog_analytics"):
    # with prefix("workon {}".format(project_name)):
        with cd("/home/ubuntu/{}".format(project_name)):
            run("pip install gunicorn")
            upload_template("./deploy/gunicorn",
                    "/home/ubuntu/{}/gunicorn.conf.py".format(project_name),
                    {'number_of_workers': number_of_workers,
                     'project_name': project_name},
                    use_sudo=True,
                    backup=False)

    restart_app()