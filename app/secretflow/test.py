import secretflow as sf
import numpy as np

sf.init(['alice', 'bob', 'carol'], address='local')
dev = sf.PYU('alice')
data = dev(np.random.rand)(3, 4)
sf.reveal(data)
