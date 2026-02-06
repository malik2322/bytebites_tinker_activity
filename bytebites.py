"""
ByteBites Backend Logic
A food delivery application backend system
"""

from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum


class OrderStatus(Enum):
    """Enum for order states"""
    PLACED = "Placed"
    PREPARING = "Preparing"
    DELIVERING = "Delivering"
    COMPLETED = "Completed"


class MenuItem:
    """Represents a food item available in the restaurant"""
    
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        """
        Initialize a menu item
        
        Args:
            name: Name of the item (e.g., "Spicy Burger")
            price: Price of the item
            category: Category of the item (e.g., "Drinks", "Desserts")
            popularity_rating: Rating of the item (0-5)
        """
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating
    
    def __repr__(self):
        return f"MenuItem(name='{self.name}', price=${self.price}, category='{self.category}', rating={self.popularity_rating})"


class Menu:
    """Manages the collection of all menu items for a restaurant"""
    
    def __init__(self):
        """Initialize an empty menu"""
        self.items: List[MenuItem] = []
    
    def add_item(self, item: MenuItem) -> None:
        """Add an item to the menu"""
        self.items.append(item)
    
    def remove_item(self, item_name: str) -> None:
        """Remove an item from the menu by name"""
        self.items = [item for item in self.items if item.name != item_name]
    
    def get_items_by_category(self, category: str) -> List[MenuItem]:
        """Filter menu items by category"""
        return [item for item in self.items if item.category == category]
    
    def get_all_items(self) -> List[MenuItem]:
        """Get all menu items"""
        return self.items
    
    def __repr__(self):
        return f"Menu(items_count={len(self.items)})"


class User:
    """Represents a customer in the ByteBites system"""
    
    def __init__(self, name: str, contact_info: str):
        """
        Initialize a user/customer
        
        Args:
            name: Customer's full name
            contact_info: Customer's phone number or email
        """
        self.name = name
        self.contact_info = contact_info
        self.saved_addresses: List[str] = []
        self.payment_methods: List[Dict[str, str]] = []
        self.purchase_history: List['Order'] = []
    
    def add_saved_address(self, address: str) -> None:
        """Save an address for future orders"""
        self.saved_addresses.append(address)
    
    def add_payment_method(self, payment_method: Dict[str, str]) -> None:
        """Add a payment method (credit card, debit card, etc.)"""
        self.payment_methods.append(payment_method)
    
    def add_to_purchase_history(self, order: 'Order') -> None:
        """Record a completed order in purchase history"""
        self.purchase_history.append(order)
    
    def is_real_user(self) -> bool:
        """Verify if user is a real user with at least one purchase"""
        return len(self.purchase_history) > 0
    
    def __repr__(self):
        return f"User(name='{self.name}', contact='{self.contact_info}')"


class Driver:
    """Represents a delivery driver/courier"""
    
    def __init__(self, name: str, vehicle_type: str):
        """
        Initialize a driver
        
        Args:
            name: Driver's name
            vehicle_type: Type of vehicle (e.g., "Motorcycle", "Car", "Bicycle")
        """
        self.name = name
        self.vehicle_type = vehicle_type
        self.current_location: Optional[str] = None
        self.is_available = True
        self.active_deliveries: List['Order'] = []
    
    def set_location(self, location: str) -> None:
        """Update driver's current location"""
        self.current_location = location
    
    def set_availability(self, available: bool) -> None:
        """Set driver's availability status"""
        self.is_available = available
    
    def accept_delivery(self, order: 'Order') -> None:
        """Accept a delivery order"""
        self.active_deliveries.append(order)
    
    def complete_delivery(self, order: 'Order') -> None:
        """Mark a delivery as completed"""
        if order in self.active_deliveries:
            self.active_deliveries.remove(order)
    
    def __repr__(self):
        return f"Driver(name='{self.name}', vehicle='{self.vehicle_type}', available={self.is_available})"


class Restaurant:
    """Represents a restaurant vendor"""
    
    def __init__(self, name: str, address: str):
        """
        Initialize a restaurant
        
        Args:
            name: Restaurant's name
            address: Restaurant's address
        """
        self.name = name
        self.address = address
        self.operating_hours: Dict[str, str] = {}
        self.menu = Menu()
    
    def set_operating_hours(self, day: str, hours: str) -> None:
        """Set operating hours for a specific day"""
        self.operating_hours[day] = hours
    
    def add_menu_item(self, item: MenuItem) -> None:
        """Add an item to the restaurant's menu"""
        self.menu.add_item(item)
    
    def get_menu(self) -> Menu:
        """Get the restaurant's menu"""
        return self.menu
    
    def __repr__(self):
        return f"Restaurant(name='{self.name}', address='{self.address}')"


class Order:
    """Represents a single transaction/order in the ByteBites system"""
    
    def __init__(self, user: User, restaurant: Restaurant):
        """
        Initialize an order
        
        Args:
            user: Customer placing the order
            restaurant: Restaurant fulfilling the order
        """
        self.user = user
        self.restaurant = restaurant
        self.driver: Optional[Driver] = None
        self.selected_items: List[MenuItem] = []
        self.status = OrderStatus.PLACED
        self.total_cost = 0.0
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
    
    def add_item(self, item: MenuItem) -> None:
        """Add an item to the order"""
        self.selected_items.append(item)
        self._compute_total_cost()
    
    def remove_item(self, item: MenuItem) -> None:
        """Remove an item from the order"""
        if item in self.selected_items:
            self.selected_items.remove(item)
            self._compute_total_cost()
    
    def _compute_total_cost(self) -> None:
        """Calculate and update the total cost of the order"""
        self.total_cost = sum(item.price for item in self.selected_items)
    
    def assign_driver(self, driver: Driver) -> None:
        """Assign a driver to this order"""
        self.driver = driver
        driver.accept_delivery(self)
    
    def update_status(self, new_status: OrderStatus) -> None:
        """Update the order status"""
        self.status = new_status
        if new_status == OrderStatus.COMPLETED:
            self.completed_at = datetime.now()
            self.user.add_to_purchase_history(self)
            if self.driver:
                self.driver.complete_delivery(self)
    
    def get_order_summary(self) -> Dict:
        """Get a summary of the order"""
        return {
            "customer": self.user.name,
            "restaurant": self.restaurant.name,
            "items": [item.name for item in self.selected_items],
            "total_cost": self.total_cost,
            "status": self.status.value,
            "driver": self.driver.name if self.driver else "Not assigned"
        }
    
    def __repr__(self):
        return f"Order(user='{self.user.name}', restaurant='{self.restaurant.name}', status='{self.status.value}', total=${self.total_cost:.2f})"


# Example usage
if __name__ == "__main__":
    # Create a restaurant
    restaurant = Restaurant("Spicy Delights", "123 Main St, Austin, TX")
    restaurant.set_operating_hours("Monday", "10:00 AM - 10:00 PM")
    
    # Add menu items
    restaurant.add_menu_item(MenuItem("Spicy Burger", 12.99, "Burgers", 4.8))
    restaurant.add_menu_item(MenuItem("Large Soda", 3.49, "Drinks", 4.5))
    restaurant.add_menu_item(MenuItem("Chocolate Cake", 5.99, "Desserts", 4.9))
    
    # Create a customer
    user = User("John Doe", "555-0123")
    user.add_saved_address("456 Oak Ave, Austin, TX")
    
    # Create an order
    order = Order(user, restaurant)
    order.add_item(restaurant.menu.items[0])  # Add Spicy Burger
    order.add_item(restaurant.menu.items[1])  # Add Large Soda
    
    # Create and assign a driver
    driver = Driver("Alice Smith", "Car")
    driver.set_location("50 miles away")
    order.assign_driver(driver)
    
    # Process the order
    order.update_status(OrderStatus.PREPARING)
    order.update_status(OrderStatus.DELIVERING)
    order.update_status(OrderStatus.COMPLETED)
    
    # Display results
    print(order.get_order_summary())
    print(f"User is real: {user.is_real_user()}")
    print(f"Purchase history: {len(user.purchase_history)} orders")
