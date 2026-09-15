import numpy as np
import pytest

from decay import simulate


def test_simulate_starts_at_N0():
    result = simulate(N0=100, lam=0.1, seed=0)
    assert result[0] == 100


def test_simulate_negative_rate():
    with pytest.raises(ValueError):
        simulate(N0=100, lam=-0.1)


def test_simulate_average():
    N0 = 1000
    lam = 0.1
    dt = 0.05
    steps = 200

    results = []

    for seed in range(100):
        result = simulate(N0, lam, dt, steps, seed)
        results.append(result[-1])

    average = np.mean(results)
    expected = N0 * np.exp(-lam * dt * steps)

    assert average == pytest.approx(expected, rel=0.1)
