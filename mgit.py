import datetime
import os
import stat
import subprocess

def mgit(path, git_args):
    print '# mgit %s %s started at %s' % (path, ' '.join(git_args), datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))
    _run_all(path, git_args)
    print '# mgit finished at %s' % (datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))

def _run_all(path, git_args):
    git_dir = path + "/.git"
    if os.path.isdir(git_dir):
        _run_one(path, git_dir, git_args)
    else:
        for f in os.listdir(path):
            child_path = os.path.join(path, f)
            s = os.stat(child_path)
            if stat.S_ISDIR(s[stat.ST_MODE]):
                _run_all(child_path, git_args)

def _run_one(work_tree, git_dir, git_args):
    cmd = 'git --work-tree=%s --git-dir=%s' % (work_tree, git_dir)
    for arg in git_args:
        cmd += ' ' + arg
    print '$ %s' % cmd
    p = subprocess.Popen(cmd, shell=True)
    retval = p.wait()
