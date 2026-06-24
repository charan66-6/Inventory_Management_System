import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Inventory Management System",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Inventory Management System")
st.caption("Manage your products and inventory stock")

# ======================
# SIDEBAR
# ======================

with st.sidebar:

    st.title("📦 Inventory")

    menu = st.radio(
        "Navigation",
        [
            "View Products",
            "Add Product",
            "Update Product",
            "Delete Product",
            "Low Stock Alert"
        ]
    )

# ======================
# VIEW PRODUCTS
# ======================

if menu == "View Products":

    summary = requests.get(
        f"{BASE_URL}/summary"
    ).json()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Products",
        summary["total_products"]
    )

    c2.metric(
        "Total Stock",
        summary["total_quantity"]
    )

    c3.metric(
        "Inventory Value",
        f"₹{summary['inventory_value']}"
    )

    st.divider()

    products = requests.get(
        f"{BASE_URL}/products"
    ).json()

    # SEARCH BAR

    left, right = st.columns([4, 2])

    with left:
        st.subheader("Available Products")

    with right:
        search = st.text_input(
            "🔍 Search Product",
            placeholder="Enter product name..."
        )

    # FILTER PRODUCTS

    filtered_products = {}

    if search:

        for product_id, item in products.items():

            if search.lower() in item["name"].lower():

                filtered_products[product_id] = item

    else:

        filtered_products = products

    # DISPLAY PRODUCTS

    if len(filtered_products) == 0:

        st.error(
            "❌ No matching product found."
        )

    else:

        for product_id, item in filtered_products.items():

            with st.container(border=True):

                col1, col2, col3, col4 = st.columns(
                    [4, 2, 2, 2]
                )

                # PRODUCT DETAILS

                with col1:

                    st.subheader(item["name"])

                    st.caption(
                        f"Product ID : {product_id}"
                    )

                    if item["quantity"] < 5:

                        st.markdown(
                            "🔴 **Low Stock**"
                        )

                    elif item["quantity"] < 10:

                        st.markdown(
                            "🟡 **Limited Stock**"
                        )

                    else:

                        st.markdown(
                            "🟢 **In Stock**"
                        )

                # PRICE

                with col2:

                    st.metric(
                        "Price",
                        f"₹{item['price']}"
                    )

                # QUANTITY

                with col3:

                    st.metric(
                        "Quantity",
                        item["quantity"]
                    )

                # QUANTITY BUTTONS

                with col4:

                    b1, b2 = st.columns(2)

                    with b1:

                        if st.button(
                            "➕",
                            key=f"add_{product_id}"
                        ):

                            requests.patch(
                                f"{BASE_URL}/products/{product_id}/quantity",
                                params={
                                    "change": 1
                                }
                            )

                            st.rerun()

                    with b2:

                        if st.button(
                            "➖",
                            key=f"sub_{product_id}"
                        ):

                            requests.patch(
                                f"{BASE_URL}/products/{product_id}/quantity",
                                params={
                                    "change": -1
                                }
                            )

                            st.rerun()

# ======================
# ADD PRODUCT
# ======================

elif menu == "Add Product":

    st.header("➕ Add Product")

    try:

        products = requests.get(
            f"{BASE_URL}/products"
        ).json()

        next_id = max(
            map(int, products.keys())
        ) + 1

    except:

        next_id = 1

    st.text_input(
        "Product ID",
        value=str(next_id),
        disabled=True
    )

    with st.form("add_product"):

        name = st.text_input(
            "Product Name"
        )

        price = st.number_input(
            "Price",
            min_value=0.0
        )

        quantity = st.number_input(
            "Quantity",
            min_value=0
        )

        submit = st.form_submit_button(
            "Add Product"
        )

        if submit:

            response = requests.post(
                f"{BASE_URL}/products",
                json={
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.success(
                    f"✅ Product Added Successfully (ID: {data['product_id']})"
                )

# ======================
# UPDATE PRODUCT
# ======================

elif menu == "Update Product":

    st.header("✏️ Update Product")

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        step=1
    )

    with st.form("update_product"):

        name = st.text_input(
            "New Product Name"
        )

        price = st.number_input(
            "New Price",
            min_value=0.0
        )

        quantity = st.number_input(
            "New Quantity",
            min_value=0
        )

        submit = st.form_submit_button(
            "Update Product"
        )

        if submit:

            response = requests.put(
                f"{BASE_URL}/products/{product_id}",
                json={
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }
            )

            if response.status_code == 200:

                st.success(
                    "✅ Product Updated Successfully"
                )

            else:

                st.error(
                    response.json()["detail"]
                )

# ======================
# DELETE PRODUCT
# ======================

elif menu == "Delete Product":

    st.header("🗑️ Delete Product")

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Product"):

        response = requests.delete(
            f"{BASE_URL}/products/{product_id}"
        )

        if response.status_code == 200:

            st.success(
                response.json()["message"]
            )

        else:

            st.error(
                response.json()["detail"]
            )

# ======================
# LOW STOCK ALERT
# ======================

elif menu == "Low Stock Alert":

    st.header("⚠️ Low Stock Products")

    products = requests.get(
        f"{BASE_URL}/low-stock"
    ).json()

    if len(products) == 0:

        st.success(
            "✅ All products are sufficiently stocked."
        )

    else:

        for product_id, item in products.items():

            with st.container(border=True):

                st.subheader(
                    item["name"]
                )

                st.write(
                    f"Product ID : {product_id}"
                )

                st.write(
                    f"Quantity Left : {item['quantity']}"
                )

                st.markdown(
                    "🔴 **Low Stock**"
                )
                