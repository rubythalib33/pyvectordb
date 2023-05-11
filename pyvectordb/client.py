import socket
from typing import List, Optional, Union
import numpy as np


class VectorDBClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.sock = None
        self.connect()

    def connect(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def close(self) -> None:
        self.sock.close()

    def _send_request(self, request: str) -> str:
        self.sock.sendall(request.encode())
        response = self.sock.recv(1024).decode()
        return response

    def auth(self, username: str, password: str) -> None:
        request = f'AUTH {username} {password}\n'
        response = self._send_request(request)
        self.token = response.strip()

    def create(self, label: str, vector: Optional[Union[None, List[float], np.ndarray]]) -> None:
        vector_str = ''
        if vector is not None:
            if isinstance(vector, np.ndarray):
                vector = vector.tolist()
            vector_str = ' '.join(str(x) for x in vector)
        request = f'CREATE {self.token} {label} {vector_str}\n'
        self._send_request(request)

    def read(self, label: str) -> Optional[np.ndarray]:
        request = f'READ {self.token} {label}\n'
        response = self._send_request(request)
        if response.strip() == 'NOT_FOUND':
            return None
        return np.array([float(x) for x in response.strip().split()])

    def update(self, label: str, vector: List[float]) -> None:
        vector_str = ' '.join(str(x) for x in vector)
        request = f'UPDATE {self.token} {label} {vector_str}\n'
        self._send_request(request)

    def delete(self, label: str) -> None:
        request = f'DELETE {self.token} {label}\n'
        self._send_request(request)

    def search(self, vector: Optional[Union[None, List[float], np.ndarray]], threshold: float, top_k: int) -> List[str]:
        if vector is None:
            raise ValueError('vector must not be None')
        else:
            if isinstance(vector, np.ndarray):
                vector = vector.tolist()
            vector_str = ' '.join(str(x) for x in vector)
            request = f'SEARCH {self.token} {vector_str} {threshold} {top_k}\n'
        response = self._send_request(request)
        labels = response.strip().split()
        return labels

    def make_cluster(self, k:int) -> None:
        request = f'MAKE_CLUSTER {self.token} {k}\n'
        self._send_request(request)

    def search_cluster(self, vector: Optional[Union[None, List[float], np.ndarray]], threshold: float, top_k: int) -> List[str]:
        if vector is None:
            raise ValueError('vector must not be None')
        else:
            if isinstance(vector, np.ndarray):
                vector = vector.tolist()
            vector_str = ' '.join(str(x) for x in vector)
            request = f'SEARCH_CLUSTER {self.token} {vector_str} {threshold} {top_k}\n'
        response = self._send_request(request)
        labels = response.strip().split()
        return labels
