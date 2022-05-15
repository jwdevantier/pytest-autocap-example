import pytest


class TestModAClass:
    @pytest.fixture(scope="class", params=["p1", "p2"])
    def cls_fixture2(cls, request):
        print(f"cls_fixture2[{request.param}")

    def test_one(self):
        print("tests/moda/test_mod_a/TestModACls::test_one fn")

    def test_two(self):
        print("tests/moda/test_mod_a/TestModACls::test_two fn")


def test_function_test(autocap_dir):
    with open(autocap_dir / "stuff.txt", "w") as fh:
        fh.write("hello, world\n")
    pass
