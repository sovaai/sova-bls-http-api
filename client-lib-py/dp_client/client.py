from typing import Tuple, Optional
from .exceptions import DPClientException
from .answer import Answer
from .session import Session
from .inf import Inf
from pydpclient import cl_cmd_init, cl_cmd_purge_session, cl_cmd_purge_inf, \
    cl_cmd_update_session, cl_cmd_send_session, cl_cmd_send_inf, cl_cmd_request
import re


class Client:
    """
    Класс для работы с сервером InfServer.
    """

    def __init__(
            self,
            connection_string: str = '',
            time_out: int = 1000,
            pack_data_flag: bool = True,
            session: Session = None,
            inf: Inf = None,
            answer: Answer = None,
    ):
        """
        Инициализация объекта.
        Args:
            connection_string: строка соединения. Формат строки соединения:
                tcp:host:2255 или unix:socket.
            time_out: значение таймаута в секундах.
            pack_data_flag: флаг упаковки данных при пересылке между
                клиентом и сервером InfServer.
        """
        self.session = session
        self.inf = inf
        self.connection_string = connection_string
        self.time_out = time_out
        self.pack_data_flag = pack_data_flag
        self.answer = answer

    def __del__(self):
        """
        Высвобождение памяти, занимаемой собственными объектами.
        """
        del self.session
        del self.inf
        del self.answer

    def initialize(
            self,
            session_id: Optional[int] = None,
            inf_id: Optional[int] = None,
    ) -> int:
        """
        Запрос инициализации сервером сессии с идентификатором session_id
        для инфа inf_id. Если идентификаторы не указаны - берутся айди
        связанных объектов.
        Args:
            session_id: идентификатор сессии.
            inf_id: идентификатор инфа.
        Returns:
            маска недостающих компонентов.
        """
        if session_id is None:
            session_id = self.session.get_id()
        if inf_id is None:
            inf_id = self.inf.get_id()
        ret_code, missed_data_mask = cl_cmd_init(
            inf_id, session_id,
            self.connection_string, self.time_out, self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return missed_data_mask

    def purge_session(self, session_id: Optional[int] = None) -> None:
        """
        Удаление сессии с идентификатором session_id из кеша сервера.
        Если идентификатор не указан - удаляется сессия с идентификатором
        связанной сессии.
        Args:
            session_id: идентификатор сессии.
        """
        if session_id is None:
            session_id = self.session.get_id()
        ret_code = cl_cmd_purge_session(
            session_id,
            self.connection_string,
            self.time_out,
            self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return

    def purge_inf(self, inf_id: Optional[int] = None) -> None:
        """
        Удаление инфа из кэша бэкэнда по его идентифитаору.
        Если идентификатор не указан - удаляется инф с идентификатором
        связанного инфа.
        Args:
            inf_id: идентификатор инфа.
        """
        if inf_id is None:
            inf_id = self.inf.get_id()
        ret_code = cl_cmd_purge_inf(
            inf_id, self.connection_string, self.time_out, self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return

    def send_session(self, session: Optional[Session] = None) -> None:
        """
        Обновление или добавление сессии в кэш сервера.
        Если сессия не указана, то отправляется связанная.
        Args:
            session: объект сессии.
        """
        if session is None:
            session = self.session
        ret_code = cl_cmd_send_session(
            session.session_obj,
            self.connection_string,
            self.time_out,
            self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return

    def update_session(self, session: Optional[Session] = None) -> None:
        """
        Обновление значений переменных сессии в кэшэ сервера.
        Если сессия не указана, то обновляется связанная сессия.
        Args:
            session: объект сессии.
        """
        if session is None:
            session = self.session
        ret_code = cl_cmd_update_session(
            session.session_obj,
            self.connection_string,
            self.time_out,
            self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return

    def send_inf(self, inf: Optional[Inf] = None) -> None:
        """
        Обновление или добавление в кэш сервера данных инфа.
        Если инф не передан, то отправляется связанный инф.
        Args:
            inf: объект инфа.
        """
        if inf is None:
            inf = self.inf
        ret_code = cl_cmd_send_inf(
            inf.inf_obj,
            self.connection_string,
            self.time_out,
            self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        return

    def request(
            self,
            session: Optional[Session] = None,
            request: str = '',
    ) -> Tuple[Answer, int]:
        """
        Запрос ответа сервера на запрос request, относящийся к сессии с
        идентификатором session_id и инфу с идентификатором inf_id.
        Если не указана сессия, то отправится связанная сессия.
        Args:
            session: объект сессии.
            request: запрос.
        Returns:
            кортеж из двух элементов - объекта ответа и маски потерянных данных.
        """
        if session is None:
            session = self.session
        ret_code, answer_obj, missed_data_mask = cl_cmd_request(
            session.get_id(), session.get_inf_id(),
            request, session.session_obj,
            self.connection_string, self.time_out, self.pack_data_flag,
        )
        if ret_code:
            raise DPClientException(ret_code)
        answer = Answer(answer_obj)
        return answer, missed_data_mask

    @staticmethod
    def is_success(missed_data_mask: int) -> bool:
        """
        Проверка на успешность передачи.
        Args:
            missed_data_mask: маска потерянных данных.
        Returns:
            True, если данные не потеряны, иначе False.
        """
        return not missed_data_mask

    @staticmethod
    def is_session_missed(missed_data_mask: int) -> bool:
        """
        Проверка на потерю данных сессии при передаче.
        Args:
            missed_data_mask: маска потерянных данных.
        Returns:
            True, если сессия потеряна, иначе False.
        """
        return bool(missed_data_mask & 0x02)

    @staticmethod
    def is_inf_missed(missed_data_mask: int) -> bool:
        """
        Проверка на потерю данных инфа при передаче.
        Args:
            missed_data_mask: маска потерянных данных.
        Returns:
            True, если данные инфа потеряны, иначе False.
        """
        return bool(missed_data_mask & 0x01)

    def process_missed(
            self,
            missed_data_mask: int,
            session_id: Optional[int] = None,
            inf_id: Optional[int] = None,
    ) -> int:
        """
        Переотправка потерянных данных до бесконечности, если потребуется.
        Если идентификаторы сессии или инфа не указаны, то берутся
        идентификаторы связанных объектов.
        Args:
            missed_data_mask: маска потерянных данных.
            session_id: идентификатор сессии.
            inf_id: идентификатор инфа.
        Returns:
            флаг потерянных данных.
        """
        if session_id is None:
            session_id = self.session.get_id()
        if inf_id is None:
            inf_id = self.inf.get_id()
        if self.is_session_missed(missed_data_mask):
            self.send_session(self.session)
        if self.is_inf_missed(missed_data_mask):
            self.send_inf(self.inf)
        return self.initialize(session_id, inf_id)

    @staticmethod
    def string_postprocessing(s: str) -> str:
        """
        Постобработка строки
        Args:
            s: исходня строка
        Returns:
            Результирующая строка
        """
        # Убираем лишние пробелы по краям
        s = s.strip()
        # Заменяем &#59 на ;
        s = s.replace("&#59", ';')
        # Убираем пробелы перед знаком пунктуации
        pat = r"\s+([,.!?;)]+)"
        s = re.sub(r"\s{2,}", " ", re.sub(pat, r"\1", s))
        # Убираем пробелы после (
        s = s.replace("( ", '(')
        # Убираем пробелы в кавычках
        pat = r'\"\s+([^"]+)\s+\"'
        s = re.sub(pat, r'"' + r'\1' + r'"', s)
        # Ставим пробел перед (
        s = re.sub(r"([^:=\s])(\()", r"\1 \2", s)
        # Ставим пробел перед смайликом
        s = re.sub(r"(\S?)([:=][(|)])", r"\1 \2", s)
        return s

    def process_answer(self, answer: Answer) -> dict:
        """
        Обрабатывает ответ и возвращает его в удобном виде.
        Args:
            answer: объект ответа.
        Returns:
            кортеж из двух элементов - строки текстового ответа и словаря-контекста.
        """
        result = {
            "text": '',
            "vars": dict(),
        }
        end_of_list = ''
        for i in range(answer.get_size()):
            msg_type = answer.get_type(i)[0]
            if msg_type == 1:       # Текст
                text = answer.get_text(i)
                result["text"] += ' ' + text
            elif msg_type == 2:     # Тег инфа
                value, request = answer.get_tag_inf(i)
                request_part = f' data-request="{request}"' if request else ''
                inf_tag = f'<userlink{request_part}>{value}</userlink>'
                result["text"] += ' ' + inf_tag
            elif msg_type == 3:     # Тег <br>
                br_tag = "<br/>"
                result["text"] += ' ' + br_tag
            elif msg_type == 4:     # Тег href
                url, target, link = answer.get_tag_href(i)
                target = target or "_blank"
                href = f'<a href="{url}" target="{target}">{link}</a>'
                href = href.replace("&amp;", '&')
                result["text"] += ' ' + href
            elif msg_type == 5:     # Инструкция по изменению сессии
                key, val = answer.get_instruct(i)
                result["vars"][key] = val
            # Тип 6 и 7 - не используются
            elif msg_type == 8:     # AnswerItemTypeStartUList
                start_of_ulist = "<ul><li>"
                end_of_list = "</ul>"
                result["text"] += ' ' + start_of_ulist
            elif msg_type == 9:     # AnswerItemTypeStartOList
                start_of_olist = "<ol><li>"
                end_of_list = "</ol>"
                result["text"] += ' ' + start_of_olist
            elif msg_type == 10:    # AnswerItemTypeListItem
                li_part = "</li><li>"
                result["text"] += ' ' + li_part
            elif msg_type == 11:    # AnswerItemTypeEndList
                list_ending = "</li>" + end_of_list
                result["text"] += ' ' + list_ending
        result["text"] = self.string_postprocessing(result["text"])
        return result

    def easy_request(
            self,
            request: str,
            session_id: int,
            session_context: dict,
            bot_id: int,
            bot_context: dict,
    ) -> dict:
        """
        Запрос данных с сервера.
        Args:
            request: текст запроса.
            session_id: идентификатор сессии.
            session_context: контекст сессии.
            bot_id: идентификатор бота.
            bot_context: контекст бота.
        Returns:
            кортеж из двух элементов - строки текстового ответа и словаря-контекста.
        """
        self.inf = Inf(inf_id=bot_id, inf_context=bot_context)
        self.session = Session(
            session_id=session_id,
            inf_id=bot_id,
            session_context=session_context,
        )
        answer, missed_mask = self.request(request=request)
        if not self.is_success(missed_mask):
            self.process_missed(missed_mask)
            answer, missed_mask = self.request(request=request)
        return self.process_answer(answer)

    def easy_update(
            self,
            session_id: int,
            bot_id: int,
            session_context: dict,
    ) -> None:
        """
        Обновление данных сессии на сервере.
        Args:
            session_id: идентификатор сессии.
            bot_id: идентификатор связанного с сессией инфа.
            session_context: контекст сессии.
        """
        self.session = Session(
            session_id=session_id,
            inf_id=bot_id,
            session_context=session_context,
        )
        self.update_session(self.session)
        return
