import pandas as pd
import numpy as np
from pathlib import Path

def generate_synthetic_network_data(filename="data/network_traffic.csv", num_samples=2000):
    np.random.seed(42)
    protocols = ['tcp', 'udp', 'icmp']
    services = ['http', 'smtp', 'ftp', 'dns', 'ssh']
    flag_types = ['SF', 'S0', 'REJ', 'RSTO']
    
    data = []
    for _ in range(num_samples):
        is_anomaly = np.random.choice([0, 1], p=[0.8, 0.2])
        protocol = np.random.choice(protocols)
        service = np.random.choice(services)
        flag = 'SF' if is_anomaly == 0 else np.random.choice(flag_types)
        
        if is_anomaly == 0:
            duration = np.random.exponential(scale=2.0)
            src_bytes = int(np.random.normal(loc=500, scale=100))
            dst_bytes = int(np.random.normal(loc=2000, scale=500))
            wrong_fragment = 0
            urgent = 0
            hot = 0
            num_failed_logins = 0
            count = int(np.random.poisson(lam=5))
            srv_count = int(np.random.poisson(lam=5))
            serror_rate = np.random.uniform(0.0, 0.05)
            rerror_rate = np.random.uniform(0.0, 0.05)
            label = "normal"
        else:
            attack_type = np.random.choice(["DoS", "Probe", "R2L", "U2R"])
            duration = np.random.exponential(scale=15.0) if attack_type != "DoS" else 0.0
            src_bytes = int(np.random.exponential(scale=5000)) if attack_type != "DoS" else 0
            dst_bytes = int(np.random.exponential(scale=10000)) if attack_type != "DoS" else 0
            wrong_fragment = np.random.choice([0, 1, 3], p=[0.7, 0.2, 0.1])
            urgent = np.random.choice([0, 1], p=[0.95, 0.05])
            hot = np.random.randint(0, 5) if attack_type in ["R2L", "U2R"] else 0
            num_failed_logins = np.random.randint(1, 5) if attack_type == "R2L" else 0
            count = int(np.random.poisson(lam=150)) if attack_type == "DoS" else int(np.random.poisson(lam=20))
            srv_count = int(np.random.poisson(lam=150)) if attack_type == "DoS" else int(np.random.poisson(lam=20))
            serror_rate = np.random.uniform(0.8, 1.0) if flag == 'S0' else np.random.uniform(0.0, 0.2)
            rerror_rate = np.random.uniform(0.8, 1.0) if flag == 'REJ' else np.random.uniform(0.0, 0.2)
            label = attack_type

        row = {
            'duration': max(0, round(duration, 2)),
            'protocol_type': protocol,
            'service': service,
            'flag': flag,
            'src_bytes': max(0, src_bytes),
            'dst_bytes': max(0, dst_bytes),
            'wrong_fragment': wrong_fragment,
            'urgent': urgent,
            'hot': hot,
            'num_failed_logins': num_failed_logins,
            'count': count,
            'srv_count': srv_count,
            'serror_rate': round(serror_rate, 2),
            'rerror_rate': round(rerror_rate, 2),
            'label': label
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Synthetic dataset generated successfully at '{filename}' with {num_samples} records.")

if __name__ == "__main__":
    generate_synthetic_network_data()
