import subprocess

def execute_cmd(cmd):
    output=subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True).stdout
    output=output.replace('\r', '').replace('\n', '')
    return output
