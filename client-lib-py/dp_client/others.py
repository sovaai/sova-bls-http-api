from pydpclient import get_protocol_version, get_allocated_memory_size,\
    code_to_string


def protocol_version() -> int:
    """
    Возвращает версию протокола.
    Returns:
        версия протокола.
    """
    return get_protocol_version()


def allocated_memory() -> int:
    """
    Возвращает размер памяти, аллоцированной под работу библиотеки.
    Returns:
        число байт занятой памяти.
    """
    return get_allocated_memory_size()


def return_code_string(ret_code: int) -> str:
    """
    Возвращает текстовое описание ошибки.
    Args:
        ret_code: код ошибки.
    Returns:
        текстовое описание ошибки.
    """
    if 0 < ret_code < -11:
        return ''
    return code_to_string(ret_code)
