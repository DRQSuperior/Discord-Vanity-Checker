# Discord Vanity Checker :mag_right: :inbox_tray:

Python script to automate checking availability of Discord server vanity URLs and sends vanities when webhook become available.

## Features :rocket:

- Automates checking the availability of Discord vanity URLs :white_check_mark:
- Sends notifications via a Discord webhook :bell:
- Randomized checking intervals for variability :arrows_counterclockwise:
- Easy-to-use and customizable :computer:

## Usage :hammer_and_wrench:

1. Install the required dependencies: `pip install requests`
2. Update the `WEBHOOK_URL` variable in `discord_vanity_checker.py` with your own Discord webhook URL.
3. Populate the `vanities.txt` file with the vanity URLs you want to check.
4. Run the script: `python discord_vanity_checker.py`

## Notes :memo:

- Make sure you have Python 3.x installed :snake:
- The `requests` library is required for making API requests :package:

## Contributing :handshake:

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License :page_with_curl:

This project is licensed under the [MIT License](LICENSE).

