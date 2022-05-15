import pytest
import subprocess


@pytest.fixture(autouse=True, scope="session")
def _auto_session(request):
    print("_auto_session(autouse=True, scope=session)")


@pytest.fixture(autouse=True, scope="class")
def _auto_class():
    print("_auto_class(autouse=True, scope=class) [B4]")
    subprocess.run(["ls", "/"])
    yield
    print("_auto_class(autouse=True, scope=class) [AFTER]")


@pytest.fixture(autouse=True, scope="function")
def _auto_fn():
    print("_auto_fn(autouse=True, scope=function)")


@pytest.fixture(scope="class")
def cls_fixture1():
    print("[global] cls_fixture1(scope=class)")


@pytest.fixture(scope="class")
def cls_fixture2():
    print("[global] cls_fixture2(scope=class)")


@pytest.fixture(scope="function")
def fn_fixture():
    print("[global] fn_fixture(scope=function)")
