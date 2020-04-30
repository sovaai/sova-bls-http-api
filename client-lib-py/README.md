# Обертка для библиотеки ClientLib

Модуль для питона, который раотает с Си-функциями из библиотеки ClientLib.  
Генерируемый в процессе сборки файл `*.so` представляет собой Python-обертку Си-функций.  
Пакет `dp_client` представляет собой более высокоуровниевую обертку над модулем `pydpclient`.

## Зависимости

CMake:
```bash
sudo apt install cmake
```
python3-dev:
```bash
sudo apt install python3-dev
```

## Сборка

Скачать библиотеку:

```bash
git submodule update --init
```

Запустить скрипт:

```bash
sudo ./rebuild.sh
```

Установить pytest (вместо Х - версия интерпретатора):
```bash
sudo python3.X -m pip install pytest
```

Проверить сборку (вместо Х - версия интерпретатора):

```bash
python3.X -m pytest -s dp_client/test.py --conn_str <cs>
```
где cs - connection string.  
Аргумент `--conn_str` не обязательный - если его не передавать, все тесты, 
свзанные с обращениями к серверу, будут пропущены.

Установка:

```bash
python3.X setup.py install
```

## Easy инструкция
```python
from dp_client.client import Client

SESSION_ID = 1
SESSION_CONTEXT = {
    "var_name": "var_value",
}
BOT_ID = 2
BOT_CONTEXT = {
    "inf_person": "demo",
    "inf_name": '',
}
CONN_STR = "tcp:localhost:2255"

# Создаем объект клиента
client = Client(connection_string=CONN_STR)
# Делаем запрос
ans = client.easy_request(
    request="Привет!",
    session_id=SESSION_ID,
    session_context=SESSION_CONTEXT,
    bot_id=BOT_ID,
    bot_context=BOT_CONTEXT,
)
```

## Пример использования пакета dp_client

```python
import dp_client

SESSION_ID = 1
INF_ID = 1

# Создем и инициализируем сессию
session = dp_client.session.Session()
session.set_id(SESSION_ID)
session.set_inf_id(INF_ID)

# Создаем и инициализируем инф
inf = dp_client.inf.Inf()
inf.set_id(INF_ID)
inf.append_var("inf_person", "demo")
inf.append_var("inf_name", '')

# Создаем клиента
client = dp_client.client.Client(
    connection_string="tcp:localhost:2255",
    session=session,
    inf=inf,
)

# Удаляем старые сессии и инф с сервера
client.purge_inf()
client.purge_session()

# Отправляем новые сессию и инф
client.send_session()
client.send_inf()

# Инициализируем соединение
missed_mask = client.initialize()

# Если потеряны данные, то переотправим
if not client.is_success(missed_mask):
    missed_mask = client.process_missed(missed_mask)

# Отправляем запрос
answer, missed_mask = client.request(request="привет, мир!")

# Разбираем ответ
print("Answer length: ", answer.get_size())
for i in range(answer.get_size()):
    print("Message #", i)
    print("\ttype: ", answer.get_type(i)[1])
    print("\tcontent: ", answer.process_message(i))
```

## Документация на низкоуровниевые фунции

Докстринг на модуль `pydpclient` доступен в аттрибуте `__doc__` модуля.  
Докстринг на каждую функцию модуля `pydpclient` в аттрибуте `__doc__` соответствующей функции.  
Докстринги на методы классов пакета `dp_client` написаны нативно.
---
Доступные группы функций:
- cl_cmd_ - методы для коммутации с сервером InfServer.
- cl_session_ - данные сессии и функции для работы с ней.
- cl_inf_ - данные инфа и функции для работы с ними.
- cl_answer_ - Ответ сервера на запрос REQUEST и функции для работы с ним.
Дополнительные функции:
- code_to_string - получение описания кода возврата.
- get_protocol_version - возвращает версию используемого протокола.
- get_allocated_memory_size - получение размера памяти, выделенной библиотекой для внутреннего использования.
---

### Группа cl_cmd

- cl_cmd_init:
```
cl_cmd_init( aInfId: int, aSessionId: int, aMissedDataMask: int, aConnectionString: str, aTimeOut: int, aPackDataFlag: int) -> int:
Запрос инициализации сервером сессии с идентификатором aSessionId для инфа aInfId.
aMissedDataMask - маска недостающих компонентов.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: код операции.
```
- cl_cmd_purge_session:
```
purge_session( aSessionId: int, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:
Удаление сессии с идентификатором aSessionId из кеша сервера.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: код операции.
```
- cl_cmd_send_session:
```
cl_cmd_send_session( SDptr: SessionDataPonterType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:
Обновление или добавление сессии в кэш сервера.
SDptr - данные сессии.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: код операции.
```
- cl_cmd_update_session:
```
cl_cmd_update_session( SDptr: SessionDataPonterType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:
Обновление значений переменных сессии в кэшэ сервера.
SDptr - данные сессии.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: код операции.
```
- cl_cmd_request:
```
cl_cmd_request( aSessionId: int, aInfId: int, aRequest: str, SDptr: SessionDataPonterType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> Tuple[int, AnswerPointerType]:
Запрос ответа сервера на запрос aRequest, относящийся к сессии с идентификатором aSessionId и инфу с идентификатором aInfId.
SDptr - данные сессии.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: (retcode, AnswerPointerType, aMissedDataMask), где retcode - код ответа, AnswerPointerType - объект ответа, aMissedDataMask - маска недостающих компонентов.
```
- cl_cmd_purge_inf:
```
cl_cmd_purge_inf( aInfId: int, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:
Удаление инфа из кэша бэкэнда.
aInfId - идентификатор инфа.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: код операции.
```
- cl_cmd_send_inf:
```
cl_cmd_send_inf( IDptr: InfDataPointerType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:
Обновление или добавление в кэш сервера данных инфа.
IDptr - данные инфа.
aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.
aTimeOut - значение таймаута в секундах.
aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.
Returns: код операции.
```

### Группа cl_session

- cl_session_create:
```
cl_session_create( ) -> SessionDataPonterType:
Создание данных сессии.
Returns: объект сессии SessionDataPonterType.
```
- cl_session_resize:
```
cl_session_resize( SDptr: SessionDataPonterType, aVarsNumber: int ) -> int:
Выделение памяти под переменные инфа. Все переменные, при этом действии, обнуляются.
SDptr - данные сессии.
aVarsNumber - количество переменных.
Returns: код операции.
```
- cl_session_set_var:
```
cl_session_set_var( SDptr: SessionDataPonterType, aVarInd: int, aVarName: str, aVarValue: str) -> None:
Установка имени и значения aVarInd-ой переменной.
SDptr - данные сессии.
VarInd - номер переменной.
aVarName - имя переменной.
aVarValue - значение переменной.
```
- cl_session_set_id:
```
cl_session_set_id( SDptr: SessionDataPonterType, aSessionId: int ) -> None:
Установка идентификатора сессии.
SDptr - данные сессии.
aSessionId - идентификатор сессии.
```
- cl_session_set_inf_id:
```
cl_session_set_inf_id( SDptr: SessionDataPonterType, aInfId: int ) -> None:
Установка идентификатор инфа, связанного с сессиией.
SDptr - данные сессии.
aInfId - идентификатор инфа.
```
- cl_session_get_size:
```
cl_session_get_size( SDptr: SessionDataPonterType ) -> int:
Получение числа переменных в сессии.
SDptr - данные сессии.
Returns: число переменных.
```
- cl_session_get:
```
cl_session_get( SDptr: SessionDataPonterType, aVarInd: int ) -> Tuple[int, str, str]:
Получение имени и значения aVarInd-ой переменной.
SDptr - данные сессии.
aVarInd - номер переменной.
Returns: (retCode, VarName, VarValue), где retCode - код операции, VarName - имя переменной, VarValue - значение переменной.
```
- cl_session_free:
```
cl_session_free( SDptr: SessionDataPonterType ) -> int:
Освобождение памяти выделенной под переменные сессии.
aSessionData - данные сессии.
Returns: код операции.
```

### Группа cl_inf

- cl_inf_create:
```
cl_inf_create( ) -> InfDataPointerType:
Создание профиля данных инфа.
Returns: объект инфа InfDataPointerType.
```
- cl_inf_resize:
```
cl_inf_resize( IDptr: InfDataPonterType, aVarsNumber: int, aDictsNumber: int) -> int:
Выделение памяти под переменные инфа. Все переменные, при этом действии, обнуляются.
IDptr - данные инфа.
aVarsNumber - количество переменных.
aDictsNumber - количество словарей.
Returns: код операции.
```
- cl_inf_set_var:
```
cl_inf_set_var( IDptr: InfDataPonterType, aVarInd: int, aVarName: str, aVarValue: str) -> None:
Установка имени и значения переменной с номером aVarInd.
IDptr - данные инфа.
aVarInd - номер переменной.
aVarName - имя переменной.
aVarValue - значение переменной.
```
- cl_inf_set_dict:
```
cl_inf_set_dict( IDptr: InfDataPonterType, aDictInd: int, aDictName: str, aDict: str) -> None:
Установка имени и тела словаря с номером aVarInd.
IDptr - данные инфа.
aDictInd - номер словаря.
aDictName - имя словаря.
aDict - тело стоваря.
```
- cl_inf_set_id:
```
cl_inf_set_id( IDptr: InfDataPonterType, aInfId: int ) -> None:
Установка идентификатора инфа.
IDptr - данные инфа.
aInfId - идентификатор инфа.
```
- cl_inf_set_templates:
```
cl_inf_set_templates( IDptr: InfDataPonterType, aTemplates: str ) -> None:
Установка шаблонов инфа.
IDptr - данные инфа.
aTemplates - шаблоны инфа.
```
- cl_inf_get_vars_cnt:
```
cl_inf_get_vars_cnt( IDptr: InfDataPonterType ) -> int:
Получение числа переменных в данных инфа.
IDptr - данные инфа.
Returns: число переменных.
```
- cl_inf_get_dicts_cnt:
```
cl_inf_get_dicts_cnt( IDptr: InfDataPonterType ) -> int:
Получение числа словарей в данных инфа.
IDptr - данные инфа.
Returns: число словарей.
```
- cl_inf_get_var:
```
cl_inf_get_var( IDptr: InfDataPonterType, aVarInd int ) -> Tuple[int, str, str]:
Получение имени и значения переменной с номером aVarInd.
IDptr - данные инфа.
aVarInd - номер переменной.
Returns: (retCode, VarName, VarValue), где retCode - код операции, VarName - имя переменной, VarValue - значение переменной.
```
- cl_inf_get_dict:
```
"cl_inf_get_dict( IDptr: InfDataPonterType, aDictInd: int ) -> Tuple[int, str, str]:
"Получение имени и тела словаря с номером aDictInd.
"IDptr - данные инфа.
"aDictInd - номер словаря.
"Returns: (retCode, VarName, VarValue), где retCode - код операции, DictName - имя словаря, DictValue - значение словаря.
```
- cl_inf_free:
```
cl_inf_free( IDptr: InfDataPonterType ) -> int:
Освобождение памяти.
IDptr - данные инфа.
Returns: код операции.
```

### Группа cl_answer

- cl_answer_free:
```
cl_answer_free( Aptr: AnswerPointerType ) -> int:
Освобождение памяти, занимаемой ответом сервера.
Aptr - данные ответа.
Returns: код операции.
```
- cl_answer_get_size:
```
cl_answer_get_size( Aptr: AnswerPointerType ) -> int:
Получение количества элементов в ответе сервера.
Aptr - данные ответа.
Returns: количество элементов.
```
- cl_answer_get_type:
```
cl_answer_get_type( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, int]:
Получение типа aItemInd-ого элемента ответа сервера.
	AnswerItemTypeTextString    = 1		Текстовая строка.
	AnswerItemTypeTagInf        = 2		Тэг inf, обозначающий кликабельный ответ инфу.
	AnswerItemTypeTagBr         = 3		Тэг br, обозначающий перенос строки.
	AnswerItemTypeTagHref       = 4		Тэг href, обозначающий ссылку.
	AnswerItemTypeInstruct      = 5		Инструкция на изменение сессии.
	AnswerItemTypeTagOpenWindow = 6		Тэг open_window, обозначающий команду открытия ссылки в окне браузера.
	AnswerItemTypeTagRSS        = 7		Тэг запроса RSS.
	AnswerItemTypeStartUList 	= 8		Начало ненумерованного форматированного списка.
	AnswerItemTypeStartOList	= 9		Начало нумерованного форматированного списка.
	AnswerItemTypeListItem  	= 10	Начало элемента форматированного списка.
	AnswerItemTypeEndList    	= 11	Конец форматированного списка.
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, answeritemtype), где retCode - код операции, answeritemtype - тип ответа.
```
- cl_answer_get_text:
```
cl_answer_get_text( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str]:
Получение данных aItemInd-ого элемента как текстовой строки.
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, answertext), где retCode - код операции, answertext - текст ответа.
```
- cl_answer_get_tag_inf:
```
cl_answer_get_tag_inf( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str]:
Получение данных aItemInd-ого элемента как тэга запроса к инфу( tag inf ).
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, aValue, aRequest), где retCode - код операции, aValue - текст ссылки, aRequest - запрос к серверу.
```
- cl_answer_get_tag_href:
```
cl_answer_get_tag_href( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str, str]:
Получение данных aItemInd-ого элемента как тэга ссылки ( tag href ).
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, aURL, aTarget, aLink), где retCode - код операции, aURL - URL, aTarget - target ссылки, aLink - текст ссылки.
```
- cl_answer_get_instruct:
```
cl_answer_get_instruct( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str]:
Получение данных aItemInd-ого элемента как инструкции к изменению сессии.
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, aVarName, aVarValue), где retCode - код операции, aVarName - имя переменной, aVarValue - значение переменной.
```
- cl_answer_get_tag_open_window:
```
cl_answer_get_tag_open_window( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, int]:
Получение данных aItemInd-ого элемента как тэга открытия ссылки в окне браузера.
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, aURL, aTarget), где retCode - код операции, aURL - URL, aTarget - идентификатор окна, в котором нужно открыть ссылку. ( New - 0; Parent - 1 ).
```
- cl_answer_get_tag_rss:
```
cl_answer_get_tag_rss( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str, int, int, int, int]:
Получение данных aItemInd-ого элемента как тэга запроса RSS.
Aptr - данные ответа.
aItemInd - номер элемента в ответе сервера.
Returns: (retCode, aURL, aAlt, aOffset, aShowTitle, aShowLink, aUpdatePeriod), где retCode - код операции, aURL - URL RSS'а,
aAlt - текст, показываемый при недоступности RSS, aOffset - номер RSS записи, aShowTitle - флаг показа заголовка RSS,
aShowLink - флаг показа ссылки на RSS, aUpdatePeriod - частота обновления RSS.
```

### Прочее

- code_to_string:
```
code_to_string( code: int ) -> str:
Получние описания кода возврата.
code - код возврата.
```
- get_protocol_version:
```
get_protocol_version( ) -> int:
Возвращает версию используемого протокола.
```
- get_allocated_memory_size:
```
get_allocated_memory_size( ) -> int:
Получение размера памяти, выделенной библиотекой для внутреннего использования.
```