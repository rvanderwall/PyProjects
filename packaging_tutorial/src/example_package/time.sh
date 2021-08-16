
python -m timeit \
    --setup 'from harmonic_mean import harmonic_mean' \
    --setup 'from random import randint' \
    --setup 'nums = [randint(1, 1_000_000) for _ in range(1_000_000)]' \
    'harmonic_mean(nums)'

