import random
import time

# dictionary to store messages with their unlock time
message_dict = {}

def send_msg(msg: str, delay: int, units: str):
    if not isinstance(delay, int):
        raise Exception("Delay must be an integer.")

    if units not in ["seconds", "minutes", "hours"]:
        raise Exception("Units must be 'seconds', 'minutes', or 'hours'.")

    unit_seconds = {"seconds": 1, "minutes": 60, "hours": 3600}

    unlock_time = time.time() + delay * unit_seconds[units]

    # Generate a unique 6-digit ID
    msg_id = random.randint(100000, 999999)
    while msg_id in message_dict:
        msg_id = random.randint(100000, 999999)

    message_dict[msg_id] = {'message': msg, 'unlock_time': unlock_time}

    print(msg_id)
    return msg_id

def get_msg(id: int):
    current_time = time.time()

    msg_entry = message_dict.get(id)

    if not msg_entry or current_time < msg_entry['unlock_time']:
        print("cannot retrieve your message. The message may not exist or more time may need to pass.")
        return False

    print(msg_entry['message'])
    return True
