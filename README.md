# The borrower App

## Prerequisites

- You have to have poetry installed locally
- You have at least Python 3.8 installed

This is a streamlit app that you can run locally by running the following command

```bash
poetry shell && streamlit run blockchain/app.pp
```

After running this command successfully, you will get a message like this

```
  You can now view your Streamlit app in your browser.

  Network URL: http://192.168.132.119:8501
  External URL: http://109.173.213.88:8501
```

## Calling the API

The initial step towards initiating a series of automatically triggered events inside of Kaleido (leveraging subscriptions), is to send the borrower data from this borrower App.

However, you can send it from any other place (like another borrower app), by programatically calling a custom-build API for the purposes of the Blockchain POC.

Here's a sample API call using the terminal (for example WSL 2, make sure you install curl if it's not installed)

```bash
curl --location --request POST 'https://rrjkbunuf0.execute-api.us-east-1.amazonaws.com/prod' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "Oswaldo",
    "phone": "616616616",
    "email": "test@gmail.com",
    "street": "alpha street",
    "street_2": "some address",
    "property_city": "Queretaro",
    "property_country": "Mexico",
    "property_state": "",
    "property_zip_code": "",
    "tell_us_about_your_loan": "",
    "property_location": "",
    "property_use": "Vacation",
    "property_value": "1M",
    "line_of_credit": "500K",
    "plans_for_the_funds": "",
    "loan_used_for_business": "",
    "suffix": "Mr.",
    "time_at_address": "",
    "best_time_to_call": "",
    "secondary_phone_number": "",
    "country_of_citizenship": "",
    "country_of_residence": "Laos",
    "social_security_number": "",
    "date_of_birth": "April 15",
    "marital_status": "",
    "preferred_language": "",
    "employment_status": "",
    "anual_income": "1M",
    "source_of_income": "",
    "additional_income": "",
    "coapplicant": "",
    "vendor": "receive_borrower",
    "topics": "123-456"
}'
```

To avoid any errors, pass the exact same fields (all of them) and always generate a random "topics" field, since this is where you actually pass the loan ID.

If it goes well, you will receive a response like this:

```bash
{
    "borrower_received": true,
    "data": [
        {
            "id": "cf59f306-c8c1-49df-9f0c-454652d6edd3",
            "hash": "bebfe5032ff64869b4166cab6583ec8cf8110a13b9a512282441513b1801d0d5"
        }
    ],
    "hash": "2949db7085574e88473660195835a5490d78fc2ebb57f174d70c6a645c01ff2e",
    "header": {
        "id": "8f7309bb-2e8e-4798-a37c-6131fefce79b",
        "type": "private",
        "txtype": "batch_pin",
        "author": "0xb1db08b8d06510518f1328f3e3da2de5c55eb766",
        "created": "2022-02-14T18:27:13.739015941Z",
        "namespace": "default",
        "group": "cbb5174472caa6facc2dcffd78a63a6b52e604d8c6e05d4e732c9c4817f11d5c",
        "topics": [
            "123-456"
        ],
        "tag": "credit_run",
        "datahash": "56150584e686e9f5aaa25ec74ff95543069b6aa9915986a4507bfca905baa048"
    }
}
```

You can then go to https://share.streamlit.io/git-zventus/analyst-ui/main/lender/app.py and type exactly what you sent on the "topics" key (for example I sent 123-456) so that's what I would type under "Please enter the loan ID"

### Bonus.

Here's another example of how to start the process using a JavaScript example:

```
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "name": "Oswaldo",
  "phone": "616616616",
  "email": "test@gmail.com",
  "street": "alpha street",
  "street_2": "some address",
  "property_city": "Queretaro",
  "property_country": "Mexico",
  "property_state": "",
  "property_zip_code": "",
  "tell_us_about_your_loan": "",
  "property_location": "",
  "property_use": "Vacation",
  "property_value": "1M",
  "line_of_credit": "500K",
  "plans_for_the_funds": "",
  "loan_used_for_business": "",
  "suffix": "Mr.",
  "time_at_address": "",
  "best_time_to_call": "",
  "secondary_phone_number": "",
  "country_of_citizenship": "",
  "country_of_residence": "Laos",
  "social_security_number": "",
  "date_of_birth": "April 15",
  "marital_status": "",
  "preferred_language": "",
  "employment_status": "",
  "anual_income": "1M",
  "source_of_income": "",
  "additional_income": "",
  "coapplicant": "",
  "vendor": "receive_borrower",
  "topics": "123-456"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://rrjkbunuf0.execute-api.us-east-1.amazonaws.com/prod", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
