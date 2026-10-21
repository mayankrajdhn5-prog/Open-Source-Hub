"""
Unit test suite for Circuit Breaker pattern.
"""
from utils.circuit_breaker import CircuitBreaker, CircuitBreakerOpenException

def test_breaker():
    cb = CircuitBreaker(failure_threshold=2, recovery_timeout=0.1)
    fail = lambda: (_ for _ in ()).throw(ValueError("err"))
    try: cb.call(fail)
    except: pass
    try: cb.call(fail)
    except: pass
    assert cb.state == "OPEN"
