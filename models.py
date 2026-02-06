"""
ByteBites Backend - Data Models

The system consists of four core entities: User, Restaurant, Order, and Driver.
- User: Initiates orders and stores personal, address, and payment information.
- Restaurant: Provides food, maintains operational details, and manages a menu catalog.
- Order: Central transaction connecting User, Restaurant, and Driver with order status and contents.
- Driver: Handles delivery logistics including availability, location tracking, and vehicle details.
"""

from typing import List, Dict, Optional
from datetime import datetime


class MenuItem:
    """Represents a food item available for purchase"""
    
    def __init__(
        self,
        name: str,
        price: float,
        category: str,
        popularity_rating: float
    ):
        """
        Initialize a menu item
        
        Args:
            name: Name of the food item (e.g., "Spicy Burger")
            price: Price of the item in dollars
            category: Category classification (e.g., "Burgers", "Drinks", "Desserts")
            popularity_rating: Rating between 0-5 indicating item popularity
        """
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class User:
    """Represents a customer in the ByteBites system"""
    
    def __init__(self, name: str, contact_info: str):
        """
        Initialize a customer
        
        Args:
            name: Customer's full name
            contact_info: Customer's contact information (phone or email)
        """
        self.name = name
        self.contact_info = contact_info
        self.saved_addresses: List[str] = []
        self.payment_methods: List[Dict[str, str]] = []
        self.purchase_history: List['Order'] = []


class Restaurant:
    """Represents a restaurant vendor"""
    
    def __init__(self, name: str, address: str):
        """
        Initialize a restaurant
        
        Args:
            name: Restaurant name
            address: Restaurant physical address
        """
        self.name = name
        self.address = address
        self.operating_hours: Dict[str, str] = {}
        self.menu_items: List[MenuItem] = []


class Driver:
    """Represents a delivery courier"""
    
    def __init__(self, name: str, vehicle_type: str):
        """
        Initialize a driver
        
        Args:
            name: Driver's full name
            vehicle_type: Type of vehicle (e.g., "Car", "Motorcycle", "Bicycle")
        """
        self.name = name
        self.vehicle_type = vehicle_type
        self.current_location: Optional[str] = None
        self.is_available: bool = True
        self.active_deliveries: List['Order'] = []


class Order:
    """Represents a single transaction/order in the system"""
    
    def __init__(self, user: User, restaurant: Restaurant):
        """
        Initialize an order
        
        Args:
            user: Reference to the User placing the order
            restaurant: Reference to the Restaurant fulfilling the order
        """
        self.user = user
        self.restaurant = restaurant
        self.driver: Optional[Driver] = None
        self.selected_items: List[MenuItem] = []
        self.status: str = "Placed"
        self.total_cost: float = 0.0
        self.created_at: datetime = datetime.now()
        self.completed_at: Optional[datetime] = None


