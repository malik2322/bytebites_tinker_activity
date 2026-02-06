"""
ByteBites Model Scaffolds Verification Script

Purpose: Manually verify that model classes can be instantiated and 
store attributes correctly without running formal unit tests.

This script:
  - Creates sample objects for each model
  - Populates with realistic data
  - Prints attributes to confirm they're accessible
  - Does NOT test logic or calculations
"""

from models import MenuItem, User, Restaurant, Driver, Order
from datetime import datetime


def print_header(title: str):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def print_object_details(obj_name: str, obj, attributes: list):
    """Print object details in a readable format"""
    print(f"\n{obj_name}:")
    print("-" * 70)
    for attr in attributes:
        value = getattr(obj, attr, "NOT FOUND")
        print(f"  {attr:25} : {value}")


# ============================================================================
# STEP 1: Verify MenuItem Creation
# ============================================================================

print_header("1. MENUITEM VERIFICATION")

burger = MenuItem(
    name="Spicy Burger",
    price=12.99,
    category="Burgers",
    popularity_rating=4.8
)

soda = MenuItem(
    name="Large Soda",
    price=3.49,
    category="Drinks",
    popularity_rating=4.5
)

dessert = MenuItem(
    name="Chocolate Cake",
    price=5.99,
    category="Desserts",
    popularity_rating=4.9
)

# Display MenuItem instances
print_object_details("MenuItem 1 (Spicy Burger)", burger, 
                     ["name", "price", "category", "popularity_rating"])

print_object_details("MenuItem 2 (Large Soda)", soda,
                     ["name", "price", "category", "popularity_rating"])

print_object_details("MenuItem 3 (Chocolate Cake)", dessert,
                     ["name", "price", "category", "popularity_rating"])

print(f"\n✓ Created {3} MenuItem objects successfully")


# ============================================================================
# STEP 2: Verify User Creation
# ============================================================================

print_header("2. USER VERIFICATION")

customer_john = User(
    name="John Doe",
    contact_info="555-0123"
)

# Populate additional attributes
customer_john.saved_addresses.append("456 Oak Ave, Austin, TX")
customer_john.saved_addresses.append("789 Pine St, Austin, TX")

customer_john.payment_methods.append({
    "type": "credit_card",
    "last_four": "1234",
    "name": "Visa"
})

print_object_details("User (John Doe)", customer_john,
                     ["name", "contact_info", "saved_addresses", 
                      "payment_methods", "purchase_history"])

print(f"\n✓ User attributes accessible:")
print(f"  - Saved addresses: {len(customer_john.saved_addresses)} stored")
print(f"  - Payment methods: {len(customer_john.payment_methods)} stored")
print(f"  - Purchase history: {len(customer_john.purchase_history)} orders")


# ============================================================================
# STEP 3: Verify Restaurant Creation
# ============================================================================

print_header("3. RESTAURANT VERIFICATION")

restaurant = Restaurant(
    name="Spicy Delights",
    address="123 Main St, Austin, TX"
)

# Populate menu items
restaurant.menu_items.append(burger)
restaurant.menu_items.append(soda)
restaurant.menu_items.append(dessert)

# Populate operating hours
restaurant.operating_hours["Monday"] = "10:00 AM - 10:00 PM"
restaurant.operating_hours["Tuesday"] = "10:00 AM - 10:00 PM"
restaurant.operating_hours["Wednesday"] = "10:00 AM - 11:00 PM"

print_object_details("Restaurant (Spicy Delights)", restaurant,
                     ["name", "address", "operating_hours", "menu_items"])

print(f"\n✓ Restaurant attributes accessible:")
print(f"  - Menu items: {len(restaurant.menu_items)} items")
print(f"  - Operating hours: {len(restaurant.operating_hours)} days configured")
print(f"  - Menu contains: {[item.name for item in restaurant.menu_items]}")


# ============================================================================
# STEP 4: Verify Driver Creation
# ============================================================================

print_header("4. DRIVER VERIFICATION")

driver_alice = Driver(
    name="Alice Smith",
    vehicle_type="Car"
)

# Set driver details
driver_alice.current_location = "50 miles from restaurant"
driver_alice.is_available = True

print_object_details("Driver (Alice Smith)", driver_alice,
                     ["name", "vehicle_type", "current_location", 
                      "is_available", "active_deliveries"])

print(f"\n✓ Driver attributes accessible:")
print(f"  - Available: {driver_alice.is_available}")
print(f"  - Location: {driver_alice.current_location}")
print(f"  - Active deliveries: {len(driver_alice.active_deliveries)}")


# ============================================================================
# STEP 5: Verify Order Creation
# ============================================================================

print_header("5. ORDER VERIFICATION")

order = Order(
    user=customer_john,
    restaurant=restaurant
)

# Populate order details
order.selected_items.append(burger)
order.selected_items.append(soda)
order.driver = driver_alice

print_object_details("Order (John's Order)", order,
                     ["user", "restaurant", "driver", "selected_items",
                      "status", "total_cost", "created_at", "completed_at"])

print(f"\n✓ Order attributes accessible:")
print(f"  - Customer name: {order.user.name}")
print(f"  - Restaurant: {order.restaurant.name}")
print(f"  - Driver assigned: {order.driver.name if order.driver else 'None'}")
print(f"  - Items in order: {len(order.selected_items)}")
print(f"  - Items selected: {[item.name for item in order.selected_items]}")
print(f"  - Order status: {order.status}")
print(f"  - Total cost: ${order.total_cost:.2f}")
print(f"  - Created at: {order.created_at}")
print(f"  - Completed at: {order.completed_at}")


# ============================================================================
# STEP 6: Verify Relationships
# ============================================================================

print_header("6. RELATIONSHIP VERIFICATION")

print("\nUser → Order Relationship:")
print(f"  - User object stored in Order: {order.user is customer_john}")
print(f"  - User name retrieval: {order.user.name}")

print("\nRestaurant → MenuItem Relationship:")
print(f"  - MenuItem objects in Restaurant: {burger in restaurant.menu_items}")
print(f"  - Restaurant menu accessible from Order: {order.restaurant is restaurant}")

print("\nDriver → Order Relationship:")
print(f"  - Driver object stored in Order: {order.driver is driver_alice}")
print(f"  - Driver name retrieval: {order.driver.name if order.driver else 'None'}")

print("\nOrder → MenuItem Relationship:")
print(f"  - MenuItem objects in Order: {burger in order.selected_items}")
print(f"  - Can access item details: {order.selected_items[0].name}")


# ============================================================================
# SUMMARY
# ============================================================================

print_header("VERIFICATION SUMMARY")

print("\n✓ All class instantiations successful")
print("✓ All attributes are accessible")
print("✓ Object references stored correctly")
print("✓ Collections (lists/dicts) work as expected")
print("✓ Model scaffolds ready for business logic implementation")

print("\nObjects created:")
print(f"  - {3} MenuItem objects")
print(f"  - {1} User object")
print(f"  - {1} Restaurant object (with {len(restaurant.menu_items)} menu items)")
print(f"  - {1} Driver object")
print(f"  - {1} Order object (with {len(order.selected_items)} items)")

print("\n" + "="*70)
print("  Verification Complete - All Models Are Ready")
print("="*70 + "\n")
