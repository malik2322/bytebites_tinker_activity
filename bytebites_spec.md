Client Feature Request
We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

Candidate Classes
User (Customer): Represents the person placing the order. It acts as the initiator of the system, storing essential data such as name, contact information, saved addresses, and payment methods.

Restaurant: Represents the vendor providing the food. This class must store the restaurant's name, address, operating hours, and, crucially, a linkage to its Menu Item catalog.

Order: The central transaction object that links the User, Restaurant, and Driver. It models the state of a request (e.g., "Placed," "Preparing," "Delivering," "Completed") and contains the total amount and order contents.

Driver (Courier): Represents the entity responsible for delivering the order. This class is essential for tracking, storing, and managing delivery logistics, including location, vehicle details, and availability.
