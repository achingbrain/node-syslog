import Options
from os import unlink, symlink, popen
from os.path import exists 

srcdir = '.'
blddir = 'build'
VERSION = '0.5.0'

def set_options(opt):
    opt.tool_options('compiler_cxx')

def configure(conf):
    conf.check_tool('compiler_cxx')
    conf.check_tool('node_addon')

def build(bld):
    obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
    obj.target = 'node-syslog'
    obj.source = 'node-syslog.cc'

def shutdown():
    # HACK to get node-syslog.node out of build directory.
    # better way to do this?
    if Options.commands['clean']:
	if exists('node-syslog.node'): unlink('node-syslog.node')
    else:
	if exists('build/default/node-syslog.node') and not exists('node-syslog.node'):
	    symlink('build/default/node-syslog.node', 'node-syslog.node')
