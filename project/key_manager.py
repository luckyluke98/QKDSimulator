class KeyManager():
    def __init__(self, own, timeline, keysize, num_keys):
        self.own = own
        self.timeline = timeline
        self.lower_protocols = []
        self.keysize = keysize
        self.num_keys = num_keys
        self.keys = []
        self.times = []
        
    def send_request(self):
        for p in self.lower_protocols:
            p.push(self.keysize, self.num_keys)
            
    def pop(self, key):
        self.keys.append(key)
        self.times.append(self.timeline.now() * 1e-9)
        
    def consume(self):
        return self.keys.pop(0)