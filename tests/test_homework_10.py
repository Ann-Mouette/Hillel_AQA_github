"""
Ваша команда та ви розробляєте систему входу для веб-додатка.

І вам потрібно реалізувати тести на функцію для логування подій
в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити,
    логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f'Login event - Username: {username}, Status: {status}'

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
    )
    logger = logging.getLogger('log_event')

    # Логування події
    if status == 'success':
        logger.info(log_message)
    elif status == 'expired':
        logger.warning(log_message)
    else:
        logger.error(log_message)


def test_log_event_success():
    """Test the logging of a successful login."""
    log_file = 'test_success.txt'

    logger = logging.getLogger('log_event')

    handler = logging.FileHandler(log_file, mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    log_event('user1', 'success')

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Login event - Username: user1, Status: success' in log_content, (
        'Invalid login success message'
    )

    logger.removeHandler(handler)


def test_log_event_expired():
    """Test the old password login."""
    log_file = 'test_expired.txt'

    logger = logging.getLogger('log_event')

    handler = logging.FileHandler(log_file, mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    log_event('user2', 'expired')

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Login event - Username: user2, Status: expired' in log_content, (
        'Invalid message for legacy password'
    )

    logger.removeHandler(handler)


def test_log_event_failed():
    """Test logging in with an incorrect password."""
    log_file = 'test_failed.txt'

    logger = logging.getLogger('log_event')

    handler = logging.FileHandler(log_file, mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    log_event('user3', 'failed')

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'Login event - Username: user3, Status: failed' in log_content, (
        'Invalid message for invalid password'
    )

    logger.removeHandler(handler)
