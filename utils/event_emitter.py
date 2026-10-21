"""
Publish-Subscribe asynchronous event emitter implementation.
"""
from collections import defaultdict

class EventEmitter:
    def __init__(self): self._events = defaultdict(list)
    def on(self, event: str, callback): self._events[event].append(callback)
    def off(self, event: str, callback):
        if callback in self._events[event]: self._events[event].remove(callback)
    def emit(self, event: str, *args, **kwargs):
        for cb in self._events[event]: cb(*args, **kwargs)
