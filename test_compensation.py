from pprint import pprint
from bls_service import (
    get_compensation_intelligence
)

result = get_compensation_intelligence(
    "Operations Manager",
    "Massachusetts"
)

pprint(result)