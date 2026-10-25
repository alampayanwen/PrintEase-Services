
from pyscript import document
from pyscript import when


# Printing service prices
PRICES = {
    "black": 2,
    "colored": 5,
    "copy": 1
}


# Calculate the printing cost
@when("click", "#calculate-btn")
def calculate_total(event):
    service = document.querySelector("#service").value
    pages_input = document.querySelector("#pages").value
    result = document.querySelector("#result")

    try:
        pages = int(pages_input)

        if pages < 1:
            result.innerText = "Please enter at least 1 page."
            return

        price = PRICES[service]
        total = pages * price

        result.innerText = (
            f"Total cost: ₱{total:.2f} "
            f"({pages} page/s at ₱{price} per page)"
        )

    except ValueError:
        result.innerText = "Please enter a valid number of pages."


# Handle the sample order form
@when("submit", "#order-form")
def submit_order(event):
    event.preventDefault()

    name = document.querySelector("#customer-name").value.strip()
    pages_input = document.querySelector("#order-pages").value
    order_result = document.querySelector("#order-result")

    try:
        pages = int(pages_input)

        if not name:
            order_result.innerText = "Please enter your name."
            return

        if pages < 1:
            order_result.innerText = "Please enter at least 1 page."
            return

        order_result.innerText = (
            f"Thank you, {name}! Your sample order for "
            f"{pages} page/s has been recorded. "
            "This is a demonstration only; no actual order was sent."
        )

    except ValueError:
        order_result.innerText = "Please enter a valid number of pages."
