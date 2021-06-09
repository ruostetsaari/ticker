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
The hex values of storage address vary

```
loading /home/julien/Workspace/Rust/ticker/target/debug/libticker.so
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
