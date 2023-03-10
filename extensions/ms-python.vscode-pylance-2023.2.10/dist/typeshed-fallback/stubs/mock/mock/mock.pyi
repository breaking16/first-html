from _typeshed import Self
from collections.abc import Callable, Coroutine, Mapping, Sequence
from contextlib import AbstractContextManager
from types import TracebackType
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Literal

_F = TypeVar("_F", bound=Callable[..., Any])
_AF = TypeVar("_AF", bound=Callable[..., Coroutine[Any, Any, Any]])
_T = TypeVar("_T")
_TT = TypeVar("_TT", bound=type[Any])
_R = TypeVar("_R")

__all__ = (
    "Mock",
    "MagicMock",
    "patch",
    "sentinel",
    "DEFAULT",
    "ANY",
    "call",
    "create_autospec",
    "AsyncMock",
    "FILTER_DIR",
    "NonCallableMock",
    "NonCallableMagicMock",
    "mock_open",
    "PropertyMock",
    "seal",
)

class InvalidSpecError(Exception): ...

FILTER_DIR: bool

class _SentinelObject:
    def __init__(self, name: str) -> None: ...
    name: str

class _Sentinel:
    def __getattr__(self, name: str) -> _SentinelObject: ...

sentinel: _Sentinel
DEFAULT: _SentinelObject

class _Call(tuple[Any, ...]):
    def __new__(
        cls: type[Self],
        value: Any = ...,
        name: Any | None = ...,
        parent: Any | None = ...,
        two: bool = ...,
        from_kall: bool = ...,
    ) -> Self: ...
    name: Any
    parent: Any
    from_kall: Any
    def __init__(
        self, value: Any = ..., name: Any | None = ..., parent: Any | None = ..., two: bool = ..., from_kall: bool = ...
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, __other: object) -> bool: ...
    def __call__(self, *args: Any, **kwargs: Any) -> _Call: ...
    def __getattr__(self, attr: str) -> Any: ...
    @property
    def args(self) -> tuple[Any, ...]: ...
    @property
    def kwargs(self) -> dict[str, Any]: ...
    def call_list(self) -> _CallList: ...

call: _Call

class _CallList(list[_Call]):
    def __contains__(self, value: Any) -> bool: ...

class Base:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class NonCallableMock(Base, Any):
    def __new__(
        cls: type[Self],
        spec: list[str] | object | type[object] | None = ...,
        wraps: Any | None = ...,
        name: str | None = ...,
        spec_set: list[str] | object | type[object] | None = ...,
        parent: NonCallableMock | None = ...,
        _spec_state: Any | None = ...,
        _new_name: str = ...,
        _new_parent: NonCallableMock | None = ...,
        _spec_as_instance: bool = ...,
        _eat_self: bool | None = ...,
        unsafe: bool = ...,
        **kwargs: Any,
    ) -> Self: ...
    def __init__(
        self,
        spec: list[str] | object | type[object] | None = ...,
        wraps: Any | None = ...,
        name: str | None = ...,
        spec_set: list[str] | object | type[object] | None = ...,
        parent: NonCallableMock | None = ...,
        _spec_state: Any | None = ...,
        _new_name: str = ...,
        _new_parent: NonCallableMock | None = ...,
        _spec_as_instance: bool = ...,
        _eat_self: bool | None = ...,
        unsafe: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    def _calls_repr(self, prefix: str = ...) -> str: ...
    def assert_called_with(_mock_self, *args: Any, **kwargs: Any) -> None: ...
    def assert_not_called(_mock_self) -> None: ...
    def assert_called_once_with(_mock_self, *args: Any, **kwargs: Any) -> None: ...
    def _format_mock_failure_message(self, args: Any, kwargs: Any, action: str = ...) -> str: ...
    def assert_called(_mock_self) -> None: ...
    def assert_called_once(_mock_self) -> None: ...
    def reset_mock(self, visited: Any = ..., *, return_value: bool = ..., side_effect: bool = ...) -> None: ...
    def _extract_mock_name(self) -> str: ...
    def assert_any_call(self, *args: Any, **kwargs: Any) -> None: ...
    def assert_has_calls(self, calls: Sequence[_Call], any_order: bool = ...) -> None: ...
    def mock_add_spec(self, spec: Any, spec_set: bool = ...) -> None: ...
    def _mock_add_spec(self, spec: Any, spec_set: bool, _spec_as_instance: bool = ..., _eat_self: bool = ...) -> None: ...
    def attach_mock(self, mock: NonCallableMock, attribute: str) -> None: ...
    def configure_mock(self, **kwargs: Any) -> None: ...
    return_value: Any
    side_effect: Any
    called: bool
    call_count: int
    call_args: Any
    call_args_list: _CallList
    mock_calls: _CallList
    def _format_mock_call_signature(self, args: Any, kwargs: Any) -> str: ...
    def _call_matcher(self, _call: tuple[_Call, ...]) -> _Call: ...
    def _get_child_mock(self, **kw: Any) -> NonCallableMock: ...

class CallableMixin(Base):
    side_effect: Any
    def __init__(
        self,
        spec: Any | None = ...,
        side_effect: Any | None = ...,
        return_value: Any = ...,
        wraps: Any | None = ...,
        name: Any | None = ...,
        spec_set: Any | None = ...,
        parent: Any | None = ...,
        _spec_state: Any | None = ...,
        _new_name: Any = ...,
        _new_parent: Any | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def __call__(_mock_self, *args: Any, **kwargs: Any) -> Any: ...

class Mock(CallableMixin, NonCallableMock): ...

class _patch(Generic[_T]):
    attribute_name: Any
    getter: Callable[[], Any]
    attribute: str
    new: _T
    new_callable: Any
    spec: Any
    create: bool
    has_local: Any
    spec_set: Any
    autospec: Any
    kwargs: Mapping[str, Any]
    additional_patchers: Any
    def __init__(
        self: _patch[_T],
        getter: Callable[[], Any],
        attribute: str,
        new: _T,
        spec: Any | None,
        create: bool,
        spec_set: Any | None,
        autospec: Any | None,
        new_callable: Any | None,
        kwargs: Mapping[str, Any],
        *,
        unsafe: bool = ...,
    ) -> None: ...
    def copy(self) -> _patch[_T]: ...
    def __call__(self, func: Callable[..., _R]) -> Callable[..., _R]: ...
    def decorate_class(self, klass: _TT) -> _TT: ...
    def decorate_callable(self, func: _F) -> _F: ...
    def decorate_async_callable(self, func: _AF) -> _AF: ...
    def decoration_helper(
        self, patched: Any, args: tuple[Any, ...], keywargs: dict[str, Any]
    ) -> AbstractContextManager[tuple[tuple[Any, ...], dict[str, Any]]]: ...
    def get_original(self) -> tuple[Any, bool]: ...
    target: Any
    temp_original: Any
    is_local: bool
    def __enter__(self) -> _T: ...
    def __exit__(
        self, __exc_type: type[BaseException] | None, __exc_value: BaseException | None, __traceback: TracebackType | None
    ) -> None: ...
    def start(self) -> _T: ...
    def stop(self) -> None: ...

class _patch_dict:
    in_dict: Any
    values: Any
    clear: Any
    def __init__(self, in_dict: Any, values: Any = ..., clear: Any = ..., **kwargs: Any) -> None: ...
    def __call__(self, f: Any) -> Any: ...
    def decorate_callable(self, f: _F) -> _F: ...
    def decorate_async_callable(self, f: _AF) -> _AF: ...
    def decorate_class(self, klass: Any) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, *args: object) -> Any: ...
    start: Any
    stop: Any

class _patcher:
    TEST_PREFIX: str
    dict: type[_patch_dict]
    @overload
    def __call__(  # type: ignore[misc]
        self,
        target: Any,
        *,
        spec: Any | None = ...,
        create: bool = ...,
        spec_set: Any | None = ...,
        autospec: Any | None = ...,
        new_callable: Any | None = ...,
        unsafe: bool = ...,
        **kwargs: Any,
    ) -> _patch[MagicMock | AsyncMock]: ...
    # This overload also covers the case, where new==DEFAULT. In this case, the return type is _patch[Any].
    # Ideally we'd be able to add an overload for it so that the return type is _patch[MagicMock],
    # but that's impossible with the current type system.
    @overload
    def __call__(
        self,
        target: Any,
        new: _T,
        spec: Any | None = ...,
        create: bool = ...,
        spec_set: Any | None = ...,
        autospec: Any | None = ...,
        new_callable: Any | None = ...,
        *,
        unsafe: bool = ...,
        **kwargs: Any,
    ) -> _patch[_T]: ...
    @overload
    def object(  # type: ignore[misc]
        self,
        target: Any,
        attribute: str,
        *,
        spec: Any | None = ...,
        create: bool = ...,
        spec_set: Any | None = ...,
        autospec: Any | None = ...,
        new_callable: Any | None = ...,
        unsafe: bool = ...,
        **kwargs: Any,
    ) -> _patch[MagicMock | AsyncMock]: ...
    @overload
    def object(
        self,
        target: Any,
        attribute: str,
        new: _T,
        spec: Any | None = ...,
        create: bool = ...,
        spec_set: Any | None = ...,
        autospec: Any | None = ...,
        new_callable: Any | None = ...,
        *,
        unsafe: bool = ...,
        **kwargs: Any,
    ) -> _patch[_T]: ...
    def multiple(
        self,
        target: Any,
        spec: Any | None = ...,
        create: bool = ...,
        spec_set: Any | None = ...,
        autospec: Any | None = ...,
        new_callable: Any | None = ...,
        *,
        unsafe: bool = ...,
        **kwargs: _T,
    ) -> _patch[_T]: ...
    def stopall(self) -> None: ...

patch: _patcher

class MagicMixin:
    def __init__(self, *args: Any, **kw: Any) -> None: ...

class NonCallableMagicMock(MagicMixin, NonCallableMock):
    def mock_add_spec(self, spec: Any, spec_set: bool = ...) -> None: ...

class MagicMock(MagicMixin, Mock):
    def mock_add_spec(self, spec: Any, spec_set: bool = ...) -> None: ...

class AsyncMockMixin(Base):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def assert_awaited(_mock_self) -> None: ...
    def assert_awaited_once(_mock_self) -> None: ...
    def assert_awaited_with(_mock_self, *args: Any, **kwargs: Any) -> None: ...
    def assert_awaited_once_with(_mock_self, *args: Any, **kwargs: Any) -> None: ...
    def assert_any_await(_mock_self, *args: Any, **kwargs: Any) -> None: ...
    def assert_has_awaits(_mock_self, calls: _CallList, any_order: bool = ...) -> None: ...
    def assert_not_awaited(_mock_self) -> None: ...
    def reset_mock(self, *args: Any, **kwargs: Any) -> None: ...
    await_count: int
    await_args: _Call | None
    await_args_list: _CallList
    __name__: str
    __defaults__: tuple[Any, ...]
    __kwdefaults__: dict[str, Any]
    __annotations__: dict[str, Any] | None  # type: ignore[assignment]

class AsyncMagicMixin(MagicMixin): ...
class AsyncMock(AsyncMockMixin, AsyncMagicMixin, Mock): ...

class MagicProxy(Base):
    name: str
    parent: Any
    def __init__(self, name: str, parent: Any) -> None: ...
    def create_mock(self) -> Any: ...
    def __get__(self, obj: Any, _type: Any | None = ...) -> Any: ...

class _ANY:
    def __eq__(self, other: object) -> Literal[True]: ...
    def __ne__(self, other: object) -> Literal[False]: ...

ANY: Any

def create_autospec(
    spec: Any,
    spec_set: Any = ...,
    instance: Any = ...,
    _parent: Any | None = ...,
    _name: Any | None = ...,
    *,
    unsafe: bool = ...,
    **kwargs: Any,
) -> Any: ...

class _SpecState:
    spec: Any
    ids: Any
    spec_set: Any
    parent: Any
    instance: Any
    name: Any
    def __init__(
        self,
        spec: Any,
        spec_set: Any = ...,
        parent: Any | None = ...,
        name: Any | None = ...,
        ids: Any | None = ...,
        instance: Any = ...,
    ) -> None: ...

def mock_open(mock: Any | None = ..., read_data: Any = ...) -> Any: ...

class PropertyMock(Mock):
    def __get__(self: Self, obj: _T, obj_type: type[_T] | None = ...) -> Self: ...
    def __set__(self, obj: Any, value: Any) -> None: ...

def seal(mock: Any) -> None: ...
