import subprocess
import sys
import click
import traceback
from datetime import datetime


@click.group()
def cli():
    pass


def cmd(command):
    [ret, msg] = subprocess.getstatusoutput(command)
    if ret != 0:
        click.echo(msg)
        sys.exit(-1)
    return ret, msg


@click.command(name="mr")
@click.option("-c", "--commit", is_flag=True, help="是否自动提交")
def create_mr(commit):
    """
    对本地当前分支的已commit未push的代码发起merge request
    """
    _, branch = cmd("git branch --show-current")
    commit_size = len(cmd("git status -s")[1])
    if commit and commit_size > 0:
        commit_title = click.prompt("Input Commit Message:")
        cmd('git add .;git commit -m "{}"'.format(commit_title))
    push_size = len(cmd("git log {} ^origin".format(branch))[1])
    if push_size == 0:
        click.secho("当前没有需要push的代码!!!", fg="red")
        sys.exit(-1)
    tmp_name = datetime.now().strftime("%Y%m%d%H%M")
    gen_mr = "git push origin head:{} -o merge_request.target={} ".format(tmp_name, branch)
    gen_mr += "-o merge_request.create -o merge_request.remove_source_branch -f"
    [_, ret] = cmd(gen_mr)
    click.echo(ret)


cli.add_command(create_mr)
if __name__ == '__main__':
    try:
        cli()
    except Exception as err:
        click.echo(err)
        traceback.print_exc()
        sys.exit(1)



