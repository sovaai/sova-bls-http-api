from .others import return_code_string


class DPClientException(Exception):
    """
    Класс-исключение.
    """

    def __init__(self, ret_code: int):
        """
        Определяет текстовое описание ислючения по его коду и форматирует
        соответствующее сообщение.
        Args:
            ret_code: т.н. "код возврата", который возвращет большинство
                Си-функций в результате своей работы.
        """
        error = return_code_string(ret_code)
        super().__init__(f"Error: {error}")
