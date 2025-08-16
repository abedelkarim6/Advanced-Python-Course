from utils import *


def show_menu():
    print("\n=== TIPS MANAGEMENT ===")
    print("1. Add Category")
    print("2. Add Tip")
    print("3. Update Tip")
    print("4. Delete Tip")
    print("5. Filter by Category")
    print("6. Search by Keyword")
    print("7. Mark/Unmark Favorite")
    print("8. Show Recent Tips")
    print("0. Exit")


def show_categories():
    print("Categories:")
    for cid, cname in get_categories():
        print(f"{cid}: {cname}")


if __name__ == "__main__":
    print("Welcome to the Tips Management System!")
    print("You can manage tips and categories in your SQLite database.")

    # Initialize the database connection
    while True:
        show_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            name = input("Enter category name: ")
            add_category(name)
            print("✅ Category added.")

        elif choice == "2":
            title = input("Enter tip title: ")
            content = input("Enter tip content: ")
            show_categories()
            category_id = int(input("Enter category ID: "))
            add_tip(title, content, category_id)
            print("✅ Tip added.")

        elif choice == "3":
            tip_id = int(input("Enter tip ID to update: "))
            title = input("New title (leave blank to keep current): ").strip() or None
            content = (
                input("New content (leave blank to keep current): ").strip() or None
            )
            category_id = input(
                "New category ID (leave blank to keep current): "
            ).strip()
            category_id = int(category_id) if category_id else None
            update_tip(tip_id, title, content, category_id)
            print("✏️ Tip updated.")

        elif choice == "4":
            tip_id = int(input("Enter tip ID to delete: "))
            delete_tip(tip_id)
            print("🗑️ Tip deleted.")

        elif choice == "5":
            show_categories()
            category_id = int(input("Enter category ID: "))
            tips = filter_by_category(category_id)
            for t in tips:
                print(t)

        elif choice == "6":
            keyword = input("Enter keyword: ")
            tips = search_by_keyword(keyword)
            for t in tips:
                print(t)

        elif choice == "7":
            tip_id = int(input("Enter tip ID to mark/unmark favorite: "))
            mark_favorite(tip_id)
            print("⭐ Favorite status toggled.")

        elif choice == "8":
            tips = get_recent_tips()
            for t in tips:
                print(t)

        elif choice == "0":
            print("Goodbye!")
            cursor.close()
            break

        else:
            print("❌ Invalid choice, try again.")
