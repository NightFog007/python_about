
from httprunner.cli import tttest,main
# print('test start')

# import pytest
# xx = [
#     # '--version',
#     '--html=report.html',
#     # '/Users/gsky/my_github/python_about/new_httprunner3/tt01/testcases/demo_testcase_ref_test.py',
#     # '/Users/gsky/my_github/python_about/new_httprunner3/tt01/testcases/demo_testcase_request_test.py'
# ]
# pytest.main(xx)
main()
tttest()


# import os,sys
# pt = os.getcwd()
# print(pt)

# def test_path(path: str) -> str:
#     if path.startswith("./"):
#         # Linux/Darwin, hrun ./test.yml
#         path = path[len("./") :]
#     elif path.startswith(".\\"):
#         # Windows, hrun .\\test.yml
#         path = path[len(".\\") :]

#     path = ensure_path_sep(path)
#     project_meta = load_project_meta(path)

#     if os.path.isabs(path):
#         absolute_path = path
#     else:
#         absolute_path = os.path.join(project_meta.RootDir, path)

#     if not os.path.isfile(absolute_path):
#         logger.error(f"Invalid testcase file path: {absolute_path}")
#         sys.exit(1)

#     return absolute_path

# nn = test_path(pt)
# print("[bold magenta]2021-08-04 11:25:21↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓[/bold magenta]!",locals())
# print(nn)
# print("[bold magenta]2021-08-04 11:25:21↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑[/bold magenta]!")


# def inc(x):
#     return x+1

# def test_anset():
#     assert inc(3) == 5
    
# def test_anset2():
#     assert inc(4) == 5