# Pluggable storage backends

class StorageBackend:
    def save_multipart(self, file, path_hint: str):
        raise NotImplementedError

    def get_signed_url(self, filename: str, mime: str, method: str = "PUT"):
        raise NotImplementedError

    def open_stream(self, key: str):
        raise NotImplementedError

    def resolve_path(self, key: str):
        raise NotImplementedError
