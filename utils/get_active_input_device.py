import pyaudio


def is_bluetooth_input_device(info):
    # Check if it's an input device and potentially a Bluetooth device
    is_input_device = info['maxInputChannels'] > 0
    is_potential_bluetooth = 'bluetooth' in info['name'].lower()
    return is_input_device and is_potential_bluetooth


def get_device_index():
    p = pyaudio.PyAudio()
    num_devices = p.get_device_count()
    
    for i in range(num_devices):
        info = p.get_device_info_by_index(i)
        
        # Check if it's a potential Bluetooth input device
        if is_bluetooth_input_device(info):
            active_input_device = info['hostApi'] != -1 and p.is_format_supported(44100.0, input_device=i, input_channels=1, input_format=pyaudio.paInt16)
            if active_input_device:
                print(f"Active Bluetooth input device found: {info['name']}")
                return i
    
    # Default to None if no active Bluetooth input device is found
    return None