from fasthtml_extn.deploy import deploy_metacall_faas

# Initialize __all__ as an empty list
__all__ = []

deploy_metacall_faas(__all__)

print(f"Exported functions: {__all__}")
