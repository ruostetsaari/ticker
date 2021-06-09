type Callback = extern "C" fn(u32);

pub struct Ticker {
    ticks: u32,
    limit: u32,
    callback: Option<Callback>
}

impl Ticker {
    fn new(limit: u32) -> Ticker {
	Ticker {
	    ticks: 0u32,
	    limit: limit,
	    callback: None
	}
    }
    fn set_callback(&mut self, callback: Callback) {
	println!("Ticker.set_callback {:?}", callback);
	self.callback = Some(callback);
    }
    fn tick(&mut self) {
	self.ticks += 1;
	println!("Ticker.tick {}", self.ticks);
	if let Some(callback) = self.callback {
	    if self.ticks % self.limit == 0 {
		println!("Alarm time at {} ticks. Call {:?}", self.ticks, callback);
		callback(self.ticks);
	    }
	}
    }
}

#[no_mangle]
pub extern "C" fn ticker_new(limit: u32) -> *mut Ticker {
    let ticker = Ticker::new(limit);
    Box::into_raw(Box::new(ticker))
}

#[no_mangle]
pub extern "C" fn ticker_free(ptr: *mut Ticker) {
    if ptr.is_null() {
        return;
    }
    unsafe {
        Box::from_raw(ptr);
    }
}

#[no_mangle]
pub extern "C" fn ticker_tick(ptr: *mut Ticker) {
    let ticker = unsafe {
        assert!(!ptr.is_null());
        &mut *ptr
    };
    ticker.tick();
}

#[no_mangle]
pub extern "C" fn ticker_set_callback(ptr: *mut Ticker, callback: Callback) {
    let ticker = unsafe {
        assert!(!ptr.is_null());
        &mut *ptr
    };
    println!("ticker_set_callback {:?}", callback);
    ticker.set_callback(callback);
}

