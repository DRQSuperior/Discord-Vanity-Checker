import random
import requests
import time

WEBHOOK_URL = 'https://discord.com/api/webhooks/1095924861462921266/8aGkHKBQ7K2pAzeArasJMnRbI8k1ZnAalDIcYlWF729xu1Ep3bpz9IxvXUoiDaBsCdIm'


def send_webhook(vanity):
    data = {
        'content': f'**Available Vanity:** *.gg/{vanity}*',
    }
    requests.post(WEBHOOK_URL, json=data)


def check_vanity_url(vanity_url):
    url = f'https://ptb.discord.com/api/v9/invites/{vanity_url}'
    response = requests.get(url)
    return response.status_code == 404


def get_vanities():
    with open('vanities.txt', 'r') as f:
        lines = f.read().splitlines()

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|',
               '\\', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?', '`', '~']
    cleaned_lines = [line.translate(str.maketrans('', '', ''.join(symbols))).lower() for line in lines]
    vanities = sorted(set(cleaned_lines))
    return vanities


def main():
    vanities = get_vanities()
    while True:
        for _ in range(15):
            vanity = random.choice(vanities)
            if check_vanity_url(vanity):
                send_webhook(vanity)
                print(f'Vanity: discord.gg/{vanity} is available!')
            else:
                print(f'Vanity: discord.gg/{vanity} is not available.')
        time.sleep(random.uniform(0.01, 8.0))


if __name__ == '__main__':
    main()
