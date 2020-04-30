import pytest
from .session import Session
from .inf import Inf
from .client import Client
from pydpclient import get_protocol_version, code_to_string,\
    get_allocated_memory_size, cl_session_create, cl_session_set_id,\
    cl_session_set_inf_id, cl_session_get_size, cl_session_resize,\
    cl_session_set_var, cl_session_get, cl_session_free, cl_inf_create,\
    cl_inf_set_id, cl_inf_set_templates, cl_inf_get_vars_cnt,\
    cl_inf_get_dicts_cnt, cl_inf_resize, cl_inf_set_var, cl_inf_get_var,\
    cl_inf_set_dict, cl_inf_get_dict, cl_inf_free, cl_cmd_purge_session,\
    cl_cmd_purge_inf, cl_cmd_send_inf, cl_cmd_init, cl_cmd_send_session,\
    cl_cmd_request, cl_answer_get_size, cl_answer_free


@pytest.fixture
def conn_str(request):
    return request.config.getoption("--conn_str")


class TestOthers:

    def test_protocol_version(self):
        assert get_protocol_version() == 6

    def test_code_to_strong(self):
        assert code_to_string(1) == ''
        assert code_to_string(0) == 'Success'
        assert code_to_string(-1) == 'Invalid arguments'

    def test_allocated_memory(self):
        assert get_allocated_memory_size() == 0


class TestSession:

    session = None
    _var_name_session_1 = "variable_name"
    _var_name_session_2 = "имя_переменной"
    _var_value_session_1 = "variable_value"
    _var_value_session_2 = "значение переменной"

    def setup_class(self):
        self.session = cl_session_create()
        cl_session_set_id(self.session, 1)
        cl_session_set_inf_id(self.session, 2)

    def test_resize(self):
        assert cl_session_get_size(self.session) == 0
        cl_session_resize(self.session, 2)
        assert cl_session_get_size(self.session) == 2

    def test_variables(self):
        cl_session_set_var(
            self.session, 0,
            self._var_name_session_1,
            self._var_value_session_1,
        )
        assert cl_session_get(self.session, 0) == (
            0, self._var_name_session_1, self._var_value_session_1,
        )
        cl_session_set_var(
            self.session, 1,
            self._var_name_session_2,
            self._var_value_session_2,
        )
        assert cl_session_get(self.session, 1) == (
            0, self._var_name_session_2, self._var_value_session_2,
        )

    def teardown_class(self):
        assert cl_session_free(self.session) == 0
        del self.session


class TestInf:

    inf = None
    _var_name_inf_1 = "inf_var_name"
    _var_name_inf_2 = "имя переменной инфа"
    _var_value_inf_1 = "inf_var_value"
    _var_value_inf_2 = "значение переменной инфа"
    _dict_name_inf_1 = "inf_dict_name"
    _dict_name_inf_2 = "имя словаря инфа"
    _dict_value_inf_1 = "inf_dict_value"
    _dict_value_inf_2 = "значение словаря инфа"

    def setup_class(self):
        self.inf = cl_inf_create()
        cl_inf_set_id(self.inf, 2)
        cl_inf_set_templates(self.inf, "foo")

    def test_resize(self):
        assert cl_inf_get_vars_cnt(self.inf) == 0
        assert cl_inf_get_dicts_cnt(self.inf) == 0
        assert cl_inf_resize(self.inf, 2, 2) == 0
        assert cl_inf_get_vars_cnt(self.inf) == 2
        assert cl_inf_get_dicts_cnt(self.inf) == 2

    def test_variables(self):
        cl_inf_set_var(self.inf, 0, self._var_name_inf_1, self._var_value_inf_1)
        cl_inf_set_var(self.inf, 1, self._var_name_inf_2, self._var_value_inf_2)
        assert cl_inf_get_var(self.inf, 0) == (
            0, self._var_name_inf_1, self._var_value_inf_1,
        )
        assert cl_inf_get_var(self.inf, 1) == (
            0, self._var_name_inf_2, self._var_value_inf_2,
        )

    def test_dicts(self):
        cl_inf_set_dict(
            self.inf, 0, self._dict_name_inf_1, self._dict_value_inf_1,
        )
        cl_inf_set_dict(
            self.inf, 1, self._dict_name_inf_2, self._dict_value_inf_2,
        )
        assert cl_inf_get_dict(self.inf, 0) == (
            0, self._dict_name_inf_1, self._dict_value_inf_1,
        )
        assert cl_inf_get_dict(self.inf, 1) == (
            0, self._dict_name_inf_2, self._dict_value_inf_2,
        )

    def teardown_class(self):
        assert cl_inf_free(self.inf) == 0
        del self.inf


class TestServer:

    timeout = 1000
    pack_flag = 1

    session_id = 1
    inf_id = 1

    answer = None
    session = None
    inf = None

    def setup_class(self):
        self.inf = cl_inf_create()
        cl_inf_resize(self.inf, 1, 0)
        cl_inf_set_id(self.inf, self.inf_id)
        cl_inf_set_var(self.inf, 0, "INF_PERSON", "demo")
        self.session = cl_session_create()
        cl_session_set_id(self.session, self.session_id)
        cl_session_set_inf_id(self.session, self.inf_id)
        cl_session_resize(self.session, 0)

    def test_cleanup_server(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed")
        assert cl_cmd_purge_session(
            self.session_id, conn_str, self.timeout, self.pack_flag,
        ) == 0
        assert cl_cmd_purge_inf(
            self.inf_id, conn_str, self.timeout, self.pack_flag,
        ) == 0

    def test_send_inf(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed")
        assert cl_cmd_send_inf(
            self.inf, conn_str, self.timeout, self.pack_flag,
        ) == 0

    def test_init_communication(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed")
        assert cl_cmd_init(
            self.session_id, self.inf_id,
            conn_str, self.timeout, self.pack_flag,
        ) == (0, 0)

    def test_send_session(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed")
        assert cl_cmd_send_session(
            self.session, conn_str, self.timeout, self.pack_flag,
        ) == 0

    def test_request(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed")
        code, self.answer, missed_data_mask = cl_cmd_request(
            self.session_id, self.inf_id, "покажи юзерлинк", self.session,
            conn_str, self.timeout, self.pack_flag,
        )
        assert code == 0
        assert self.answer is not None

    def test_answer(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed")
        items = cl_answer_get_size(self.answer)
        assert items > 0

    def teardown_class(self):
        assert cl_session_free(self.session) == 0
        del self.session
        assert cl_inf_free(self.inf) == 0
        del self.inf
        if self.answer is not None:
            assert cl_answer_free(self.answer) == 0
            del self.answer


class TestSessionClass:

    session = None
    test_var_1 = ("test1", "test2")
    test_var_2 = ("test3", "test4")

    def setup_class(self):
        self.session = Session()
        self.session.set_id(1)
        self.session.set_inf_id(1)

    def test_append(self):
        assert self.session.get_size() == 0
        self.session.append_var(*self.test_var_1)
        assert self.session.get_size() == 1
        assert self.session.get_var(0) == self.test_var_1

    def test_get_vars(self):
        self.session.append_var(*self.test_var_2)
        assert self.session.get_vars() == [self.test_var_1, self.test_var_2]

    def test_pop(self):
        assert self.session.pop() == self.test_var_2
        assert self.session.get_size() == 1

    def test_pop_index(self):
        assert self.session.pop(0) == self.test_var_1
        assert self.session.get_size() == 0

    def teardown_class(self):
        del self.session


class TestInfClass:

    inf = None
    test_var_1 = ("var1", "var2")
    test_var_2 = ("var3", "var4")
    test_dict_1 = ("dict1", "dict2")
    test_dict_2 = ("dict3", "dict4")

    def setup_class(self):
        self.inf = Inf()
        self.inf.set_id(1)

    def test_append_var(self):
        assert self.inf.get_vars_number() == 0
        self.inf.append_var(*self.test_var_1)
        assert self.inf.get_vars_number() == 1
        assert self.inf.get_var(0) == self.test_var_1

    def test_get_vars(self):
        self.inf.append_var(*self.test_var_2)
        assert self.inf.get_vars() == [self.test_var_1, self.test_var_2]

    def test_pop_var(self):
        assert self.inf.pop_value() == self.test_var_2
        assert self.inf.get_vars_number() == 1

    def test_pop_var_index(self):
        assert self.inf.pop_value(0) == self.test_var_1
        assert self.inf.get_vars_number() == 0

    def test_append_dict(self):
        assert self.inf.get_dicts_number() == 0
        self.inf.append_dict(*self.test_dict_1)
        assert self.inf.get_dicts_number() == 1
        assert self.inf.get_dict(0) == self.test_dict_1

    def test_get_dicts(self):
        self.inf.append_dict(*self.test_dict_2)
        assert self.inf.get_dicts() == [self.test_dict_1, self.test_dict_2]

    def test_pop_dict(self):
        assert self.inf.pop_dict() == self.test_dict_2
        assert self.inf.get_dicts_number() == 1

    def test_pop_dict_index(self):
        assert self.inf.pop_dict(0) == self.test_dict_1
        assert self.inf.get_dicts_number() == 0

    def teardown_class(self):
        del self.inf


class TestConnection:

    session = None
    inf = None
    client = None
    answer = None

    def setup_class(self):
        self.session = Session()
        self.session.set_id(1)
        self.session.set_inf_id(1)
        self.inf = Inf()
        self.inf.set_id(1)

    def test_cleanup_server(self, conn_str):
        self.client = Client(conn_str)
        if not conn_str:
            pytest.skip("No connection string passed!")
        self.client.purge_inf(1)
        self.client.purge_session(1)

    def test_send_session(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed!")
        Client(conn_str).send_session(self.session)

    def test_send_inf(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed!")
        client = Client(conn_str)
        client.send_inf(self.inf)

    def test_init(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed!")
        client = Client(conn_str)
        client.initialize(1, 1)

    def test_request(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed!")
        client = Client(conn_str)
        self.answer, missed_data_mask = client.request(
            self.session, "привет",
        )
        assert client.is_success(missed_data_mask)
        assert self.answer.get_size() > 0

    def teardown_class(self):
        del self.session
        del self.inf
        del self.client


class TestEasy:

    SID = 2
    SC = dict()
    BID = 1
    BC = {
        "inf_person": "demo",
        "inf_name": '',
    }
    RQ = "1"

    def test_easy_request(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed!")
        self.client = Client(connection_string=conn_str)
        ans = self.client.easy_request(self.RQ, self.SID, self.SC, self.BID, self.BC)
        assert len(ans["text"]) > 0

    def test_string_postprocessing(self):
        test_string = ' Hello , world named "  Terra  " ! &#59(  This is test  ) .=|:):( '
        check_string = 'Hello, world named "Terra"!; (This is test). =| :) :('
        client = Client()
        assert client.string_postprocessing(test_string) == check_string

    def test_easy_update(self, conn_str):
        if not conn_str:
            pytest.skip("No connection string passed!")
        self.client = Client(connection_string=conn_str)
        self.client.easy_update(self.SID, self.BID, self.SC)
