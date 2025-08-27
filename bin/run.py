import argparse
from robot import  run_cli
from robot import  rebot_cli

parser = argparse.ArgumentParser(description='run robotframework')
parser.add_argument('filename',nargs='+',help='测试套件或者目录')
parser.add_argument('-t', '--runTest',action='store_true',help='是否执行用例')
parser.add_argument('-r', '--rerun',type=int,help='执行失败的用例，参数是重试的次数')
args = parser.parse_args()

args_dest = args.filename  #获取待执行的robot文件或者目录

if args.runTest:   #是否执行测试用例
    args_dest = ["--outputdir","report"] + args_dest
    run_cli(args_dest,exit=False)

if args.rerun >= 1:    #失败用例重新执行
    args_dest = ["--outputdir","report","--rerunfailed","report/output.xml","--output","output_rerun.xml"] + args_dest
    for i in range(args.rerun):
        run_cli(args_dest,exit=False)
        #将重新执行的报告合并到首次执行的报告中
        rebot_cli(["--outputdir","report","--output","output.xml","--report","report.html","--log","log.html","--merge","report/output.xml","report/output_rerun.xml"])

