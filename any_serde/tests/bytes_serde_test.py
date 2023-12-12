from any_serde import bytes_serde
import random


def test_bytes_rt() -> None:
    random.seed(2395872345)

    byte_values = [random.randint(0, 255) for _ in range(10_000)]

    obj = bytes(byte_values)
    data = bytes_serde.to_data(bytes, obj)
    print(data)
    obj_rt = bytes_serde.from_data(bytes, data)
    assert obj == obj_rt
