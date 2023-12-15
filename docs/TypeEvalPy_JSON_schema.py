from typing import List, Optional

from pydantic import BaseModel


class TypeEvalPySchemaLocalVariable(BaseModel):
    file: str
    line_number: int
    col_offset: int
    type: List[str]
    variable: str


class TypeEvalPySchemaLocalVariableInsideFunction(BaseModel):
    file: str
    line_number: int
    col_offset: int
    type: List[str]
    function: str
    variable: str


class TypeEvalPySchemaParameter(BaseModel):
    file: str
    line_number: int
    col_offset: int
    type: List[str]
    function: str
    parameter: str


class TypeEvalPySchemaFunctionReturn(BaseModel):
    file: str
    line_number: int
    col_offset: int
    type: List[str]
    function: Optional[str] = None
