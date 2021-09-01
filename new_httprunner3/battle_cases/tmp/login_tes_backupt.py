import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters


class TestCaseBattle(HttpRunner):
    # 引入csv文件参数
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {"username-password-res":"${P(battle_cases/account.csv)}"}
        ),
    )
    def test_start(self,param):
        super().test_start(param)

    config = (
        Config("battle: login")
        # .variables(
        #     **{
        #         "username": "gsky",
        #         "password": "gsky",
        #     }
        # )
        .base_url("http://101.34.170.225:12356")
        .verify(False)
    )

    teststeps = [
        # Step(
            # RunTestCase("request with login")
            # .with_variables(
            #     **{"foo1": "testcase_ref_bar1", "expect_foo1": "testcase_ref_bar1"}
            # )
            # .call(DemoTestcaseRequest)
            # .export(*["foo3"])
        # ),
        Step(
            RunRequest("post form data")
            # .with_variables(**{"username": "test1","password":"test1","res":"please select One Equipment"})

            .post("/login")
            # .with_headers(
            #     **{
            #         "User-Agent": "HttpRunner/${get_httprunner_version()}",
            #         "Content-Type": "application/x-www-form-urlencoded",
            #     }
            # )

            # .with_data("username222=$username&password222=$password")
            .with_data({"username":"$username","password":"$password"})
            .validate()
            .assert_equal("status_code", 200)
            # .assert_contains("body", b"please select One Equipment")
            # .assert_contains("body", "${res}")
            .assert_regex_match("body", "${res}")
            # .assert_startswith("body", b'please select One Equipme')
            # .assert_equal("body.form.foo1", "bar1")
            # .assert_equal("body.form.foo2", "bar21")
        ),
    ]


if __name__ == "__main__":
    TestCaseBattle().test_start()
