def pytest_addoption(parser):
    parser.addoption(
        "--conn_str", action="store", default='', help="Address of InfServer",
    )
