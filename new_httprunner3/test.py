
from httprunner.cli import tttest,main
print('test start')


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


