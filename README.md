# GPTWebApp

This is a simple web server with oauth2 authentication from google

## Installation

To install the required packages, run `pip install -r requirements.txt`
Then, edit `config.json` and add your OpenAI Key

The tool can be started with `python app.py`

### Google Oauth2 Keys
AI: To get the keys from the Google Cloud Console, you need to follow these steps:

* Go to the Google Cloud Console (https://console.cloud.google.com/).
* Create a new project or select an existing project.
* Go to the APIs & Services dashboard.
* Click on the Create Credentials button and select OAuth client ID.
* Select the Web application option.
* Enter a name for your OAuth client ID.
* In the Authorized JavaScript origins field, add the URL of your web server.
* In the Authorized redirect URIs field, add the URL of your web server followed by /oauth2callback (e.g. http://localhost:8000/oauth2callback).
* Click the Create button.
*  You will be presented with your client ID and client secret. Make sure to keep these values secret and secure.

Once you have your client ID and client secret, you can use them to authenticate users with Google's OAuth2 API.

## Usage

Provide instructions on how to use the project, including any command line arguments or configuration options.

## Contributing

Explain how others can contribute to the project, including guidelines for submitting bug reports, feature requests, and pull requests.

## License

This project is published under the MIT license (see `license.txt`)

## Authors

Main authors:
- Reto Bättig - reto@baettig.org

## Acknowledgments

Thanks to the OpenAI GPT Models for all the help and tipps!

