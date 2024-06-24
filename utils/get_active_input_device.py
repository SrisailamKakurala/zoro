import pyaudio


def is_input_device(info):
    return info['maxInputChannels'] > 0

def is_potential_bluetooth_device(info):
    return 'bluetooth' in info['name'].lower()

def get_device_index():
    p = pyaudio.PyAudio()
    num_devices = p.get_device_count()

    for i in range(num_devices):
        info = p.get_device_info_by_index(i)
        if is_input_device(info) and is_potential_bluetooth_device(info):
            try:
                if p.is_format_supported(44100.0, input_device=i, input_channels=1, input_format=pyaudio.paInt16):
                    # print(f"Active Bluetooth input device found: {info['name']}")
                    return i
            except ValueError as e:
                pass
                # print(f"Device {info['name']} does not support 44100 Hz sample rate. Error: {e}")
    
    # Default to the first available microphone if no Bluetooth input device is found
    for i in range(num_devices):
        info = p.get_device_info_by_index(i)
        if is_input_device(info):
            print(f"Using default input device: {info['name']}")
            return i

    return None


