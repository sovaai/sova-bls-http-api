from typing import Tuple, Optional, List
from .exceptions import DPClientException
from pydpclient import InfDataPointerType, cl_inf_create, cl_inf_free,\
    cl_inf_set_id, cl_inf_set_templates, cl_inf_get_vars_cnt,\
    cl_inf_get_dicts_cnt, cl_inf_resize, cl_inf_set_var, cl_inf_set_dict,\
    cl_inf_get_var, cl_inf_get_dict


class Inf:
    """
    Класс для работы с объектами инфов (которые являются структурами в Си).
    Сами объекты типа InfDataPointerType являются указателями на структуры в Си.
    """

    inf_id = None

    def __init__(
            self,
            inf_obj: Optional[InfDataPointerType] = None,
            inf_id: Optional[int] = None,
            inf_context: Optional[dict] = None,
    ):
        """
        Инициализация объекта инфа. Си-структура будет создана,
        если не был передан объект типа InfDataPointerType.
        Args:
            inf_obj: объект-указатель на структуру InfData.
        """
        self.inf_obj = inf_obj if inf_obj is not None else cl_inf_create()
        if inf_id is not None:
            self.set_id(inf_id)
        if inf_context is not None:
            for key, value in inf_context.items():
                self.append_var(key, value)

    def __del__(self):
        """
        Высвобождение занятой объектом памяти (как объектом-указателем,
        так и самой стрктурой, расположенной по этому указателю).
        """
        ret_code = cl_inf_free(self.inf_obj)
        del self.inf_obj
        if ret_code:
            raise DPClientException(ret_code)

    # Базовые функции

    def set_id(self, inf_id: int) -> None:
        """
        Установка идентификтора инфа.
        Args:
            inf_id: идентификатор инфа.
        """
        if inf_id < 0:
            raise DPClientException(-1)
        self.inf_id = inf_id
        cl_inf_set_id(self.inf_obj, inf_id)
        return

    def get_id(self):
        """
        Получение идентификатора инфа.
        Returns:
            идентификатор инфа.
        """
        return self.inf_id

    def set_template(self, template: str) -> None:
        """
        Установка шаблона инфа.
        Args:
            template: шаблон инфа.
        """
        cl_inf_set_templates(self.inf_obj, template)
        return

    def get_vars_number(self) -> int:
        """
        Получение числа переменных инфа.
        Returns:
            число переменных инфа.
        """
        return cl_inf_get_vars_cnt(self.inf_obj)

    def get_dicts_number(self) -> int:
        """
        Получение числа словарей инфа.
        Returns:
            число словарей инфа.
        """
        return cl_inf_get_dicts_cnt(self.inf_obj)

    def resize(
            self,
            new_vars_cnt: Optional[int],
            new_dicts_cnt: Optional[int],
    ) -> None:
        """
        Изменение объема памяти, отведенного под переменные и словари инфа.
        Старые переменные и словари при этом стираются.
        Args:
            new_vars_cnt: новое число переменных инфа.
            new_dicts_cnt: новое число словарей инфа.
        """
        if new_vars_cnt is None:
            new_vars_cnt = self.get_vars_number()
        if new_dicts_cnt is None:
            new_dicts_cnt = self.get_dicts_number()
        if new_vars_cnt < 0 or new_dicts_cnt < 0:
            raise DPClientException(-1)
        ret_val = cl_inf_resize(self.inf_obj, new_vars_cnt, new_dicts_cnt)
        if ret_val:
            raise DPClientException(ret_val)
        return

    def set_var(self, pos: int, var_name: str, var_value: str) -> None:
        """
        Установить переменную инфа по ее индексу.
        Args:
            pos: индекс переменной.
            var_name: имя переменной.
            var_value: знаение переменной.
        """
        if pos < 0 or pos >= self.get_vars_number():
            raise DPClientException(-1)
        cl_inf_set_var(self.inf_obj, pos, var_name, var_value)
        return

    def set_dict(self, pos: int, dict_name: str, dict_value: str) -> None:
        """
        Установка словаря инфа по его индексу.
        Args:
            pos: индекс словаря.
            dict_name: имя словаря.
            dict_value: значение словаря.
        """
        if pos < 0 or pos >= self.get_dicts_number():
            raise DPClientException(-1)
        cl_inf_set_dict(self.inf_obj, pos, dict_name, dict_value)
        return

    def get_var(self, pos: int) -> Tuple[str, str]:
        """
        Получить имя и значение переменной по ее индексу.
        Args:
            pos: индекс переменной.
        Returns:
            кортеж из двух строк - имени и значения переменной.
        """
        if pos < 0 or pos >= self.get_vars_number():
            raise DPClientException(-1)
        ret_code, var_name, var_value = cl_inf_get_var(self.inf_obj, pos)
        if ret_code:
            raise DPClientException(ret_code)
        return var_name, var_value

    def get_dict(self, pos: int) -> Tuple[str, str]:
        """
        Получение словаря инфа по его индексу.
        Args:
            pos: индекс словаря инфа.
        Returns:
            кортеж из двух строк - имени и значения словаря.
        """
        if pos < 0:
            raise DPClientException(-1)
        ret_code, dict_name, dict_value = cl_inf_get_dict(self.inf_obj, pos)
        if ret_code:
            raise DPClientException(ret_code)
        return dict_name, dict_value

    # Расширенные методы

    def get_vars(self) -> List[Tuple[str, str]]:
        """
        Получене всех переменных инфа.
        Returns:
            список кортежей, состоящих из двух строк -
            имени и значения переменной.
        """
        vars_number = self.get_vars_number()
        current_variables = list()
        for n in range(vars_number):
            current_variables.append(self.get_var(n))
        return current_variables

    def get_dicts(self) -> List[Tuple[str, str]]:
        """
        Получение всех словарей инфа.
        Returns:
            список кортежей, состоящих из двух строк -
            имени и значения словаря.
        """
        dicts_number = self.get_dicts_number()
        current_dicts = list()
        for n in range(dicts_number):
            current_dicts.append(self.get_dict(n))
        return current_dicts

    def append_var(self, var_name: str, var_value: str) -> None:
        """
        Добавить новую переменную в конец. При этом старые переменные
        и словари перезапишутся, т.к. операция изменения места под словари
        и переменные удаляет их.
        Args:
            var_name: имя переменной.
            var_value: значение переменной.
        """
        size_vars = self.get_vars_number()
        size_dicts = self.get_dicts_number()
        current_vars = self.get_vars()
        current_vars.append((var_name, var_value))
        current_dicts = self.get_dicts()
        self.resize(size_vars+1, size_dicts)
        for n in range(size_vars+1):
            self.set_var(n, current_vars[n][0], current_vars[n][1])
        for n in range(size_dicts):
            self.set_dict(n, current_dicts[n][0], current_dicts[n][1])
        return

    def append_dict(self, dict_name: str, dict_value: str) -> None:
        """
        Добавить словарь в конец. Переменные и словари при этом перезапишутся,
        т.к. операция изменения места под переменные и словари удаляет их.
        Args:
            dict_name: имя словаря.
            dict_value: значение словаря.
        """
        size_dicts = self.get_dicts_number()
        size_vars = self.get_vars_number()
        current_dicts = self.get_dicts()
        current_dicts.append((dict_name, dict_value))
        current_vars = self.get_vars()
        self.resize(size_vars, size_dicts+1)
        for n in range(size_dicts+1):
            self.set_dict(n, current_dicts[n][0], current_dicts[n][1])
        for n in range(size_vars):
            self.set_var(n, current_vars[n][0], current_vars[n][1])
        return

    def pop_value(self, index: Optional[int] = None) -> Tuple[str, str]:
        """
        Удалить и вернуть переменную по ее индексу.
        Если индекс не указан, то вернется и удалится последняя переменная.
        Args:
            index: индекс переменной.
        Returns:
            кортеж из двух строк - имени и значения переменной.
        """
        size_vars = self.get_vars_number()
        index = index if index is not None else size_vars - 1
        if not size_vars or index >= size_vars or index < 0:
            raise DPClientException(-1)
        size_dicts = self.get_dicts_number()
        current_vars = self.get_vars()
        var_name, var_value = current_vars.pop(index)
        current_dicts = self.get_dicts()
        self.resize(size_vars-1, size_dicts)
        for n in range(size_vars-1):
            self.set_var(n, current_vars[n][0], current_vars[n][1])
        for n in range(size_dicts):
            self.set_dict(n, current_dicts[n][0], current_dicts[n][1])
        return var_name, var_value

    def pop_dict(self, index: Optional[int] = None) -> Tuple[str, str]:
        """
        Удалить и вернуть словарь инфа по его индексу.
        Если индекс не указан, то удалится и вернется последний элемент.
        Args:
            index: индекс словаря инфа.
        Returns:
            кортеж из двух строк - имени и значения словаря.
        """
        size_dicts = self.get_dicts_number()
        index = index if index is not None else size_dicts - 1
        if not size_dicts or index >= size_dicts or index < 0:
            raise DPClientException(-1)
        size_vars = self.get_vars_number()
        current_dicts = self.get_dicts()
        dict_name, dict_value = current_dicts.pop(index)
        current_vars = self.get_vars()
        self.resize(size_vars, size_dicts-1)
        for n in range(size_dicts-1):
            self.set_dict(n, current_dicts[n][0], current_dicts[n][1])
        for n in range(size_vars):
            self.set_var(n, current_vars[n][0], current_vars[n][1])
        return dict_name, dict_value
