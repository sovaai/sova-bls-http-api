#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
#include <stddef.h>
#include "ClientLib/ClientLib.h"

/******************************* Работа со структурой SessionData **************************************/

// Структура, которая будет хранить указатель на  структуру SessionData.
typedef struct SessionDataPointer {
    PyObject_HEAD
    SessionData *pointer;
} SessionDataPointerType;

// Освобождение структуры
static void SessionData_dealloc(SessionDataPointerType* self) {
    //Py_TYPE(self)->tp_free((PyObject*)self);
    PyTypeObject *tp = Py_TYPE(self);
    // free references and buffers here
    tp->tp_free(self);
    Py_DECREF(tp);
}

// Создание структуры
static PyObject * SessionData_new(PyTypeObject *type) {//, PyObject *args, PyObject *kwds) {
    SessionDataPointerType *self;
    self = (SessionDataPointerType *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->pointer = NULL;
    }
    return (PyObject *)self;
}

// Инициализация структуры, заполняем её переданными значениями
static int SessionData_init(SessionDataPointerType *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"pointer", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|i", kwlist, &self->pointer))
        return -1;
    return 0;
}

// Описываем аттрибуты из которых состоит структура
static PyMemberDef SessionData_members[] = {
    {"pointer", T_INT, offsetof(SessionDataPointerType, pointer), 0, "int"},
    {NULL},
};

// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject SessionDataPointer_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pydpclient.SessionDataPointer",            /* tp_name */
    sizeof(SessionDataPointerType),             /* tp_basicsize */
    0,                                          /* tp_itemsize */
    (destructor) SessionData_dealloc,           /* tp_dealloc */
    0,                                          /* tp_print */
    0,                                          /* tp_getattr */
    0,                                          /* tp_setattr */
    0,                                          /* tp_reserved */
    0,                                          /* tp_repr */
    0,                                          /* tp_as_number */
    0,                                          /* tp_as_sequence */
    0,                                          /* tp_as_mapping */
    0,                                          /* tp_hash  */
    0,                                          /* tp_call */
    0,                                          /* tp_str */
    0,                                          /* tp_getattro */
    0,                                          /* tp_setattro */
    0,                                          /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "SessionDataPointerType objects",           /* tp_doc */
    0,                                          /* tp_traverse */
    0,                                          /* tp_clear */
    0,                                          /* tp_richcompare */
    0,                                          /* tp_weaklistoffset */
    0,                                          /* tp_iter */
    0,                                          /* tp_iternext */
    0,                                          /* tp_methods */
    SessionData_members,                        /* tp_members */
    0,                                          /* tp_getset */
    0,                                          /* tp_base */
    0,                                          /* tp_dict */
    0,                                          /* tp_descr_get */
    0,                                          /* tp_descr_set */
    0,                                          /* tp_dictoffset */
    (initproc) SessionData_init,                /* tp_init */
    0,                                          /* tp_alloc */
    (newfunc) SessionData_new,                  /* tp_new */
};

/********************************* Работа со структурой InfData *****************************************/

// Структура, которая будет хранить указатель на  структуру InfData.
typedef struct InfDataPointer {
    PyObject_HEAD
    InfData *pointer;
} InfDataPointerType;

// Освобождение структуры
static void InfData_dealloc(InfDataPointerType* self) {
    //Py_TYPE(self)->tp_free((PyObject*)self);
    PyTypeObject *tp = Py_TYPE(self);
    // free references and buffers here
    tp->tp_free(self);
    Py_DECREF(tp);
}

// Создание структуры
static PyObject * InfData_new(PyTypeObject *type) {//, PyObject *args, PyObject *kwds) {
    InfDataPointerType *self;
    self = (InfDataPointerType *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->pointer = NULL;
    }
    return (PyObject *)self;
}

// Инициализация структуры, заполняем её переданными значениями
static int InfData_init(InfDataPointerType *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"pointer", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|i", kwlist, &self->pointer))
        return -1;
    return 0;
}

// Описываем аттрибуты из которых состоит структура
static PyMemberDef InfData_members[] = {
    {"pointer", T_INT, offsetof(InfDataPointerType, pointer), 0, "int"},
    {NULL},
};

// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject InfDataPointer_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pydpclient.InfDataPointer",                /* tp_name */
    sizeof(InfDataPointerType),                 /* tp_basicsize */
    0,                                          /* tp_itemsize */
    (destructor) InfData_dealloc,               /* tp_dealloc */
    0,                                          /* tp_print */
    0,                                          /* tp_getattr */
    0,                                          /* tp_setattr */
    0,                                          /* tp_reserved */
    0,                                          /* tp_repr */
    0,                                          /* tp_as_number */
    0,                                          /* tp_as_sequence */
    0,                                          /* tp_as_mapping */
    0,                                          /* tp_hash  */
    0,                                          /* tp_call */
    0,                                          /* tp_str */
    0,                                          /* tp_getattro */
    0,                                          /* tp_setattro */
    0,                                          /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "InfDataPointerType objects",               /* tp_doc */
    0,                                          /* tp_traverse */
    0,                                          /* tp_clear */
    0,                                          /* tp_richcompare */
    0,                                          /* tp_weaklistoffset */
    0,                                          /* tp_iter */
    0,                                          /* tp_iternext */
    0,                                          /* tp_methods */
    InfData_members,                            /* tp_members */
    0,                                          /* tp_getset */
    0,                                          /* tp_base */
    0,                                          /* tp_dict */
    0,                                          /* tp_descr_get */
    0,                                          /* tp_descr_set */
    0,                                          /* tp_dictoffset */
    (initproc) InfData_init,                    /* tp_init */
    0,                                          /* tp_alloc */
    (newfunc) InfData_new,                      /* tp_new */
};

/************************* Работа со структурами Answer ***************************************/

// Структура, которая будет хранить указатель на  структуру Answer.
typedef struct AnswerPointer {
    PyObject_HEAD
    Answer *pointer;
} AnswerPointerType;

// Освобождение структуры
static void Answer_dealloc(AnswerPointerType* self) {
    //Py_TYPE(self)->tp_free((PyObject*)self);
    PyTypeObject *tp = Py_TYPE(self);
    // free references and buffers here
    tp->tp_free(self);
    Py_DECREF(tp);
}

// Создание структуры
static PyObject * Answer_new(PyTypeObject *type) {//, PyObject *args, PyObject *kwds) {
    AnswerPointerType *self;
    self = (AnswerPointerType*)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->pointer = NULL;
    }
    return (PyObject *)self;
}

// Инициализация структуры, заполняем её переданными значениями
static int Answer_init(AnswerPointerType *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"pointer", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|i", kwlist, &self->pointer))
        return -1;
    return 0;
}

// Описываем аттрибуты из которых состоит структура
static PyMemberDef Answer_members[] = {
    {"pointer", T_INT, offsetof(AnswerPointerType, pointer), 0, "int"},
    {NULL},
};

// Структура описывающая нашу структуру. Какие атрибуты, методы, конструкторы, деструкторы и т.д. и т.п.
PyTypeObject AnswerPointer_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "pydpclient.AnswerPointer",                 /* tp_name */
    sizeof(AnswerPointerType),                  /* tp_basicsize */
    0,                                          /* tp_itemsize */
    (destructor) Answer_dealloc,                /* tp_dealloc */
    0,                                          /* tp_print */
    0,                                          /* tp_getattr */
    0,                                          /* tp_setattr */
    0,                                          /* tp_reserved */
    0,                                          /* tp_repr */
    0,                                          /* tp_as_number */
    0,                                          /* tp_as_sequence */
    0,                                          /* tp_as_mapping */
    0,                                          /* tp_hash  */
    0,                                          /* tp_call */
    0,                                          /* tp_str */
    0,                                          /* tp_getattro */
    0,                                          /* tp_setattro */
    0,                                          /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,   /* tp_flags */
    "AnswerPointerType objects",                /* tp_doc */
    0,                                          /* tp_traverse */
    0,                                          /* tp_clear */
    0,                                          /* tp_richcompare */
    0,                                          /* tp_weaklistoffset */
    0,                                          /* tp_iter */
    0,                                          /* tp_iternext */
    0,                                          /* tp_methods */
    Answer_members,                             /* tp_members */
    0,                                          /* tp_getset */
    0,                                          /* tp_base */
    0,                                          /* tp_dict */
    0,                                          /* tp_descr_get */
    0,                                          /* tp_descr_set */
    0,                                          /* tp_dictoffset */
    (initproc) Answer_init,                     /* tp_init */
    0,                                          /* tp_alloc */
    (newfunc) Answer_new,                       /* tp_new */
};

/******************** Коды возврата функций и функции для их интерпретации **********************/

static PyObject* pydpclient_CodeToString(PyObject *self, PyObject *args) {
    int code;
    if (!PyArg_ParseTuple(args, "i", &code))
        return NULL;
    if (code > 0)
        return Py_BuildValue("s", "");
    ClientLibReturnCode retCode = code;
    const char *code_description = ClientLibReturnCodeToString(retCode);
    return Py_BuildValue("s", code_description);
}

static PyObject* pydpclient_GetProtocolVersion(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    unsigned int proto_version = GetProtocolVersion();
    return Py_BuildValue("i", proto_version);
}

static PyObject* pydpclient_GetAllocatedMemorySize(PyObject *self, PyObject *args) {
    if (!PyArg_ParseTuple(args, ""))
        return NULL;
    unsigned int memory_size = GetClientLibAllocatedMemorySize();
    return Py_BuildValue("i", memory_size);
}

/************************ Методы для коммутации с сервером InfServer ****************************/

static PyObject* pydpclient_cl_cmd_init(PyObject *self, PyObject *args) {
    unsigned int aInfId, aSessionId, aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString;
    if (!PyArg_ParseTuple(args, "iisii", &aInfId, &aSessionId, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    unsigned int aMissedDataMask;
    ClientLibReturnCode retCode = cl_cmd_init(aInfId, aSessionId, &aMissedDataMask, aConnectionString, aTimeOut, aPackDataFlag);
    return Py_BuildValue("ii", retCode, aMissedDataMask);
}

static PyObject* pydpclient_cl_cmd_purge_session(PyObject *self, PyObject *args) {
    unsigned int aSessionId, aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString;
    if (!PyArg_ParseTuple(args, "isii", &aSessionId, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    ClientLibReturnCode retCode = cl_cmd_purge_session(aSessionId, aConnectionString, aTimeOut, aPackDataFlag);
    return Py_BuildValue("i", retCode);
}

static PyObject* pydpclient_cl_cmd_send_session(PyObject *self, PyObject *args) {
    unsigned int aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString;
    SessionDataPointerType *SDptr;
    if (!PyArg_ParseTuple(args, "Osii", &SDptr, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    SessionData *sdata = SDptr->pointer;
    ClientLibReturnCode retCode = cl_cmd_send_session(sdata, aConnectionString, aTimeOut, aPackDataFlag);
    return Py_BuildValue("i", retCode);
}

static PyObject* pydpclient_cl_cmd_update_session(PyObject *self, PyObject *args) {
    unsigned int aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString;
    SessionDataPointerType *SDptr;
    if (!PyArg_ParseTuple(args, "Osii", &SDptr, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    SessionData *sdata = SDptr->pointer;
    ClientLibReturnCode retCode = cl_cmd_update_session(sdata, aConnectionString, aTimeOut, aPackDataFlag);
    return Py_BuildValue("i", retCode);
}

static PyObject* pydpclient_cl_cmd_request(PyObject *self, PyObject *args) {
    unsigned int aSessionId, aInfId, aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString, *aRequest;
    SessionDataPointerType *SDptr;
    if (!PyArg_ParseTuple(args, "iisOsii", &aSessionId, &aInfId, &aRequest, &SDptr, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    SessionData *sdata = SDptr->pointer;
    Answer *adata = (Answer*)malloc(sizeof(adata)); // TODO утечка
    unsigned int aMissedDataMask;
    ClientLibReturnCode retCode = cl_cmd_request(aSessionId, aInfId, aRequest, sdata, &aMissedDataMask, &adata, aConnectionString, aTimeOut, aPackDataFlag);
    AnswerPointerType *new_answer = (AnswerPointerType*) Answer_new(&AnswerPointer_Type);
    new_answer->pointer = adata;
    return Py_BuildValue("iOi", retCode, new_answer, aMissedDataMask);
}

static PyObject* pydpclient_cl_cmd_purge_inf(PyObject *self, PyObject *args) {
    unsigned int aInfId, aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString;
    if (!PyArg_ParseTuple(args, "isii", &aInfId, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    ClientLibReturnCode retCode = cl_cmd_purge_inf(aInfId, aConnectionString, aTimeOut, aPackDataFlag);
    return Py_BuildValue("i", retCode);
}

static PyObject* pydpclient_cl_cmd_send_inf(PyObject *self, PyObject *args) {
    unsigned int aTimeOut;
    int aPackDataFlag;
    const char *aConnectionString;
    InfDataPointerType *IDptr;
    if (!PyArg_ParseTuple(args, "Osii", &IDptr, &aConnectionString, &aTimeOut, &aPackDataFlag))
        return NULL;
    InfData *infdata = IDptr->pointer;
    ClientLibReturnCode retCode = cl_cmd_send_inf(infdata, aConnectionString, aTimeOut, aPackDataFlag);
    return Py_BuildValue("i", retCode);
}

/*************************** Данные сессии и функции для работы с ней ********************************/

static PyObject* pydpclient_cl_session_create(PyObject *self, PyObject *args) {
    SessionData *new_session = cl_session_create();
    SessionDataPointerType *new_session_pointer = (SessionDataPointerType*) SessionData_new(&SessionDataPointer_Type);
    new_session_pointer->pointer = new_session;
    return Py_BuildValue("O", new_session_pointer);
}

static PyObject* pydpclient_cl_session_resize(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    unsigned int aVarsNumber;
    if (!PyArg_ParseTuple(args, "Oi", &SDptr, &aVarsNumber))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    ClientLibReturnCode retCode = cl_session_resize(sessiondata, aVarsNumber);
    return Py_BuildValue("i", retCode);
}

static PyObject* pydpclient_cl_session_set_var(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    unsigned int aVarInd;
    const char* aVarName;
    const char* aVarValue;
    if (!PyArg_ParseTuple(args, "Oiss", &SDptr, &aVarInd, &aVarName, &aVarValue))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    char *new_aVarName = (char*)malloc(strlen(aVarName)+1); // TODO потенциальная утечка при изменении переменной
    strcpy(new_aVarName, aVarName);
    char *new_aVarValue = (char*)malloc(strlen(aVarValue)+1); // TODO потенциальная утечка при изменении переменной
    strcpy(new_aVarValue, aVarValue);
    cl_session_set_var(sessiondata, aVarInd, new_aVarName, new_aVarValue);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_session_set_id(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    unsigned int aSessionId;
    if (!PyArg_ParseTuple(args, "Oi", &SDptr, &aSessionId))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    cl_session_set_id(sessiondata, aSessionId);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_session_set_inf_id(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    unsigned int aInfId;
    if (!PyArg_ParseTuple(args, "Oi", &SDptr, &aInfId))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    cl_session_set_inf_id(sessiondata, aInfId);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_session_get_size(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    if (!PyArg_ParseTuple(args, "O", &SDptr))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    unsigned int size = cl_session_get_size(sessiondata);
    return Py_BuildValue("i", size);
}

static PyObject* pydpclient_cl_session_get(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    unsigned int aVarInd;
    if (!PyArg_ParseTuple(args, "Oi", &SDptr, &aVarInd))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    const char *aVarName;
    const char *aVarValue;
    ClientLibReturnCode retCode = cl_session_get(sessiondata, aVarInd, &aVarName, &aVarValue);
    return Py_BuildValue("iss", retCode, aVarName, aVarValue);
}

static PyObject* pydpclient_cl_session_free(PyObject *self, PyObject *args) {
    SessionDataPointerType *SDptr;
    if (!PyArg_ParseTuple(args, "O", &SDptr))
        return NULL;
    SessionData *sessiondata = SDptr->pointer;
    cl_session_free(sessiondata);
    return Py_BuildValue("i", 0);
}

/************************ Данные инфа и функции для работы с ними. ***********************************/

static PyObject* pydpclient_cl_inf_create(PyObject *self, PyObject *args) {
    InfData *new_inf = cl_inf_create();
    InfDataPointerType *new_inf_pointer = (InfDataPointerType*) InfData_new(&InfDataPointer_Type);
    new_inf_pointer->pointer = new_inf;
    return Py_BuildValue("O", new_inf_pointer);
}

static PyObject* pydpclient_cl_inf_resize(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    unsigned int aVarsNumber, aDictsNumber;
    if (!PyArg_ParseTuple(args, "Oii", &IDptr, &aVarsNumber, &aDictsNumber))
        return NULL;
    InfData *infdata = IDptr->pointer;
    ClientLibReturnCode retcode = cl_inf_resize(infdata, aVarsNumber, aDictsNumber);
    return Py_BuildValue("i", retcode);  
}

static PyObject* pydpclient_cl_inf_set_var(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    unsigned int aVarInd;
    const char *aVarName;
    const char *aVarValue;
    if (!PyArg_ParseTuple(args, "Oiss", &IDptr, &aVarInd, &aVarName, &aVarValue))
        return NULL;
    InfData *infdata = IDptr->pointer;
    char *new_aVarName = (char*)malloc(strlen(aVarName)+1); // TODO потенциальная утечка при изменении переменной
    strcpy(new_aVarName, aVarName);
    char *new_aVarValue = (char*)malloc(strlen(aVarValue)+1); // TODO потенциальная утечка при изменении переменной
    strcpy(new_aVarValue, aVarValue);
    cl_inf_set_var(infdata, aVarInd, new_aVarName, new_aVarValue);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_inf_set_dict(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    unsigned int aDictInd;
    const char *aDictName;
    const char *aDict;
    if (!PyArg_ParseTuple(args, "Oiss", &IDptr, &aDictInd, &aDictName, &aDict))
        return NULL;
    InfData *infdata = IDptr->pointer;
    char *new_aDictName = (char*)malloc(strlen(aDictName)+1); // TODO потенциальная утечка при изменении переменной
    strcpy(new_aDictName, aDictName);
    char *new_aDict = (char*)malloc(strlen(aDict)+1); // TODO потенциальная утечка при изменении переменной
    strcpy(new_aDict, aDict);
    cl_inf_set_dict(infdata, aDictInd, new_aDictName, new_aDict);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_inf_set_id(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    unsigned int aInfInd;
    if (!PyArg_ParseTuple(args, "Oi", &IDptr, &aInfInd))
        return NULL;
    InfData *infdata = IDptr->pointer;
    cl_inf_set_id(infdata, aInfInd);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_inf_set_templates(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    const char *aTemplates;
    if (!PyArg_ParseTuple(args, "Os", &IDptr, &aTemplates))
        return NULL;
    InfData *infdata = IDptr->pointer;
    cl_inf_set_templates(infdata, aTemplates);
    return Py_BuildValue("");
}

static PyObject* pydpclient_cl_inf_get_vars_cnt(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    if (!PyArg_ParseTuple(args, "O", &IDptr))
        return NULL;
    InfData *infdata = IDptr->pointer;
    unsigned int size = cl_inf_get_vars_cnt(infdata);
    return Py_BuildValue("i", size);
}

static PyObject* pydpclient_cl_inf_get_dicts_cnt(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    if (!PyArg_ParseTuple(args, "O", &IDptr))
        return NULL;
    InfData *infdata = IDptr->pointer;
    unsigned int size = cl_inf_get_dicts_cnt(infdata);
    return Py_BuildValue("i", size);
}

static PyObject* pydpclient_cl_inf_get_var(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    unsigned int aVarInd;
    if (!PyArg_ParseTuple(args, "Oi", &IDptr, &aVarInd))
        return NULL;
    InfData *infdata = IDptr->pointer;
    const char *aVarName;
    const char *aVarValue;
    ClientLibReturnCode retCode = cl_inf_get_var(infdata, aVarInd, &aVarName, &aVarValue);
    return Py_BuildValue("iss", retCode, aVarName, aVarValue);
}

static PyObject* pydpclient_cl_inf_get_dict(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    unsigned int aDictInd;
    if (!PyArg_ParseTuple(args, "Oi", &IDptr, &aDictInd))
        return NULL;
    InfData *infdata = IDptr->pointer;
    const char *aDictName;
    const char *aDicText;
    ClientLibReturnCode retCode = cl_inf_get_dict(infdata, aDictInd, &aDictName, &aDicText);
    return Py_BuildValue("iss", retCode, aDictName, aDicText);
}

static PyObject* pydpclient_cl_inf_free(PyObject *self, PyObject *args) {
    InfDataPointerType *IDptr;
    if (!PyArg_ParseTuple(args, "O", &IDptr))
        return NULL;
    InfData *infdata = IDptr->pointer;
    cl_inf_free(infdata);
    return Py_BuildValue("i", 0);
}

/**************** Ответ сервера на запрос REQUEST и функции для работы с ним *************************/

static PyObject* pydpclient_cl_answer_free(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    if (!PyArg_ParseTuple(args, "O", &Aptr))
        return NULL;
    Answer *answer = Aptr->pointer;
    cl_answer_free(answer);
    return Py_BuildValue("i", 0);
}

static PyObject* pydpclient_cl_answer_get_size(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    if (!PyArg_ParseTuple(args, "O", &Aptr))
        return NULL;
    Answer *answer = Aptr->pointer;
    unsigned int size = cl_answer_get_size(answer);
    return Py_BuildValue("i", size);
}

static PyObject* pydpclient_cl_answer_get_type(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    AnswerItemType answeritemtype;
    ClientLibReturnCode retcode = cl_answer_get_type(answer, aItemInd, &answeritemtype);
    return Py_BuildValue("ii", retcode, answeritemtype);
}

static PyObject* pydpclient_cl_answer_get_text(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    const char *answer_string;
    unsigned int answer_length;
    ClientLibReturnCode retcode = cl_answer_get_text(answer, aItemInd, &answer_string, &answer_length);
    return Py_BuildValue("is", retcode, answer_string); // TODO не возвращаю длину строки
}

static PyObject* pydpclient_cl_answer_get_tag_inf(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    const char *aValue; // Текст ссылки
    const char *aRequest; // Запрос к движку
    unsigned int aValueLength, aRequestLength;
    ClientLibReturnCode retcode = cl_answer_get_tag_inf(answer, aItemInd, &aValue, &aValueLength, &aRequest, &aRequestLength);
    return Py_BuildValue("iss", retcode, aValue, aRequest); // TODO не возвращаю длины строк
}

static PyObject* pydpclient_cl_answer_get_tag_href(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    const char *aURL; // URL
    const char *aTarget; // Target ссылки
    const char *aLink; // Текст ссылки
    unsigned int aURLLength, aTargetLength, aLinkLength;
    ClientLibReturnCode retcode = cl_answer_get_tag_href(answer, aItemInd, &aURL, &aURLLength, &aTarget, &aTargetLength, &aLink, &aLinkLength);
    return Py_BuildValue("isss", retcode, aURL, aTarget, aLink); // TODO не возвращаю длины строк
}

static PyObject* pydpclient_cl_answer_get_instruct(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    const char *aVarName; // имя переменной
    const char *aVarValue; // значение переменной
    unsigned int aVarNameLength, aVarValueLength;
    ClientLibReturnCode retcode = cl_answer_get_instruct(answer, aItemInd, &aVarName, &aVarNameLength, &aVarValue, &aVarValueLength);
    return Py_BuildValue("iss", retcode, aVarName, aVarValue); // TODO не возвращаю длины строк
}

static PyObject* pydpclient_cl_answer_get_tag_open_window(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    const char *aURL; // URL
    unsigned int aURLLength, aTarget;
    ClientLibReturnCode retcode = cl_answer_get_tag_open_window(answer, aItemInd, &aURL, &aURLLength, &aTarget);
    return Py_BuildValue("isi", retcode, aURL, aTarget); // TODO не возвращаю длины строк
}

static PyObject* pydpclient_cl_answer_get_tag_rss(PyObject *self, PyObject *args) {
    AnswerPointerType *Aptr;
    unsigned int aItemInd;
    if (!PyArg_ParseTuple(args, "Oi", &Aptr, &aItemInd))
        return NULL;
    Answer *answer = Aptr->pointer;
    const char *aURL; // URL
    unsigned int aURLLength; // Длина URL
    const char *aAlt; // Текст, показываемый при недоступности RSS
    unsigned int aAltLength; // длина текста, показываемого при недоступности RSS
    unsigned int aOffset, aShowTitle, aShowLink, aUpdatePeriod;
    ClientLibReturnCode retcode = cl_answer_get_tag_rss(answer, aItemInd, &aURL, &aURLLength, &aAlt, &aAltLength, &aOffset, &aShowTitle, &aShowLink, &aUpdatePeriod);
    return Py_BuildValue("issiiii", retcode, aURL, aAlt, aOffset, aShowTitle, aShowLink, aUpdatePeriod); // TODO не возвращаю длины строк
}

/************************************ Сборка модуля **************************************************/

// Биндинг методов (с докстрингами)
static PyMethodDef pydpclient_Methods[] = {
    // Коды возврата функций и функции для их интерпретации
    {"code_to_string",                  pydpclient_CodeToString,                    METH_VARARGS,
            "code_to_string( code: int ) -> str:\n"
            "Получние описания кода возврата.\n"
            "code - код возврата\n"
    },
    {"get_protocol_version",            pydpclient_GetProtocolVersion,              METH_VARARGS,
            "get_protocol_version( ) -> int:\n"
            "Возвращает версию используемого протокола.\n"
    },
    {"get_allocated_memory_size",       pydpclient_GetAllocatedMemorySize,          METH_VARARGS,
            "get_allocated_memory_size( ) -> int:\n"
            "Получение размера памяти, выделенной библиотекой для внутреннего использования.\n"
    },
    // Методы для коммутации с сервером InfServer
    {"cl_cmd_init",                     pydpclient_cl_cmd_init,                     METH_VARARGS,
            "cl_cmd_init( aInfId: int, aSessionId: int, aConnectionString: str, aTimeOut: int, aPackDataFlag: int) -> Tuple[int, int]:\n"
            "Запрос инициализации сервером сессии с идентификатором aSessionId для инфа aInfId.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: Кортеж из двух элементов - кода операции и aMissedDataMask - маски недостающих компонентов.\n"
    },
    {"cl_cmd_purge_session",            pydpclient_cl_cmd_purge_session,            METH_VARARGS,
            "purge_session( aSessionId: int, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:\n"
            "Удаление сессии с идентификатором aSessionId из кеша сервера.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: код операции.\n"
    },
    {"cl_cmd_send_session",             pydpclient_cl_cmd_send_session,             METH_VARARGS,
            "cl_cmd_send_session( SDptr: SessionDataPonterType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:\n"
            "Обновление или добавление сессии в кэш сервера.\n"
            "SDptr - данные сессии.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: код операции.\n"
    },
    {"cl_cmd_update_session",           pydpclient_cl_cmd_update_session,           METH_VARARGS,
            "cl_cmd_update_session( SDptr: SessionDataPonterType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:\n"
            "Обновление значений переменных сессии в кэшэ сервера.\n"
            "SDptr - данные сессии.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: код операции.\n"
    },
    {"cl_cmd_request",                  pydpclient_cl_cmd_request,                  METH_VARARGS,
            "cl_cmd_request( aSessionId: int, aInfId: int, aRequest: str, SDptr: SessionDataPonterType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> Tuple[int, AnswerPointerType, int]:\n"
            "Запрос ответа сервера на запрос aRequest, относящийся к сессии с идентификатором aSessionId и инфу с идентификатором aInfId.\n"
            "SDptr - данные сессии.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: (retcode, AnswerPointerType, aMissedDataMask), где retcode - код ответа, AnswerPointerType - объект ответа, aMissedDataMask - маска недостающих компонентов.\n"
    },
    {"cl_cmd_purge_inf",                pydpclient_cl_cmd_purge_inf,                METH_VARARGS,
            "cl_cmd_purge_inf( aInfId: int, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:\n"
            "Удаление инфа из кэша бэкэнда.\n"
            "aInfId - идентификатор инфа.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: код операции.\n"
    },
    {"cl_cmd_send_inf",                 pydpclient_cl_cmd_send_inf,                 METH_VARARGS,
            "cl_cmd_send_inf( IDptr: InfDataPointerType, aConnectionString: str, aTimeOut: int, aPackDataFlag: int ) -> int:\n"
            "Обновление или добавление в кэш сервера данных инфа.\n"
            "IDptr - данные инфа.\n"
            "aConnectionString - строка соединения. Формат строки соединения: tcp:host:2255 или unix:socket.\n"
            "aTimeOut - значение таймаута в секундах.\n"
            "aPackDataFlag - флаг, упаковки данных при пересылке между клиентом и сервером InfServer.\n"
            "Returns: код операции.\n"
    },
    // Данные сессии и функции для работы с ней
    {"cl_session_create",               pydpclient_cl_session_create,               METH_VARARGS,
            "cl_session_create( ) -> SessionDataPonterType:\n"
            "Создание данных сессии.\n"
            "Returns: объект сессии SessionDataPonterType.\n"
    },
    {"cl_session_resize",               pydpclient_cl_session_resize,               METH_VARARGS,
            "cl_session_resize( SDptr: SessionDataPonterType, aVarsNumber: int ) -> int:\n"
            "Выделение памяти под переменные инфа. Все переменные, при этом действии, обнуляются.\n"
            "SDptr - данные сессии.\n"
            "aVarsNumber - количество переменных.\n"
            "Returns: код операции.\n"
    },
    {"cl_session_set_var",              pydpclient_cl_session_set_var,              METH_VARARGS,
            "cl_session_set_var( SDptr: SessionDataPonterType, aVarInd: int, aVarName: str, aVarValue: str) -> None:\n"
            "Установка имени и значения aVarInd-ой переменной.\n"
            "SDptr - данные сессии.\n"
            "VarInd - номер переменной.\n"
            "aVarName - имя переменной.\n"
            "aVarValue - значение переменной.\n"
    },
    {"cl_session_set_id",               pydpclient_cl_session_set_id,               METH_VARARGS,
            "cl_session_set_id( SDptr: SessionDataPonterType, aSessionId: int ) -> None:\n"
            "Установка идентификатора сессии.\n"
            "SDptr - данные сессии.\n"
            "aSessionId - идентификатор сессии.\n"
    },
    {"cl_session_set_inf_id",           pydpclient_cl_session_set_inf_id,           METH_VARARGS,
            "cl_session_set_inf_id( SDptr: SessionDataPonterType, aInfId: int ) -> None:\n"
            "Установка идентификатор инфа, связанного с сессиией.\n"
            "SDptr - данные сессии.\n"
            "aInfId - идентификатор инфа.\n"
    },
    {"cl_session_get_size",             pydpclient_cl_session_get_size,             METH_VARARGS,
            "cl_session_get_size( SDptr: SessionDataPonterType ) -> int:\n"
            "Получение числа переменных в сессии.\n"
            "SDptr - данные сессии.\n"
            "Returns: число переменных.\n"
    },
    {"cl_session_get",                  pydpclient_cl_session_get,                  METH_VARARGS,
            "cl_session_get( SDptr: SessionDataPonterType, aVarInd: int ) -> Tuple[int, str, str]:\n"
            "Получение имени и значения aVarInd-ой переменной.\n"
            "SDptr - данные сессии.\n"
            "aVarInd - номер переменной.\n"
            "Returns: (retCode, VarName, VarValue), где retCode - код операции, VarName - имя переменной, VarValue - значение переменной.\n"
    },
    {"cl_session_free",                 pydpclient_cl_session_free,                 METH_VARARGS,
            "cl_session_free( SDptr: SessionDataPonterType ) -> int:\n"
            "Освобождение памяти выделенной под переменные сессии.\n"
            "aSessionData - данные сессии.\n"
            "Returns: код операции.\n"
    },
    // Данные инфа и функции для работы с ними
    {"cl_inf_create",                   pydpclient_cl_inf_create,                   METH_VARARGS,
            "cl_inf_create( ) -> InfDataPointerType:\n"
            "Создание профиля данных инфа.\n"
            "Returns: объект инфа InfDataPointerType.\n"
    },
    {"cl_inf_resize",                   pydpclient_cl_inf_resize,                   METH_VARARGS,
            "cl_inf_resize( IDptr: InfDataPonterType, aVarsNumber: int, aDictsNumber: int) -> int:\n"
            "Выделение памяти под переменные инфа. Все переменные, при этом действии, обнуляются.\n"
            "IDptr - данные инфа.\n"
            "aVarsNumber - количество переменных.\n"
            "aDictsNumber - количество словарей.\n"
            "Returns: код операции.\n"
    },
    {"cl_inf_set_var",                  pydpclient_cl_inf_set_var,                  METH_VARARGS,
            "cl_inf_set_var( IDptr: InfDataPonterType, aVarInd: int, aVarName: str, aVarValue: str) -> None:\n"
            "Установка имени и значения переменной с номером aVarInd.\n"
            "IDptr - данные инфа.\n"
            "aVarInd - номер переменной.\n"
            "aVarName - имя переменной.\n"
            "aVarValue - значение переменной.\n"
    },
    {"cl_inf_set_dict",                 pydpclient_cl_inf_set_dict,                 METH_VARARGS,
            "cl_inf_set_dict( IDptr: InfDataPonterType, aDictInd: int, aDictName: str, aDict: str) -> None:\n"
            "Установка имени и тела словаря с номером aVarInd.\n"
            "IDptr - данные инфа.\n"
            "aDictInd - номер словаря.\n"
            "aDictName - имя словаря.\n"
            "aDict - тело стоваря.\n"
    },
    {"cl_inf_set_id",                   pydpclient_cl_inf_set_id,                   METH_VARARGS,
            "cl_inf_set_id( IDptr: InfDataPonterType, aInfId: int ) -> None:\n"
            "Установка идентификатора инфа.\n"
            "IDptr - данные инфа.\n"
            "aInfId - идентификатор инфа.\n"
    },
    {"cl_inf_set_templates",            pydpclient_cl_inf_set_templates,            METH_VARARGS,
            "cl_inf_set_templates( IDptr: InfDataPonterType, aTemplates: str ) -> None:\n"
            "Установка шаблонов инфа.\n"
            "IDptr - данные инфа.\n"
            "aTemplates - шаблоны инфа.\n"
    },
    {"cl_inf_get_vars_cnt",             pydpclient_cl_inf_get_vars_cnt,             METH_VARARGS,
            "cl_inf_get_vars_cnt( IDptr: InfDataPonterType ) -> int:\n"
            "Получение числа переменных в данных инфа.\n"
            "IDptr - данные инфа.\n"
            "Returns: число переменных.\n"
    },
    {"cl_inf_get_dicts_cnt",            pydpclient_cl_inf_get_dicts_cnt,            METH_VARARGS,
            "cl_inf_get_dicts_cnt( IDptr: InfDataPonterType ) -> int:\n"
            "Получение числа словарей в данных инфа.\n"
            "IDptr - данные инфа.\n"
            "Returns: число словарей.\n"
    },
    {"cl_inf_get_var",                  pydpclient_cl_inf_get_var,                  METH_VARARGS,
            "cl_inf_get_var( IDptr: InfDataPonterType, aVarInd int ) -> Tuple[int, str, str]:\n"
            "Получение имени и значения переменной с номером aVarInd.\n"
            "IDptr - данные инфа.\n"
            "aVarInd - номер переменной.\n"
            "Returns: (retCode, VarName, VarValue), где retCode - код операции, VarName - имя переменной, VarValue - значение переменной.\n"
    },
    {"cl_inf_get_dict",                 pydpclient_cl_inf_get_dict,                 METH_VARARGS,
            "cl_inf_get_dict( IDptr: InfDataPonterType, aDictInd: int ) -> Tuple[int, str, str]:\n"
            "Получение имени и тела словаря с номером aDictInd.\n"
            "IDptr - данные инфа.\n"
            "aDictInd - номер словаря.\n"
            "Returns: (retCode, VarName, VarValue), где retCode - код операции, DictName - имя словаря, DictValue - значение словаря.\n"
    },
    {"cl_inf_free",                     pydpclient_cl_inf_free,                     METH_VARARGS,
            "cl_inf_free( IDptr: InfDataPonterType ) -> int:\n"
            "Освобождение памяти.\n"
            "IDptr - данные инфа.\n"
            "Returns: код операции.\n"
    },
    // Ответ сервера на запрос REQUEST и функции для работы с ним
    {"cl_answer_free",                  pydpclient_cl_answer_free,                  METH_VARARGS,
            "cl_answer_free( Aptr: AnswerPointerType ) -> int:\n"
            "Освобождение памяти, занимаемой ответом сервера.\n"
            "Aptr - данные ответа.\n"
            "Returns: код операции.\n"
    },
    {"cl_answer_get_size",              pydpclient_cl_answer_get_size,              METH_VARARGS,
            "cl_answer_get_size( Aptr: AnswerPointerType ) -> int:\n"
            "Получение количества элементов в ответе сервера.\n"
            "Aptr - данные ответа.\n"
            "Returns: количество элементов.\n"
    },
    {"cl_answer_get_type",              pydpclient_cl_answer_get_type,              METH_VARARGS,
            "cl_answer_get_type( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, int]:\n"
            "Получение типа aItemInd-ого элемента ответа сервера.\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, answeritemtype), где retCode - код операции, answeritemtype - тип ответа.\n"
    },
    {"cl_answer_get_text",              pydpclient_cl_answer_get_text,              METH_VARARGS,
            "cl_answer_get_text( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str]:\n"
            "Получение данных aItemInd-ого элемента как текстовой строки.\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, answertext), где retCode - код операции, answertext - текст ответа.\n"
    },
    {"cl_answer_get_tag_inf",           pydpclient_cl_answer_get_tag_inf,           METH_VARARGS,
            "cl_answer_get_tag_inf( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str]:\n"
            "Получение данных aItemInd-ого элемента как тэга запроса к инфу( tag inf ).\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, aValue, aRequest), где retCode - код операции, aValue - текст ссылки, aRequest - запрос к серверу.\n"
    },
    {"cl_answer_get_tag_href",          pydpclient_cl_answer_get_tag_href,          METH_VARARGS,
            "cl_answer_get_tag_href( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str, str]:\n"
            "Получение данных aItemInd-ого элемента как тэга ссылки ( tag href ).\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, aURL, aTarget, aLink), где retCode - код операции, aURL - URL, aTarget - target ссылки, aLink - текст ссылки.\n"
    },
    {"cl_answer_get_instruct",          pydpclient_cl_answer_get_instruct,          METH_VARARGS,
            "cl_answer_get_instruct( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str]:\n"
            "Получение данных aItemInd-ого элемента как инструкции к изменению сессии.\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, aVarName, aVarValue), где retCode - код операции, aVarName - имя переменной, aVarValue - значение переменной.\n"
    },
    {"cl_answer_get_tag_open_window",   pydpclient_cl_answer_get_tag_open_window,   METH_VARARGS,
            "cl_answer_get_tag_open_window( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, int]:\n"
            "Получение данных aItemInd-ого элемента как тэга открытия ссылки в окне браузера.\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, aURL, aTarget), где retCode - код операции, aURL - URL, aTarget - идентификатор окна, в котором нужно открыть ссылку. ( New - 0; Parent - 1 ).\n"
    },
    {"cl_answer_get_tag_rss",           pydpclient_cl_answer_get_tag_rss,           METH_VARARGS,
            "cl_answer_get_tag_rss( Aptr: AnswerPointerType, aItemInd: int ) -> Tuple[int, str, str, int, int, int, int]:\n"
            "Получение данных aItemInd-ого элемента как тэга запроса RSS.\n"
            "Aptr - данные ответа.\n"
            "aItemInd - номер элемента в ответе сервера.\n"
            "Returns: (retCode, aURL, aAlt, aOffset, aShowTitle, aShowLink, aUpdatePeriod), где retCode - код операции, aURL - URL RSS'а, "
            "aAlt - текст, показываемый при недоступности RSS, aOffset - номер RSS записи, aShowTitle - флаг показа заголовка RSS, "
            "aShowLink - флаг показа ссылки на RSS, aUpdatePeriod - частота обновления RSS.\n"
    },
    {NULL, NULL, 0, NULL},
};

// Документация на методы
static char pydpclient_Docs[] = "Обертки для функций, объявленных в ClientLib.h.\n"
"Докстринги с аннотациями доступны в __doc__ для каждой функции.\n"
"Доступные группы функций:\n"
"\tcl_cmd_ - методы для коммутации с сервером InfServer.\n"
"\tcl_session_ - данные сессии и функции для работы с ней.\n"
"\tcl_inf_ - данные инфа и функции для работы с ними.\n"
"\tcl_answer_ - Ответ сервера на запрос REQUEST и функции для работы с ним.\n"
"Дополнительные функции:\n"
"\tcode_to_string - получение описания кода возврата.\n"
"\tget_protocol_version - возвращает версию используемого протокола.\n"
"\tget_allocated_memory_size - получение размера памяти, выделенной библиотекой для внутреннего использования.\n";

// Описание модуляы
static struct PyModuleDef pydpclient_Module = {
    PyModuleDef_HEAD_INIT,
    "pydpclient",       // Имя модуля
    pydpclient_Docs,    // Документация на модуль
    -1,                 // Модуль в глобальном пространстве имен
    pydpclient_Methods, // Список методов
};

// Создание и инициализация модуля
PyMODINIT_FUNC PyInit_pydpclient(void) {

    PyObject *mod = PyModule_Create(&pydpclient_Module);

    // Добавляем объект для хранения указателя на SessionData
    if (PyType_Ready(&SessionDataPointer_Type) < 0)
        return NULL;
    Py_INCREF(&SessionDataPointer_Type);
    PyModule_AddObject(mod, "SessionDataPointerType", (PyObject *) &SessionDataPointer_Type);

    // Добавляем объект для хранения указателя на InfData
    if (PyType_Ready(&InfDataPointer_Type) < 0)
        return NULL;
    Py_INCREF(&InfDataPointer_Type);
    PyModule_AddObject(mod, "InfDataPointerType", (PyObject *) &InfDataPointer_Type);

    // Добавляем объект для хранения указателя на Answer
    if (PyType_Ready(&AnswerPointer_Type) < 0)
        return NULL;
    Py_INCREF(&AnswerPointer_Type);
    PyModule_AddObject(mod, "AnswerPointerType", (PyObject *) &AnswerPointer_Type);

    return mod;
}