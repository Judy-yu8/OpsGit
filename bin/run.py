import argparse
import sys

from robot import  run_cli
from robot import  rebot_cli

def main(argv=None):
    # 允许外部传入argv，便于单元测试；默认为 sys.argv[1:]
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(description='run robotframework')
    parser.add_argument('filename', nargs='+', help='测试集文件或者目录')
    parser.add_argument('-t', '--runTest', action='store_true', help='是否执行用例')
    parser.add_argument('-r', '--rerun', type=int, default=0, help='执行失败的用例，参数是重试的次数')
    args = parser.parse_args(argv)

    # 待执行的目标（一个或多个 .robot 或目录）
    args_dest = list(args.filename)

    if args.runTest:
        # 首次执行
        run_cli(["--outputdir", "report"] + args_dest, exit=False)

    if args.rerun >= 1:
        # 失败用例重跑
        rerun_base = ["--outputdir", "report",
                      "--rerunfailed", "report/output.xml",
                      "--output", "output_rerun.xml"]
        for _ in range(args.rerun):
            run_cli(rerun_base + args_dest, exit=False)

        # 合并报告
        rebot_cli([
            "--outputdir", "report",
            "--output", "output.xml",
            "--report", "report.html",
            "--log", "log.html",
            "report/output.xml", "output_rerun.xml"
        ])
    return 0

if __name__ == "__main__":
    # 没传任何参数时给一个默认参数，方便在 PyCharm 里直接点运行
    if len(sys.argv) <= 1:
        sys.argv = [sys.argv[0], "-t", "../keywords/000_common_keyword.robot"]
    sys.exit(main())