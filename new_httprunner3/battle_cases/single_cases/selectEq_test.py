
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

# from testcases.demo_testcase_request_test import (
#     TestCaseDemoTestcaseRequest as DemoTestcaseRequest,
# )

from login_test import TestCaseBattle as loginRequest

class TestCaseDemoTestcaseRef(HttpRunner):

    config = (
        Config("battle: login")
        .variables(
            **{
                "username": "gsky",
                "password": "gsky",
            }
        )
        .base_url("http://101.34.170.225:12356")
        .verify(False)
    )

    teststeps = [
        # Step(
        #     RunTestCase("request with login")
        #     .with_variables(
        #         **{"username": "$username", "password": "$password"}
        #     )
        #     .call(loginRequest)
        #     # .export(*["foo3"])
        # ),
        Step(
            RunRequest("post form data")
            # .with_variables(**{"foo1": "bar1"})
            .post("/selectEq")
            # .with_headers(
            #     **{
            #         "User-Agent": "HttpRunner/${get_httprunner_version()}",
            #         "Content-Type": "application/x-www-form-urlencoded",
            #     }
            # )
            .with_data("equipmentid=10001")
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("body.Message", "your pick up equipmentid")
            # .assert_startswith("body", b'please select One Equipme')
            # .assert_equal("body.form.foo1", "bar1")
            # .assert_equal("body.form.foo2", "bar21")
        ),
    ]


if __name__ == "__main__":
    TestCaseDemoTestcaseRef().test_start()
