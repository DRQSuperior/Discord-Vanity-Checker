import random
import requests
import time

WEBHOOK_URL = 'WEBHOOK_URL'


def send_webhook(vanity):
    data = {
        'content': f'**Available Vanity:** *{vanity}*',
    }
    requests.post(WEBHOOK_URL, json=data)


def check_vanity_url(vanity_url):
    url = f'https://ptb.discord.com/api/v9/invites/{vanity_url}'
    response = requests.get(url)
    return response.status_code == 404


def get_vanities():
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|',
               '\\', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?', '`', '~']
    with open('vanities.txt', 'r') as f:
        lines = f.readlines()

    # Remove duplicates and sort the lines
    lines = sorted(set(lines))

    with open('vanities.txt', 'w') as f:
        for line in lines:
            for symbol in symbols:
                line = line.replace(symbol, '')
            f.write(line.lower())

    with open('vanities.txt', 'r') as f:
        vanities = f.readlines()
    return vanities


def main():
    vanities = get_vanities()
    while True:
        for _ in range(15):
            vanity = random.choice(vanities).strip()
            if check_vanity_url(vanity):
                send_webhook(vanity)
                print(f'Vanity: discord.gg/{vanity} is available!')
            else:
                print(f'Vanity: discord.gg/{vanity} is not available.')
        time.sleep(random.randint(10, 500))


if __name__ == '__main__':
    main()