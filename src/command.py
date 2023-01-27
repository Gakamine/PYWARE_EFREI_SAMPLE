import subprocess

def execute_cmd(cmd):
    output=subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
    output=output.replace('\r', '').replace('\n', '')
    return output