import pytest
from pages.signin_page import SigninPage
from tests.conftest import *
from settings import BASE_URL


class TestSignin:
    def test_signin(
        self,
        email,
        password,
        signin_page: SigninPage
    ):
        signin_page.visit(BASE_URL)


