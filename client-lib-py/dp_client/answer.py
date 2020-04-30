from typing import Tuple, Callable, Optional
from .exceptions import DPClientException
from pydpclient import AnswerPointerType, cl_answer_free, cl_answer_get_size,\
    cl_answer_get_type, cl_answer_get_text, cl_answer_get_tag_inf,\
    cl_answer_get_tag_href, cl_answer_get_instruct,\
    cl_answer_get_tag_open_window, cl_answer_get_tag_rss


class Answer:
    """
    Класс для работы с объектом ответа.
    Сам объект AnswerPointerType представляет собой указатель на
    Си-структуру Answer.
    """

    # Типы ответа и их описание
    _answer_types = {
        1:  (
            "AnswerItemTypeTextString",
            "Текстовая строка",
        ),
        2:  (
            "AnswerItemTypeTagInf",
            "Тэг inf, обозначающий кликабельный ответ инфу",
        ),
        3:  (
            "AnswerItemTypeTagBr",
            "Тэг br, обозначающий перенос строки",
        ),
        4:  (
            "AnswerItemTypeTagHref",
            "Тэг href, обозначающий ссылку",
        ),
        5:  (
            "AnswerItemTypeInstruct",
            "Инструкция на изменение сессии",
        ),
        6:  (
            "AnswerItemTypeTagOpenWindow",
            "Тэг open_window, обозначающий команду открытия "
            "ссылки в окне браузера",
        ),
        7:  (
            "AnswerItemTypeTagRSS",
            "Тэг запроса RSS",
        ),
        8:  (
            "AnswerItemTypeStartUList",
            "Начало ненумерованного форматированного списка",
        ),
        9:  (
            "AnswerItemTypeStartOList",
            "Начало нумерованного форматированного списка",
        ),
        10: (
            "AnswerItemTypeListItem",
            "Начало элемента форматированного списка",
        ),
        11: (
            "AnswerItemTypeEndList",
            "Конец форматированного списка",
        ),
    }

    def __init__(self, answer_obj: AnswerPointerType):
        """
        Инициализация объекта ответа.
        Обязательно передавать объект указатель, т.к. нет функционала
        для создния пустого ответа.
        Args:
            answer_obj: объект-указатель на структуру Answer.
        """
        self.answer_obj = answer_obj

    def __del__(self):
        """
        Высвобождение памяти, занятой объектом ответа и
        объектом-указателем на него.
        """
        ret_code = cl_answer_free(self.answer_obj)
        del self.answer_obj
        if ret_code:
            raise DPClientException(ret_code)

    # Базовые функции

    def get_size(self) -> int:
        """
        Получение числа сообщений в ответе.
        Returns:
            число сообщений в ответе.
        """
        return cl_answer_get_size(self.answer_obj)

    def get_type(self, message_num: int) -> Tuple[int, Tuple[str, str]]:
        """
        Получение типа соообщения в ответе по его индексу.
        Args:
            message_num: индекс сообщения ответа.
        Returns:
            кортеж, в котором первый элемент является целым числом - номер типа,
            а второй элемент представляет собой кортеж из двух строк -
            название типа в Си-коде и его русскоязычного описания.
        """
        ret_code, type_num = cl_answer_get_type(self.answer_obj, message_num)
        if ret_code:
            raise DPClientException(ret_code)
        return type_num, self._answer_types.get(type_num, ('', ''))

    def get_text(self, message_num: int) -> str:
        """
        Получение значения сообщения как текста.
        Args:
            message_num: индекс сообщения ответа.
        Returns:
            строковое представление сообщения
        """
        ret_code, text = cl_answer_get_text(self.answer_obj, message_num)
        if ret_code:
            raise DPClientException(ret_code)
        return text

    def get_tag_inf(self, message_num: int) -> Tuple[str, str]:
        """
        Получение данных сообщения как тэга запроса к инфу.
        Args:
            message_num: индекс сообщения в ответе.
        Returns:
            кортеж из двух строк - текста ссылки и текста запроса к серверу.
        """
        ret_code, a_value, a_request = cl_answer_get_tag_inf(
            self.answer_obj, message_num,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return a_value, a_request

    def get_tag_href(self, message_num: int) -> Tuple[str, str, str]:
        """
        Получение данных сообщения как тэга ссылки.
        Args:
            message_num: индекс сообщения в ответе.
        Returns:
            кортеж из трех строк - URL ссылки, Target ссылки и текст ссылки.
        """
        ret_code, url, target, link = cl_answer_get_tag_href(
            self.answer_obj, message_num,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return url, target, link

    def get_instruct(self, message_num: int) -> Tuple[str, str]:
        """
        Получение данных сообщения как инструкции по изменению сессии.
        Args:
            message_num: индекс сообщения в ответе.
        Returns:
            кортеж из двух строк - имени и значения переменной.
        """
        ret_code, v_name, v_value = cl_answer_get_instruct(
            self.answer_obj, message_num,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return v_name, v_value

    def get_tag_open_window(self, message_num: int) -> Tuple[str, str]:
        """
        Получение данных сообщения как тэга открытия ссылки в окне браузера.
        Args:
            message_num: индекс сообщеия в ответе.
        Returns:
            кортеж из двух строк - URL и идентификатор окна, в
            котором нужно открыть ссылку.
        """
        ret_code, url, target = cl_answer_get_tag_open_window(
            self.answer_obj, message_num,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return url, target

    def get_tag_rss(
            self,
            message_num: int,
    ) -> Tuple[str, str, int, int, int, int]:
        """
        Получение данных сообщения как тэга запроса RSS.
        Args:
            message_num: индекс сообщения в ответе.
        Returns:
            кортеж вида (retCode, aURL, aAlt, aOffset, aShowTitle, aShowLink,
            aUpdatePeriod), где retCode - код операции, aURL - URL RSS-а, aAlt -
            текст, показываемый при недоступности RSS, aOffset - номер RSS
            записи, aShowTitle - флаг показа заголовка RSS, aShowLink - флаг
            показа ссылки на RSS, aUpdatePeriod - частота обновления RSS.
        """
        ret_code, *others = cl_answer_get_tag_rss(self.answer_obj, message_num)
        if ret_code:
            raise DPClientException(ret_code)
        return others

    # Расширенные методы TODO надо что-то придумать другое

    def bindings(self, message_type: int) -> Callable:
        """
        Получения соответствующего обработчика сообщения в
        зависимости от его типа.
        Args:
            message_type: номер типа сообщения в ответе.
        Returns:
            функция-обработчик.
        """
        if message_type == 1:
            return self.get_text
        elif message_type == 2:
            return self.get_tag_inf
        elif message_type == 3:
            return lambda *_: tuple()
        elif message_type == 4:
            return self.get_tag_href
        elif message_type == 5:
            return self.get_instruct
        elif message_type == 6:
            return self.get_tag_open_window
        elif message_type == 7:
            return self.get_tag_rss
        elif message_type in (8, 9, 10, 11):
            return lambda *_: tuple()
        else:
            raise DPClientException(-1)

    def process_message(self, message_num) -> Optional[Tuple]:
        """
        Обработка сообщения по его индексу.
        Args:
            message_num: индекс сообщения.
        Returns:
            кортеж из элементов, которые вернет обработчик.
        """
        tp = self.get_type(message_num)
        handler = self.bindings(tp[0])
        if handler is None:
            return None
        others = handler(message_num)
        return others

    def process_all(self) -> tuple:
        """
        Обработка всех сообщений в ответе.
        Генерируются кортежи из данных, которые вернут обработчики.
        Yields:
            значения, которые вернут обработчики.
        """
        message_amount = self.get_size()
        for i in range(message_amount):
            data = self.process_message(i)
            yield data
        return
