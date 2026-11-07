from ai_service import extract_current_role
from bls_service import get_compensation_intelligence

sample_text = """
Operations Manager
ABC Manufacturing
"""

role = extract_current_role(sample_text)

result = get_compensation_intelligence(
    role,
    "Massachusetts"
)

print(role)
print(result)