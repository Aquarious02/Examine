from pygen.device import Device

if __name__ == '__main__':
    my_device = Device(0x12)
    print(my_device.set_time(1))
    pass
