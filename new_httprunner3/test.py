import collections
from loguru import logger
from httprunner.utils import merge_variables
from httprunner.cli import tttest,main
from httprunner.loader import locate_file,load_debugtalk_functions,convert_relative_project_root_dir
# print('test start')
import os 
# import pytest
# xx = [
#     # '--version',
#     '--html=report.html',
#     # '/Users/gsky/my_github/python_about/new_httprunner3/tt01/testcases/demo_testcase_ref_test.py',
#     # '/Users/gsky/my_github/python_about/new_httprunner3/tt01/testcases/demo_testcase_request_test.py'
# ]
# pytest.main(xx)
# a1 =  {"ones": "$ones"}
# a2 =  {"base_url222": "$base_url2222"}
# xx = merge_variables(a1,a2)
# print(xx)
# print(xx)
main()
# tttest()
# print(convert_relative_project_root_dir('/Users/gsky/my_github/python_about/new_httprunner3/tt01/testcases/test_main_test.py'))
# load_debugtalk_functions()

def print_info(info_mapping):
    """ print info in mapping.

    Args:
        info_mapping (dict): input(variables) or output mapping.

    Examples:
        >>> info_mapping = {
                "var_a": "hello",
                "var_b": "world"
            }
        >>> info_mapping = {
                "status_code": 500
            }
        >>> print_info(info_mapping)
        ==================== Output ====================
        Key              :  Value
        ---------------- :  ----------------------------
        var_a            :  hello
        var_b            :  world
        ------------------------------------------------

    """
    if not info_mapping:
        return

    content_format = "{:<16} : {:<}\n"
    content = "\n==================== Output ====================\n"
    content += content_format.format("Variable", "Value")
    content += content_format.format("-" * 16, "-" * 29)

    for key, value in info_mapping.items():
        if isinstance(value, (tuple, collections.deque)):
            continue
        elif isinstance(value, (dict, list)):
            value = json.dumps(value)
        elif value is None:
            value = "None"

        content += content_format.format(key, value)

    content += "-" * 48 + "\n"
    logger.info(content)
    
info_mapping = {
                "var_a": "hello",
                "var_b": "world"
            }    
def omit_long_data(body, omit_len=512):
    """ omit too long str/bytes
    """
    if not isinstance(body, (str, bytes)):
        return body

    body_len = len(body)
    if body_len <= omit_len:
        return body

    omitted_body = body[0:omit_len]

    appendix_str = f" ... OMITTED {body_len - omit_len} CHARACTORS ..."
    if isinstance(body, bytes):
        appendix_str = appendix_str.encode("utf-8")

    return omitted_body + appendix_str

# xx = omit_long_data('012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789')
# print(xx) 
# print_info(info_mapping)
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