# ticker
A Rust + Python example letting Python code call Rust code and set callbacks.
## Build

```
cargo build
```

## Run

```
python src/ticker.py
```

## Expected output
The hex values of storage address vary. The following successful run is in Ubuntu.

```
loading [...]
Ticker.tick 1
Ticker.tick 2
PTicker.set_callback callback: <function msg at 0x7fe0aec67280>, cb: <CFunctionType object at 0x7fe0ae5f8400>
ticker_set_callback 0x7fe0b0243010
Ticker.set_callback 0x7fe0b0243010
Ticker.tick 3
Ticker.tick 4
Alarm time at 4 ticks. Call 0x7fe0b0243010
Alert: 4 ticks!
Ticker.tick 5
Ticker.tick 6
Alarm time at 6 ticks. Call 0x7fe0b0243010
Alert: 6 ticks!
```

### Problem: It crashes on Mac Os with Conda!

The output is from `Python 3.7.8 | packaged by conda-forge | (default, Jul 31 2020, 02:37:09)`.

```
loading [...]
Ticker.tick 1
Ticker.tick 2
PTicker.set_callback callback: <function msg at 0x7fc6e82bdef0>, cb: <CFunctionType object at 0x7fc6e833fbb0>
ticker_set_callback 0x10a5fcfc0
Ticker.set_callback 0x10a5fcfc0
Ticker.tick 3
Ticker.tick 4
Alarm time at 4 ticks. Call 0x10a5fcfc0
[1]    76444 segmentation fault  python src/ticker.py
```

The function addresses change. Using Homebrew Python 3.9.4 it works correctly.
