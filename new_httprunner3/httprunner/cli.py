import argparse
import enum
import os
import sys
import time

import pytest
from loguru import logger
from sentry_sdk import capture_message

from httprunner import __description__, __version__
from httprunner.compat import ensure_cli_args
from httprunner.ext.har2case import init_har2case_parser, main_har2case
from httprunner.make import init_make_parser, main_make
from httprunner.scaffold import init_parser_scaffold, main_scaffold
from httprunner.utils import init_sentry_sdk

from rich import print
import pdb

init_sentry_sdk()


# 定义可执行命令关键字和help语句
def init_parser_run(subparsers):
    sub_parser_run = subparsers.add_parser(
        "run", help="0813Make HttpRunner testcases and run with pytest."
    )
    return sub_parser_run

# 我自定义的一个命令,执行脚本并且自动生成测试报告,但是通过修改源码,run也会自动生成报告,所以这个命令define可以不再使用了
def init_parser_define(subparsers):
    sub_parser_run = subparsers.add_parser(
        "define", help="run test and generate reports"
    )
    return sub_parser_run


def main_run(extra_args) -> enum.IntEnum:
    capture_message("start to run")
    # keep compatibility with v2
    extra_args = ensure_cli_args(extra_args)

    tests_path_list = []
    extra_args_new = []
    for item in extra_args:
        if not os.path.exists(item):
            # item is not file/folder path
            extra_args_new.append(item)
        else:
            # item is file/folder path
            tests_path_list.append(item)

    if len(tests_path_list) == 0:
        # has not specified any testcase path
        logger.error(f"No valid testcase path in cli arguments: {extra_args}")
        sys.exit(1)
        
    # pdb.set_trace()

    testcase_path_list = main_make(tests_path_list)
    if not testcase_path_list:
        logger.error("No valid testcases found, exit 1.")
        sys.exit(1)

    if "--tb=short" not in extra_args_new:
        extra_args_new.append("--tb=short")

    extra_args_new.extend(testcase_path_list)
    logger.info(f"start to run tests with pytest. HttpRunner version: {__version__}")

    time_stamp = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    report_name = './reports/'+ time_stamp+'report'+'.html'
    extra_args_new.append('--html=%s'%report_name )
    extra_args_new.append('--self-contained-html' )
    extra_args_new.append('--alluredir=./my_allure_results' )
    extra_args_new.append('--clean-alluredir' )

    return pytest.main(extra_args_new)


#^ 框架第一个调的方法在此
def main():
    """ API test: parse command line options and run commands.
    """
    
    #argparse是一个Python模块：命令行选项、参数和子命令解析器。
    #argparse 模块可以让人轻松编写用户友好的命令行接口。程序定义它需要的参数，然后 argparse 将弄清如何从 sys.argv 解析出那些参数。 argparse 模块还会自动生成帮助和使用手册，并在用户给程序传入无效参数时报出错误信息。
    
    #1. 生成ArgumentParser对象(解析器)
    parser = argparse.ArgumentParser(description=__description__)
    #2. 调用 add_argument() 方法添加参数
    parser.add_argument(
        "-V", "--version", dest="version", action="store_true", help="show version_mydefine20210813"
    )
    # argparse 使用add_subparsers()方法去创建子命令
    subparsers = parser.add_subparsers(help="sub-command help")
    #3. 如果有子命令的话,生成子解析器
    # sub_parser_test = subparsers.add_parser("test",help="this is teast")
    #4. 为子解析器添加参数
    # sub_parser_test.add_argument(
    #     "project_name", type=str, nargs="?", help="Specify new project name."
    # )
    sub_parser_run = init_parser_run(subparsers)
    sub_parser_scaffold = init_parser_scaffold(subparsers)
    sub_parser_har2case = init_har2case_parser(subparsers)
    sub_parser_make = init_make_parser(subparsers)
    sub_parser_define = init_parser_define(subparsers)
    
    print("[bold magenta]2021-08-04 16:10:48↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[/bold magenta]!")
    print(sys.argv)
    print("[bold magenta]2021-08-04 16:10:48↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[/bold magenta]!")

    if len(sys.argv)>2:
        if sys.argv[2].startswith('--html'):
            print(sys.argv[1])
    
    if len(sys.argv) == 1:
        # httprunner
        parser.print_help()
        sys.exit(0)
    elif len(sys.argv) == 2:
        # print help for sub-commands
        if sys.argv[1] in ["-V", "--version"]:
            # httprunner -V
            print(f"{__version__}")
        elif sys.argv[1] in ["-h", "--help"]:
            # httprunner -h
            parser.print_help()
        elif sys.argv[1] == "startproject":
            # httprunner startproject
            sub_parser_scaffold.print_help()
        elif sys.argv[1] == "har2case":
            # httprunner har2case
            sub_parser_har2case.print_help()
        elif sys.argv[1] == "run":
            # httprunner run
            pytest.main(["-h"])
        elif sys.argv[1] == "make":
            # httprunner make
            sub_parser_make.print_help()
        elif sys.argv[1] == "define":
            # httprunner run
            pytest.main(["-h"])
        sys.exit(0)
    elif (
        len(sys.argv) == 3 and sys.argv[1] == "run" and sys.argv[2] in ["-h", "--help"]
    ):
        # httprunner run -h
        pytest.main(["-h"])
        sys.exit(0)

    extra_args = []
    if len(sys.argv) >= 2 and sys.argv[1] in ["run", "locusts","define"]:
        args, extra_args = parser.parse_known_args()
    else:
        args = parser.parse_args()

    if args.version:
        print(f"{__version__}")
        sys.exit(0)

    if sys.argv[1] == "run":

        sys.exit(main_run(extra_args))
        
    elif sys.argv[1] == "startproject":
        main_scaffold(args)
    elif sys.argv[1] == "har2case":
        main_har2case(args)
    elif sys.argv[1] == "make":
        main_make(args.testcase_path)
    elif sys.argv[1] == "define":
        # print("[bold magenta]2021-08-04 15:52:59↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[/bold magenta]!",locals())
        # print(extra_args)
        print("[bold magenta]2021-08-04 15:52:59↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[/bold magenta]!")



def main_hrun_alias():
    """ command alias
        hrun = httprunner run
    """
    if len(sys.argv) == 2:
        if sys.argv[1] in ["-V", "--version"]:
            # hrun -V
            sys.argv = ["httprunner", "-V"]
        elif sys.argv[1] in ["-h", "--help"]:
            pytest.main(["-h"])
            sys.exit(0)
        else:
            # hrun /path/to/testcase
            sys.argv.insert(1, "run")
    else:
        sys.argv.insert(1, "run")

    main()


def main_make_alias():
    """ command alias
        hmake = httprunner make
    """
    sys.argv.insert(1, "make")
    main()


def main_har2case_alias():
    """ command alias
        har2case = httprunner har2case
    """
    sys.argv.insert(1, "har2case")
    main()

def tttest():
    # print("this is cli.py 's  test method!")
    print("this is cli.py 's  [bold magenta]test method![/bold magenta]!", ":vampire:", locals())
    print("[bold magenta]2021-08-04 09:59:03↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[/bold magenta]!",locals())
    print("[bold magenta]2021-08-04 09:59:03↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[/bold magenta]!")




if __name__ == "__main__":
    main()


