from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from papi import Papi


class PapiErrorMixin:
    papi: "Papi"

    def __init__(self, *args, papi: "Papi"):
        self.papi = papi
        super().__init__(*args)


class DuplicateNode(PapiErrorMixin, ValueError):
    pass


class MissingObject(PapiErrorMixin, ValueError):
    pass
