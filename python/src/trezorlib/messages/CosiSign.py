# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CosiSign(p.MessageType):
    MESSAGE_WIRE_TYPE = 73

    def __init__(
        self,
        *,
        address_n: Optional[List[int]] = None,
        data: Optional[bytes] = None,
        global_commitment: Optional[bytes] = None,
        global_pubkey: Optional[bytes] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.data = data
        self.global_commitment = global_commitment
        self.global_pubkey = global_pubkey

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('data', p.BytesType, None),
            3: ('global_commitment', p.BytesType, None),
            4: ('global_pubkey', p.BytesType, None),
        }