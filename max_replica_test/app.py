from swift.common.ring import RingBuilder

builder = RingBuilder.load("/home/shahbazi/Desktop/rings/object.builder")

rr = builder._build_max_replicas_by_tier(bound=float)

xx = sorted(rr.keys())

print(xx)