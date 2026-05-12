# src/simlab/ids.py


class Identifier:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
        self.current_id = 0

    def new_id(self) -> str:
        self.current_id += 1
        return f"{self.prefix}_{self.current_id}"
    
class IdentifierRegistry:
    def __init__(self) -> None:
        self.registry: dict[str, Identifier] = {}
        self.used_prefixes: set[str] = set()

    def register_identifier(self, namespace: str, prefix: str | None = None) -> Identifier:
        """
        Register a new identifier to a namespace and an optional prefix.
        If no prefix is set, the namespace will be used as prefix.
        """
        if namespace is None or namespace == "":
            raise ValueError(f"You must supply a namespace name.")
        
        if namespace in self.registry:
            raise ValueError(f"Identifier namespace already occupied.")

        if prefix is None or prefix == '':
            prefix = namespace

        if prefix in self.used_prefixes:
            raise ValueError(f"Identifier prefix already occupied: {prefix}")
        
        identifier = Identifier(prefix)

        self.registry[namespace] = identifier
        self.used_prefixes.add(prefix)

        return self.registry[namespace]
    
    def new_id(self, namespace: str) -> str:
        if not namespace in self.registry:
            raise ValueError(f"Could not find namespace {namespace}")
        
        identifier = self.registry.get(namespace)
        if identifier is None:
            raise ValueError("Couldnt create id for namespace {namespace}")
        
        return identifier.new_id()
        

        