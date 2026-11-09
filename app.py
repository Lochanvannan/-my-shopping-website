
from flask import Flask, render_template_string, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "shopping-demo-secret-key-change-this"

# --------------------------------------------------
# PRODUCT LIST
# GST rates below are DEMO values.
# Confirm the correct GST rate for each product before
# using this website for real business.
# --------------------------------------------------

products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "category": "Electronics",
        "price": 1499,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "category": "Electronics",
        "price": 2499,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        "id": 3,
        "name": "Running Shoes",
        "category": "Fashion",
        "price": 1999,
        "gst": 5,
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff"
    },
    {
        "id": 4,
        "name": "Backpack",
        "category": "Fashion",
        "price": 999,
        "gst": 5,
        "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62"
    },
    {
        "id": 5,
        "name": "Gaming Mouse",
        "category": "Electronics",
        "price": 799,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1527814050087-3793815479db"
    },
    {
        "id": 6,
        "name": "Laptop",
        "category": "Electronics",
        "price": 54999,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853"
    },
    {
        "id": 7,
        "name": "Sunglasses",
        "category": "Fashion",
        "price": 699,
        "gst": 5,
        "image": "https://images.unsplash.com/photo-1511499767150-a48a237f0083"
    },
    {
        "id": 8,
        "name": "Camera",
        "category": "Electronics",
        "price": 24999,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32"
    },
    {
        "id": 9,
        "name": "Coffee Mug",
        "category": "Home",
        "price": 299,
        "gst": 5,
        "image": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d"
    },
    {
        "id": 10,
        "name": "Desk Lamp",
        "category": "Home",
        "price": 899,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c"
    },
    {
        "id": 11,
        "name": "Bluetooth Speaker",
        "category": "Electronics",
        "price": 1299,
        "gst": 18,
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1"
    },
    {
        "id": 12,
        "name": "T-Shirt",
        "category": "Fashion",
        "price": 599,
        "gst": 5,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab"
    }
]

DELIVERY_FEE = 50


# --------------------------------------------------
# COMMON WEBSITE DESIGN
# --------------------------------------------------

STYLE = """
<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f7fb;
    color: #222;
}

header {
    background: #111827;
    color: white;
    padding: 18px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
}

.logo {
    font-size: 25px;
    font-weight: bold;
    color: #38bdf8;
}

nav a {
    color: white;
    text-decoration: none;
    margin-left: 20px;
    font-weight: bold;
}

.hero {
    padding: 55px 7%;
    background: linear-gradient(120deg, #0f172a, #2563eb);
    color: white;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
}

.container {
    padding: 35px 7%;
}

.products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 22px;
}

.card {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 15px #00000012;
    transition: 0.2s;
}

.card:hover {
    transform: translateY(-5px);
}

.card img {
    width: 100%;
    height: 190px;
    object-fit: cover;
}

.card-content {
    padding: 18px;
}

.category {
    color: #64748b;
    font-size: 13px;
}

.price {
    color: #2563eb;
    font-size: 22px;
    font-weight: bold;
}

button, .button {
    background: #2563eb;
    color: white;
    border: none;
    padding: 12px 18px;
    border-radius: 8px;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    font-size: 15px;
}

button:hover, .button:hover {
    background: #1d4ed8;
}

input, textarea {
    width: 100%;
    padding: 12px;
    margin: 8px 0 16px;
    border: 1px solid #cbd5e1;
    border-radius: 7px;
}

table {
    width: 100%;
    background: white;
    border-collapse: collapse;
}

th, td {
    padding: 14px;
    border-bottom: 1px solid #e5e7eb;
    text-align: left;
}

.summary {
    background: white;
    padding: 22px;
    border-radius: 12px;
    margin-top: 25px;
    max-width: 500px;
    margin-left: auto;
}

footer {
    text-align: center;
    background: #111827;
    color: white;
    padding: 25px;
    margin-top: 40px;
}

@media(max-width: 600px) {
    header {
        padding: 18px 5%;
    }

    nav a {
        margin-left: 8px;
    }

    .hero h1 {
        font-size: 30px;
    }

    .container {
        padding: 25px 5%;
    }

    table {
        font-size: 13px;
    }

    th, td {
        padding: 8px;
    }
}
</style>
"""


def page(content, title="MyShop"):
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ title }}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        """ + STYLE + """
    </head>
    <body>
        <header>
            <div class="logo">MyShop 🛍️</div>
            <nav>
                <a href="{{ url_for('home') }}">Home</a>
                <a href="{{ url_for('cart') }}">Cart 🛒</a>
                <a href="{{ url_for('checkout') }}">Checkout</a>
            </nav>
        </header>

        """ + content + """

        <footer>
            <p>Contact: 91xxxx</p>
            <p>Published by loc____</p>
            <p>© 2026 MyShop. Demo website.</p>
        </footer>
    </body>
    </html>
    """, title=title)


# --------------------------------------------------
# CART HELPERS
# --------------------------------------------------

def get_cart():
    return session.get("cart", {})


def calculate_totals():
    cart = get_cart()

    subtotal = 0
    gst_total = 0
    cart_items = []

    for product in products:
        product_id = str(product["id"])
        quantity = int(cart.get(product_id, 0))

        if quantity > 0:
            item_subtotal = product["price"] * quantity
            item_gst = item_subtotal * product["gst"] / 100

            subtotal += item_subtotal
            gst_total += item_gst

            item = product.copy()
            item["quantity"] = quantity
            item["item_total"] = item_subtotal
            item["item_gst"] = item_gst

            cart_items.append(item)

    delivery = DELIVERY_FEE if cart_items else 0
    total = subtotal + gst_total + delivery

    return cart_items, subtotal, gst_total, delivery, total


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    content = """
    <section class="hero">
        <h1>Discover Your Next Favorite Product</h1>
        <p>Shop electronics, fashion, home products and more.</p>
        <a href="#products" class="button">Shop Now</a>
    </section>

    <section class="container" id="products">
        <h2>✨ Featured Products</h2>

        <div class="products">
            {% for product in products %}
            <div class="card">
                <img src="{{ product.image }}?auto=format&fit=crop&w=600&q=80"
                     alt="{{ product.name }}">

                <div class="card-content">
                    <p class="category">{{ product.category }}</p>
                    <h3>{{ product.name }}</h3>

                    <p class="price">
                        ₹{{ "{:,.2f}".format(product.price) }}
                    </p>

                    <p>Demo GST: {{ product.gst }}%</p>

                    <form action="{{ url_for('add_to_cart', product_id=product.id) }}"
                          method="POST">
                        <button type="submit">Add to Cart 🛒</button>
                    </form>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>
    """

    return page(
        render_template_string(content, products=products),
        "MyShop - Online Shopping"
    )


# --------------------------------------------------
# ADD TO CART
# --------------------------------------------------

@app.route("/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if not any(p["id"] == product_id for p in products):
        return redirect(url_for("home"))

    cart = get_cart()
    product_id = str(product_id)

    cart[product_id] = int(cart.get(product_id, 0)) + 1

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# --------------------------------------------------
# CART PAGE
# --------------------------------------------------

@app.route("/cart")
def cart():
    items, subtotal, gst, delivery, total = calculate_totals()

    content = """
    <div class="container">
        <h1>🛒 Your Shopping Cart</h1>

        {% if items %}
        <table>
            <tr>
                <th>Product</th>
                <th>Price</th>
                <th>Qty</th>
                <th>Action</th>
            </tr>

            {% for item in items %}
            <tr>
                <td>{{ item.name }}</td>
                <td>₹{{ "{:,.2f}".format(item.price) }}</td>
                <td>
                    <form action="{{ url_for('update_cart', product_id=item.id) }}"
                          method="POST">
                        <input type="number" name="quantity"
                               value="{{ item.quantity }}" min="0"
                               style="width:70px">
                        <button type="submit">Update</button>
                    </form>
                </td>
                <td>
                    <form action="{{ url_for('remove_item', product_id=item.id) }}"
                          method="POST">
                        <button type="submit">Remove</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
        </table>

        <div class="summary">
            <h3>Order Summary</h3>
            <p>Subtotal: ₹{{ "{:,.2f}".format(subtotal) }}</p>
            <p>GST: ₹{{ "{:,.2f}".format(gst) }}</p>
            <p>Delivery Fee: ₹{{ "{:,.2f}".format(delivery) }}</p>
            <hr>
            <h2>Total: ₹{{ "{:,.2f}".format(total) }}</h2>

            <a href="{{ url_for('checkout') }}" class="button">
                Proceed to Checkout
            </a>
        </div>

        {% else %}
            <h3>Your cart is empty.</h3>
            <a href="{{ url_for('home') }}" class="button">Continue Shopping</a>
        {% endif %}
    </div>
    """

    return page(
        render_template_string(
            content,
            items=items,
            subtotal=subtotal,
            gst=gst,
            delivery=delivery,
            total=total
        ),
        "MyShop - Cart"
    )


# --------------------------------------------------
# UPDATE CART
# --------------------------------------------------

@app.route("/update/<int:product_id>", methods=["POST"])
def update_cart(product_id):
    quantity = request.form.get("quantity", "1")

    try:
        quantity = max(0, int(quantity))
    except ValueError:
        quantity = 1

    cart = get_cart()
    product_id = str(product_id)

    if quantity == 0:
        cart.pop(product_id, None)
    else:
        cart[product_id] = quantity

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# --------------------------------------------------
# REMOVE ITEM
# --------------------------------------------------

@app.route("/remove/<int:product_id>", methods=["POST"])
def remove_item(product_id):
    cart = get_cart()
    cart.pop(str(product_id), None)

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# --------------------------------------------------
# CHECKOUT PAGE
# --------------------------------------------------

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    items, subtotal, gst, delivery, total = calculate_totals()

    if not items:
        return redirect(url_for("cart"))

    if request.method == "POST":
        customer_name = request.form.get("name", "").strip()
        customer_phone = request.form.get("phone", "").strip()
        customer_address = request.form.get("address", "").strip()

        if customer_name and customer_phone and customer_address:
            # Demo only: no real payment or permanent order storage.
            session["cart"] = {}

            content = """
            <div class="container">
                <h1>🎉 Order Submitted!</h1>
                <p>Thank you, {{ name }}!</p>
                <p>Your demo order has been submitted successfully.</p>
                <p>This website does not process real payments.</p>
                <a href="{{ url_for('home') }}" class="button">
                    Continue Shopping
                </a>
            </div>
            """

            return page(
                render_template_string(content, name=customer_name),
                "Order Submitted"
            )

    content = """
    <div class="container">
        <h1>📦 Checkout</h1>

        <form method="POST" style="max-width:600px;background:white;
                                   padding:25px;border-radius:12px">

            <label>Full Name</label>
            <input type="text" name="name" required>

            <label>Phone Number</label>
            <input type="tel" name="phone" required>

            <label>Delivery Address</label>
            <textarea name="address" rows="4" required></textarea>

            <h3>Order Summary</h3>

            <p>Subtotal: ₹{{ "{:,.2f}".format(subtotal) }}</p>
            <p>GST: ₹{{ "{:,.2f}".format(gst) }}</p>
            <p>Delivery Fee: ₹{{ "{:,.2f}".format(delivery) }}</p>

            <hr>

            <h2>Total: ₹{{ "{:,.2f}".format(total) }}</h2>

            <button type="submit">Place Demo Order</button>
        </form>
    </div>
    """

    return page(
        render_template_string(
            content,
            items=items,
            subtotal=subtotal,
            gst=gst,
            delivery=delivery,
            total=total
        ),
        "MyShop - Checkout"
    )


# --------------------------------------------------
# RUN WEBSITE
# --------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
