import keyboard
import json
import os



def read_keystrokes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        keystrokes = file.readlines()
    return keystrokes

def read_existing_frequency(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def update_keystroke_frequency(keystrokes, frequency_dict):
    for key in keystrokes:
        frequency_dict[key.strip()] = frequency_dict.get(key.strip(), 0) + 1
    return frequency_dict

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

keystroke_file = 'keystroke.txt'
frequency_json_file = 'keystroke_frequency.json'

keystrokes = read_keystrokes(keystroke_file)
frequency_dict = read_existing_frequency(frequency_json_file)
frequency_dict = update_keystroke_frequency(keystrokes, frequency_dict)

write_json(frequency_json_file, frequency_dict)

open(keystroke_file, 'w').close()



with open(keystroke_file, 'a', encoding='utf-8') as file:
    # Write the value of keypressed to the file
    stack_modifier = []
    flush_incr = 0
    def on_key_event(e):
        global flush_incr
        flush_incr = flush_incr + 1
        is_modifier = keyboard.is_modifier(e.scan_code)

        if is_modifier:
            if e.event_type == "down":
                if e.name not in stack_modifier:
                    stack_modifier.append(e.name)
            else:
                stack_modifier.remove(e.name)
        else:
            if e.event_type == "down":
                keypressed = '+'.join(stack_modifier) + '+' + e.name if stack_modifier else e.name
                print(keypressed)
                file.write(f'{keypressed}\n')
                # "^": 313,
        
        if flush_incr == 10:
            file.flush()
            flush_incr = 0

    keyboard.hook(on_key_event)
    keyboard.wait()


