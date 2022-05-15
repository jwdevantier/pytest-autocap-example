import pytest


class TestModBClass:
    def test_one(self, cls_fixture1):
        print("tests/modb/test_mod_a/TestModBCls::test_one fn")

    @pytest.mark.parametrize("x", [1, 2])
    def test_two(self, x):
        print("tests/modb/test_mod_a/TestModBCls::test_two fn")
