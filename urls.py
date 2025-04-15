class Endpoints:

    login = "login"
    password_recovery = "forgot-password"
    password_reset = "reset-password"
    account = "account"
    profile = "profile"
    order_history = "order-history"
    feed = "feed"

class Urls:

    main_page = "https://stellarburgers.nomoreparties.site/"
    login_page = f'{main_page}{Endpoints.login}'
    password_recovery = f'{main_page}{Endpoints.password_recovery}'
    password_reset = f'{main_page}{Endpoints.password_reset}'
    account_page = f'{main_page}{Endpoints.account}/{Endpoints.profile}'
    order_history = f'{main_page}{Endpoints.account}/{Endpoints.order_history}'
    orders_feed = f'{main_page}{Endpoints.feed}'