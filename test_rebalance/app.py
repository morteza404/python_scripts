from swift.common.ring import RingBuilder

ring = RingBuilder(17,3,1)

devs = [
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.31', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 0}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'id': 1, 'replication_ip': '192.168.40.31', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.31', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 2}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'id': 3, 'replication_ip': '192.168.40.31', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.31', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 4}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'id': 5, 'replication_ip': '192.168.40.31', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.31', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.31', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 6}, 
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'id': 7, 'replication_ip': '192.168.40.32', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.32', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 8}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'id': 9, 'replication_ip': '192.168.40.32', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.32', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 10}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'id': 11, 'replication_ip': '192.168.40.32', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.32', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 12}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.32', 'region': 1, 'id': 13, 'replication_ip': '192.168.40.32', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.34', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 14}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'id': 15, 'replication_ip': '192.168.40.34', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.34', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 16}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'id': 17, 'replication_ip': '192.168.40.34', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.34', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 18}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'id': 19, 'replication_ip': '192.168.40.34', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.34', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.34', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 20}, 
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'id': 21, 'replication_ip': '192.168.40.35', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.35', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 22}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'id': 23, 'replication_ip': '192.168.40.35', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.35', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 24}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'id': 25, 'replication_ip': '192.168.40.35', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.35', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 26}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.35', 'region': 1, 'id': 27, 'replication_ip': '192.168.40.35', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.36', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 28}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'id': 29, 'replication_ip': '192.168.40.36', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.36', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 30}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'id': 31, 'replication_ip': '192.168.40.36', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.36', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 32}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'id': 33, 'replication_ip': '192.168.40.36', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.36', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.36', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 34}, 
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'id': 35, 'replication_ip': '192.168.40.37', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.37', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 36}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'id': 37, 'replication_ip': '192.168.40.37', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.37', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 38}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'id': 39, 'replication_ip': '192.168.40.37', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.37', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 40}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.37', 'region': 1, 'id': 41, 'replication_ip': '192.168.40.37', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.38', 'parts': 4459, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 42}, 
{'replication_port': 6100, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'id': 43, 'replication_ip': '192.168.40.38', 'parts': 4458, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.38', 'parts': 4458, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 44}, 
{'replication_port': 6102, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'id': 45, 'replication_ip': '192.168.40.38', 'parts': 4458, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.38', 'parts': 4458, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 46}, 
{'replication_port': 6104, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'id': 47, 'replication_ip': '192.168.40.38', 'parts': 4458, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 1.0, 'ip': '172.20.40.38', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.38', 'parts': 4458, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 48}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'id': 49, 'replication_ip': '192.168.40.33', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.33', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 50}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'id': 51, 'replication_ip': '192.168.40.33', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.33', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 52}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'id': 53, 'replication_ip': '192.168.40.33', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.33', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 54}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.33', 'region': 1, 'id': 55, 'replication_ip': '192.168.40.33', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.39', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 56}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'id': 57, 'replication_ip': '192.168.40.39', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.39', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 58}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'id': 59, 'replication_ip': '192.168.40.39', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.39', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 60}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'id': 61, 'replication_ip': '192.168.40.39', 'parts': 3120, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.39', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.39', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 62}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'id': 63, 'replication_ip': '192.168.40.131', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.131', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 64}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'id': 65, 'replication_ip': '192.168.40.131', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.131', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 66}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'id': 67, 'replication_ip': '192.168.40.131', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.131', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 68}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.131', 'region': 1, 'id': 69, 'replication_ip': '192.168.40.131', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.132', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 70}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'id': 71, 'replication_ip': '192.168.40.132', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.132', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 72}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'id': 73, 'replication_ip': '192.168.40.132', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.132', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 74}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'id': 75, 'replication_ip': '192.168.40.132', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.132', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.132', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 76}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'id': 77, 'replication_ip': '192.168.40.133', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.133', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 78}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'id': 79, 'replication_ip': '192.168.40.133', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.133', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 80}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'id': 81, 'replication_ip': '192.168.40.133', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.133', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 82}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.133', 'region': 1, 'id': 83, 'replication_ip': '192.168.40.133', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'id': 84, 'replication_ip': '192.168.40.27', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.27', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 85}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'id': 86, 'replication_ip': '192.168.40.27', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.27', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 87}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'id': 88, 'replication_ip': '192.168.40.27', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.27', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 89}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.27', 'region': 1, 'id': 90, 'replication_ip': '192.168.40.27', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'port': 6000, 'replication_ip': '192.168.40.28', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'id': 91}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'id': 92, 'replication_ip': '192.168.40.28', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'port': 6100}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'port': 6101, 'replication_ip': '192.168.40.28', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'id': 93}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'id': 94, 'replication_ip': '192.168.40.28', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'port': 6102}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'port': 6103, 'replication_ip': '192.168.40.28', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'id': 95}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'id': 96, 'replication_ip': '192.168.40.28', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'port': 6104}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.28', 'region': 1, 'port': 6105, 'replication_ip': '192.168.40.28', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'id': 97}, 
{'replication_port': 6000, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'id': 98, 'replication_ip': '192.168.40.29', 'parts': 3121, 'meta': '', 'device': 'sdb', 'parts_wanted': 0, 'port': 6000}, 
{'replication_port': 6100, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'port': 6100, 'replication_ip': '192.168.40.29', 'parts': 3121, 'meta': '', 'device': 'sdc', 'parts_wanted': 0, 'id': 99}, 
{'replication_port': 6101, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'id': 100, 'replication_ip': '192.168.40.29', 'parts': 3121, 'meta': '', 'device': 'sdd', 'parts_wanted': 0, 'port': 6101}, 
{'replication_port': 6102, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'port': 6102, 'replication_ip': '192.168.40.29', 'parts': 3121, 'meta': '', 'device': 'sde', 'parts_wanted': 0, 'id': 101}, 
{'replication_port': 6103, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'id': 102, 'replication_ip': '192.168.40.29', 'parts': 3121, 'meta': '', 'device': 'sdf', 'parts_wanted': 0, 'port': 6103}, 
{'replication_port': 6104, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'port': 6104, 'replication_ip': '192.168.40.29', 'parts': 3121, 'meta': '', 'device': 'sdg', 'parts_wanted': 0, 'id': 103}, 
{'replication_port': 6105, 'zone': 1, 'weight': 0.7, 'ip': '172.20.40.29', 'region': 1, 'id': 104, 'replication_ip': '192.168.40.29', 'parts': 3120, 'meta': '', 'device': 'sdh', 'parts_wanted': 0, 'port': 6105}]

for dev in devs:
    ring.add_dev(dev)

ring.rebalance()

print(ring._dispersion_graph)