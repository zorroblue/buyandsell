# Buy and Sell API for Dashboard

## Explanation of the model:

There are two main types of post - offers and bids

What you offer to sell, is called an offer. <br>
Other users' offers are called bids.

## Working:

The API offers endpoints to do the following as of now:

1. Create a new offer
2. Create a new user ( done at the time of dashboard registration)
3. Viewing all bids
4. Sending an interest for a bid along with the quoted price
5. Cancel the interest

## Running:

1. Clone the repo `git clone https://github.com/zorroblue/buyandsell`
2. `cd buyandsell`
3. Make migrations if any `python manage.py mkaemigrations`
4. Migrate `python manage.py migrate`
5. Shift to the native sqlite3 database or any databse you like. Mention the path in environmental variable DATABASE_URL
6. Run the server `python manage.py runserver`
