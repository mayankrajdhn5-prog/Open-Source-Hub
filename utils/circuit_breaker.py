"""
Resilience Circuit Breaker pattern with half-open recovery timeouts.
"""
import time

class CircuitBreakerOpenException(Exception): pass

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: float = 30.0):
        self.threshold = failure_threshold
        self.timeout = recovery_timeout
        self.failures = 0
        self.state = "CLOSED"
        self.last_failure_time = 0
    def call(self, func, *args, **kwargs):
        now = time.time()
        if self.state == "OPEN":
            if now - self.last_failure_time > self.timeout:
                self.state = "HALF-OPEN"
            else: raise CircuitBreakerOpenException("Circuit is open")
        try:
            res = func(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"; self.failures = 0
            return res
        except Exception as e:
            self.failures += 1
            self.last_failure_time = now
            if self.failures >= self.threshold: self.state = "OPEN"
            raise e
