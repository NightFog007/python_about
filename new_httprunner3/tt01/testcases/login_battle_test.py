
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseDemoTestcaseRef(HttpRunner):

    config = (
        Config("battle login request")
        .variables(
            **{
                "username": "criss",
                "password": "criss",
            }
        )
        .base_url("http://127.0.0.1:12356")
        .verify(False)
        .export(*["foo3"])
    )

    teststeps = [
        Step(
            RunRequest("post form data")
            .post('/login')
            .with_data("username=$username&password=$password")
            .validate()
            .assert_equal("status_code", 200)
            .assert_startswith("body", b"please select One Equipment:\n10001:Knife\n10002:Big Sword\n10003:KuiHuaBaoDian")
        ),
        
        Step(
            RunRequest("selectEq请求值为1")
            .post('/selectEq')
            .with_data("equipmentid=1")
            .extract()
            .with_jmespath("cookies.beaker.seeion.id", "foo3")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.equipmentid", "1")
            
        ),
        
        
    ]



class TestCaseDemoTestcaseRef22(HttpRunner):

    config = (
        Config("battle login request")
        .variables(
            **{
                "username": "criss",
                "password": "criss",
            }
        )
        .base_url("http://127.0.0.1:12356")
        .verify(False)
        .export(*["foo3"])
    )

    teststeps = [
        Step(
            RunRequest("post form data")
            .post('/login')
            .with_data("username=$username&password=$password")
            .validate()
            .assert_equal("status_code", 200)
            .assert_startswith("body", b"please select One Equipment:\n10001:Knife\n10002:Big Sword\n10003:KuiHuaBaoDian")
        ),
        
        Step(
            RunRequest("selectEq请求值为1")
            .post('/selectEq')
            .with_data("equipmentid=1")
            .extract()
            .with_jmespath("cookies.beaker.seeion.id", "foo3")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.equipmentid", "1")
            
        ),
        
        
    ]

if __name__ == "__main__":
    TestCaseDemoTestcaseRef().test_start()
    TestCaseDemoTestcaseRef22().test_start()
