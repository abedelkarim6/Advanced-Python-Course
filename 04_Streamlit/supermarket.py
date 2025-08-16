import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Seeded Product Data
# =========================
products = [
    {
        "name": "Apples",
        "category": "Fruits",
        "price": 2.5,
        "stock": 120,
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
    },
    {
        "name": "Bananas",
        "category": "Fruits",
        "price": 1.8,
        "stock": 95,
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg",
    },
    {
        "name": "Oranges",
        "category": "Fruits",
        "price": 3.0,
        "stock": 80,
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg",
    },
    {
        "name": "Tomatoes",
        "category": "Vegetables",
        "price": 2.2,
        "stock": 150,
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Tomato_je.jpg",
    },
    {
        "name": "Potatoes",
        "category": "Vegetables",
        "price": 1.5,
        "stock": 200,
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg",
    },
    {
        "name": "Carrots",
        "category": "Vegetables",
        "price": 2.0,
        "stock": 100,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Carrots_of_many_colors.jpg",
    },
    {
        "name": "Onions",
        "category": "Vegetables",
        "price": 1.2,
        "stock": 160,
        "image": "https://upload.wikimedia.org/wikipedia/commons/1/18/Onion_on_White.JPG",
    },
    {
        "name": "Broccoli",
        "category": "Vegetables",
        "price": 3.5,
        "stock": 70,
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/03/Broccoli_and_cross_section_edit.jpg",
    },
    {
        "name": "Milk",
        "category": "Dairy",
        "price": 1.9,
        "stock": 90,
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Milk_glass.jpg",
    },
    {
        "name": "Cheese",
        "category": "Dairy",
        "price": 4.5,
        "stock": 60,
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Cheese.jpg",
    },
    {
        "name": "Yogurt",
        "category": "Dairy",
        "price": 2.8,
        "stock": 75,
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Plain_yogurt.jpg",
    },
    {
        "name": "Chicken Breast",
        "category": "Meat",
        "price": 7.5,
        "stock": 50,
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/55/Chicken_breast.jpg",
    },
    {
        "name": "Beef Steak",
        "category": "Meat",
        "price": 12.0,
        "stock": 40,
        "image": "https://upload.wikimedia.org/wikipedia/commons/b/bd/Beef_steak.jpg",
    },
    {
        "name": "Fish Fillet",
        "category": "Meat",
        "price": 9.0,
        "stock": 45,
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f8/Raw_fish_fillet.jpg",
    },
    {
        "name": "Rice",
        "category": "Grains",
        "price": 1.3,
        "stock": 180,
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/68/Rice_DSC01012.jpg",
    },
    {
        "name": "Pasta",
        "category": "Grains",
        "price": 2.0,
        "stock": 130,
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/57/Italian_pasta.jpg",
    },
    {
        "name": "Bread",
        "category": "Bakery",
        "price": 2.2,
        "stock": 85,
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Bread.jpg",
    },
    {
        "name": "Eggs",
        "category": "Dairy",
        "price": 3.2,
        "stock": 110,
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/71/Chicken_eggs.jpg",
    },
    {
        "name": "Butter",
        "category": "Dairy",
        "price": 3.8,
        "stock": 65,
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/36/Butter.jpg",
    },
    {
        "name": "Olive Oil",
        "category": "Condiments",
        "price": 6.0,
        "stock": 55,
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Olive_Oil_Bottle.jpg",
    },
]

product_df = pd.DataFrame(products)

# =========================
# Sidebar Navigation
# =========================
pages = ["Home", "Dashboard", "Cart", "About"]
choice = st.sidebar.radio("Navigate", pages)

# =========================
# Home Page
# =========================
if choice == "Home":
    st.title("🛒 Supermarket Products")
    st.write("Browse our available products:")

    for i, row in product_df.iterrows():
        with st.container():
            cols = st.columns([1, 2])
            with cols[0]:
                st.image(row["image"], width=150)
            with cols[1]:
                st.subheader(row["name"])
                st.write(f"**Category:** {row['category']}")
                st.write(f"**Price:** ${row['price']}")
                st.write(f"**In Stock:** {row['stock']} units")
                if st.button(f"Add to Cart - {row['name']}", key=f"btn{i}"):
                    st.session_state.setdefault("cart", []).append(row.to_dict())
                    st.success(f"{row['name']} added to cart!")

# =========================
# Dashboard Page
# =========================
elif choice == "Dashboard":
    st.title("📊 Supermarket Dashboard")

    st.write("### Inventory Stats")
    st.write(f"Total Products: {len(product_df)}")
    st.write(f"Total Stock: {product_df['stock'].sum()} units")

    st.write("### Stock by Category")
    stock_by_cat = product_df.groupby("category")["stock"].sum()
    fig, ax = plt.subplots()
    stock_by_cat.plot(kind="bar", ax=ax)
    ax.set_ylabel("Units")
    ax.set_title("Stock Distribution by Category")
    st.pyplot(fig)

    st.write("### Price Distribution")
    fig2, ax2 = plt.subplots()
    product_df["price"].plot(kind="hist", bins=10, ax=ax2)
    ax2.set_xlabel("Price ($)")
    ax2.set_title("Price Histogram")
    st.pyplot(fig2)

# =========================
# Cart Page
# =========================
elif choice == "Cart":
    st.title("🛒 Shopping Cart")
    if "cart" in st.session_state and st.session_state["cart"]:
        cart_df = pd.DataFrame(st.session_state["cart"])
        st.table(cart_df[["name", "price", "category"]])
        st.write(f"**Total Items:** {len(cart_df)}")
        st.write(f"**Total Price:** ${cart_df['price'].sum():.2f}")
    else:
        st.info("Your cart is empty!")

# =========================
# About Page
# =========================
elif choice == "About":
    st.title("ℹ️ About This App")
    st.write("This is a demo Streamlit supermarket application.")
    st.write("It showcases products, a shopping cart system, and a simple dashboard.")
    st.write("Developed for educational purposes.")
