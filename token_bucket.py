import time
import random

def token_bucket_simulator(burst_packets, bucket_capacity, token_generation_rate):
   
    tokens = 0
    dropped_packets = 0
    packets_sent = 0

    print("Token Bucket Simulation")
    print(f"Bucket Capacity: {bucket_capacity}, Token Rate: {token_generation_rate} tokens/sec")
    
    start_time = time.time()
    last_token_add_time = start_time

    for i, packet in enumerate(burst_packets):
        current_time = time.time()
        
        time_elapsed = current_time - last_token_add_time
        tokens_to_add = int(time_elapsed * token_generation_rate)
        tokens = min(tokens + tokens_to_add, bucket_capacity)
        last_token_add_time = current_time

        if tokens >= 1: 
            tokens -= 1
            packets_sent += 1
            print(f"[{current_time - start_time:.2f}s] ✅ Packet {i+1} arrived. Sent using a token. Tokens left: {tokens}")
        else:
            dropped_packets += 1
            print(f"[{current_time - start_time:.2f}s] ❌ Packet {i+1} arrived, but no tokens. Dropped.")
        
        time.sleep(random.uniform(0.0, 0.2))

    print(f"\nToken Bucket: Total packets dropped = {dropped_packets}")
    print(f"Token Bucket: Total packets sent = {packets_sent}")

num_packets = 50
bursty_traffic = []
for i in range(num_packets):
    bursty_traffic.append(f"Pkt_{i}")
print("Case ")

token_bucket_simulator(bursty_traffic, bucket_capacity=15, token_generation_rate=12)
print("Case 2")
token_bucket_simulator(bursty_traffic, bucket_capacity=15, token_generation_rate=5)
print("Case 3")

token_bucket_simulator(bursty_traffic, bucket_capacity=15, token_generation_rate=20)