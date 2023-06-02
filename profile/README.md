# profile

## cProfile

```sh
pdm run profile/c_profile.py
```

```sh
         44 function calls (9 primitive calls) in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     36/1    0.000    0.000    0.000    0.000 /Users/yifanwu/Projects/py-playground/profile/c_profile.py:6(fib)
        1    0.000    0.000    0.000    0.000 /Users/yifanwu/.pyenv/versions/3.9.9/lib/python3.9/pstats.py:107(__init__)
        1    0.000    0.000    0.000    0.000 /Users/yifanwu/.pyenv/versions/3.9.9/lib/python3.9/pstats.py:117(init)
        1    0.000    0.000    0.000    0.000 /Users/yifanwu/.pyenv/versions/3.9.9/lib/python3.9/pstats.py:136(load_stats)
        1    0.000    0.000    0.000    0.000 /Users/yifanwu/.pyenv/versions/3.9.9/lib/python3.9/cProfile.py:50(create_stats)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

```sh
pdm run python -m cProfile profile/fib.py
```

```sh
         29860706 function calls (4 primitive calls) in 3.240 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.240    3.240 fib.py:1(<module>)
29860703/1    3.240    0.000    3.240    3.240 fib.py:5(fib)
        1    0.000    0.000    3.240    3.240 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

dump the output

```sh
pdm run python -m cProfile -o profile/assets/fib.prof profile/fib.py
```

### viz with [SnakeViz](https://github.com/jiffyclub/snakeviz)

```sh
pdm run snakeviz profile/assets/fib.prof
```

![snakeviz](./assets/snakeviz.png)

### viz with [tuna](https://github.com/nschloe/tuna)

```sh
pdm run tuna profile/assets/fib.prof
```

![tuna](./assets/tuna.png)

## [line-profiler](https://github.com/pyutils/line_profiler)

```sh
pdm run kernprof -lv profile/lp_profile.py
```

```sh
Wrote profile results to lp_profile.py.lprof
Timer unit: 1e-06 s

Total time: 1.9e-05 s
File: profile/lp_profile.py
Function: fib at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @cache
     5                                           @profile
     6                                           def fib(x):
     7        29          1.0      0.0      5.3      if x < 2:
     8         2          1.0      0.5      5.3          return x
     9        29         17.0      0.6     89.5      return fib(x - 1) + fib(x - 2)
```

## [scalene](https://github.com/plasma-umass/scalene)

```sh
pdm run scalene --cli profile/fib.py
```

![scalene profile screenshot](./assets/scalene.png)

## [py-spy](https://github.com/benfred/py-spy)

```sh
sudo pdm run py-spy record --function --gil -o profile/assets/py-spy-profile.svg -- python profile/fib.py
```

![py-spy profile flamegraph](./assets/py-spy-profile.svg)
