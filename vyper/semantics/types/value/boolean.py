from typing import Union

from vyper import ast as vy_ast
from vyper.abi_types import ABI_Bool, ABIType
from vyper.exceptions import InvalidLiteral

from ..bases import BasePrimitive, BaseTypeDefinition, ValueTypeDefinition


class BoolT(SimpleGettableT):
    _id = "bool"
    _as_array = True
    _valid_literal = (vy_ast.NameConstant,)


    def validate_boolean_op(self, node: vy_ast.BoolOp) -> None:
        return

    def validate_numeric_op(
        self, node: Union[vy_ast.UnaryOp, vy_ast.BinOp, vy_ast.AugAssign]
    ) -> None:
        if isinstance(node.op, vy_ast.Not):
            return
        super().validate_numeric_op(node)

    @property
    def abi_type(self) -> ABIType:
        return ABI_Bool()

    def validate_literal(cls, node: vy_ast.Constant) -> None:
        super().validate_literal(node)
        if node.value is None:
            raise InvalidLiteral("Invalid literal for type 'bool'", node)
