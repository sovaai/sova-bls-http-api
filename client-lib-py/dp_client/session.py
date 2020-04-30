from typing import Tuple, List, Optional
from .exceptions import DPClientException
from pydpclient import SessionDataPointerType, cl_session_create,\
    cl_session_free, cl_session_set_id, cl_session_set_inf_id,\
    cl_session_get_size, cl_session_resize, cl_session_set_var, cl_session_get


class Session:
    """
    Класс для работы с объектами сессий (которые являются структурами в Си).
    Сами объекты типа SessionDataPointerType являются
    указателями на структуры в Си.
    """

    session_id = None
    inf_id = None

    def __init__(
            self,
            session_obj: Optional[SessionDataPointerType] = None,
            session_id: Optional[int] = None,
            inf_id: Optional[int] = None,
            session_context: Optional[dict] = None,
    ):
        """
        Инициализация объекта сессии. Си-структура будет создана,
        если не был передан объект типа SessionDataPointerType.
        Args:
            session_obj: объект-указатель на структуру SessionData.
        """
        self.session_obj = session_obj if session_obj is not None \
            else cl_session_create()
        if session_id is not None:
            self.set_id(session_id)
        if inf_id is not None:
            self.set_inf_id(inf_id)
        if session_context is not None:
            for key, value in session_context.items():
                self.append_var(key, value)

    def __del__(self):
        """
        Высвобождение занятой объектом памяти (как объектом-указателем,
        так и самой стрктурой, расположенной по этому указателю).
        """
        ret_code: int = cl_session_free(self.session_obj)
        del self.session_obj
        if ret_code:
            raise DPClientException(ret_code)

    # Базовые функции

    def set_id(self, session_id: int) -> None:
        """
        Установка идентификатора сессии.
        Args:
            session_id: идентификатор сессии
        """
        if session_id < 0:
            raise DPClientException(-1)
        self.session_id = session_id
        cl_session_set_id(self.session_obj, session_id)
        return

    def get_id(self):
        """
        Получение идентификатора сессии.
        Returns:
            идентификатор сессии.
        """
        return self.session_id

    def set_inf_id(self, inf_id: int) -> None:
        """
        Установка идентификатора инфа.
        Args:
            inf_id: идентификатор инфа.
        """
        if inf_id < 0:
            raise DPClientException(-1)
        self.inf_id = inf_id
        cl_session_set_inf_id(self.session_obj, inf_id)
        return

    def get_inf_id(self):
        """
        Получение идентификатора инфа
        Returns:
            идентификатор инфа.
        """
        return self.inf_id

    def get_size(self) -> int:
        """
        Получение числа переменных, записанных в объекте сессии.
        Returns:
            число переменных.
        """
        return cl_session_get_size(self.session_obj)

    def resize(self, new_size: int) -> None:
        """
        Изменение числа переменных сессии.
        При этом старые переменные будут удалены.
        Args:
            new_size: новое количество переменных.
        """
        if new_size < 0:
            raise DPClientException(-1)
        ret_code = cl_session_resize(self.session_obj, new_size)
        if ret_code:
            raise DPClientException(ret_code)
        return

    def set_var(self, pos: int, var_name: str, var_value: str) -> None:
        """
        Установка имени и значения переменной по ее индексу (нумерация с нуля).
        Args:
            pos: индекс  переменной.
            var_name: имя переменной.
            var_value: значение переменной.
        """
        if pos < 0 or pos >= self.get_size():
            raise DPClientException(-1)
        cl_session_set_var(self.session_obj, pos, var_name, var_value)
        return

    def get_var(self, pos: int) -> Tuple[str, str]:
        """
        Получение имени и значения переменной по ее индексу (нумерация с нуля).
        Args:
            pos: индекс переменной.
        Returns:
            Кортеж, состоящий из двух строк - имени и значения переменной.
            Либо исплючение, если переменная не существует.
        """
        if pos < 0 or pos >= self.get_size():
            raise DPClientException(-1)
        ret_code, var_name, var_value = cl_session_get(self.session_obj, pos)
        if ret_code:
            raise DPClientException(ret_code)
        return var_name, var_value

    # Расширенные методы

    def get_vars(self) -> List[Tuple[str, str]]:
        """
        Получение всех переменных, содержащихся в сессии.
        Returns:
            Список кортежей, состоящих из двух строк -
            имени и значения переменной.
        """
        current_vars = list()
        size = self.get_size()
        for n in range(size):
            current_vars.append(self.get_var(n))
        return current_vars

    def append_var(self, var_name: str, var_value: str) -> None:
        """
        Добавить переменную в конец с расширением места, отведенного под
        переменные сессии.
        Args:
            var_name: имя переменной.
            var_value: значение переменной.
        """
        size = self.get_size()
        current_vars = self.get_vars()
        current_vars.append((var_name, var_value))
        self.resize(size+1)
        for n in range(size+1):
            self.set_var(n, current_vars[n][0], current_vars[n][1])
        return

    def pop(self, index: Optional[int] = None) -> Tuple[str, str]:
        """
        Удалить и вернуть переменную из сессии по ее индексу.
        Если не указан индекс - удаление и возврат происходит с конца.
        Args:
            index: индекс переменной сессии.
        Returns:
            Кортеж, состоящий из двух строк - имени и значения переменной.
        """
        size = self.get_size()
        index = index if index is not None else size-1
        if not size or index >= size:
            raise DPClientException(-1)
        current_vars = self.get_vars()
        var_name, var_value = current_vars.pop(index)
        self.resize(size-1)
        for n in range(size-1):
            self.set_var(n, current_vars[n][0], current_vars[n][1])
        return var_name, var_value
