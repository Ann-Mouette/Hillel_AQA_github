"""
Моніторингова система.

Моніторингова система клєнта надсилає сигнал,
що вона працездатна кожні 30-31 сек - наприклад
Timestamp 05:45:40, а в наступному повідомлені
— Timestamp 05:45:09 (тут різниця heartbeat в
31 секунду).
Є декілька дублючих потоків, що шлють дані одночасно,
тож ми можемо проаналізувати лише один потік -
Key TSTFEED0300|7E3E|0400.
Засобами автоматизації проаналізуйте наданий
нам лог: hblog.txt.
відберіть лише строки з вказаним ключем
Key TSTFEED0300|7E3E|0400.
Створіть функцію, що поверне лог-файл,
де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек,
але менше 33 логувало WARNING в файл hb_test.log,
для кожного випадку де heartbeat більше рівно 33
логувало ERROR в файл hb_test.log
Зверніть увагу, що нам для аналізу помилок було
б добре знати час, в який помилка відбулася.

Обов’язково включіть результат роботи —
файл hb_test.log в PR.
"""

from datetime import datetime


def analyze_heartbeat_log(file_path, key, output_path):
    """Analyze a log file and logs heartbeat violations."""
    with open(file_path, 'r') as log_file:
        log_lines = log_file.readlines()

    filtered_lines = [line for line in log_lines if key in line]

    timestamps = []

    for line in filtered_lines:
        timestamp_index = line.find('Timestamp ')
        if timestamp_index != -1:
            timestamp_str = line[timestamp_index + 10:timestamp_index + 18]
            timestamp = datetime.strptime(timestamp_str, '%H:%M:%S')
            timestamps.append((timestamp, line))

    with open(output_path, 'w') as output_file:
        for i in range(len(timestamps) - 1):
            current_time, current_line = timestamps[i]
            next_time, _ = timestamps[i + 1]

            time_difference = (current_time - next_time).total_seconds()

            if 31 < time_difference < 33:
                output_file.write(
                    f'WARNING: Heartbeat delay {time_difference} seconds '
                    f'at {current_time.strftime("%H:%M:%S")}\n',
                )
            elif time_difference >= 33:
                output_file.write(
                    f'ERROR: Heartbeat delay {time_difference} seconds '
                    f'at {current_time.strftime("%H:%M:%S")}\n',
                )


analyze_heartbeat_log(
    file_path='hblog.txt',
    key='Key TSTFEED0300|7E3E|0400',
    output_path='hb_test.log',
)
