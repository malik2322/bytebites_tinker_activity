================================================================================
                    ByteBites - Four Core Classes UML Diagram
================================================================================

┌─────────────────────────────────────────────────────────────────────────────┐
│                                 USER (Customer)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ Attributes:                                                                  │
│  - name: str                                                                 │
│  - contact_info: str                                                         │
│  - saved_addresses: List[str]                                                │
│  - payment_methods: List[Dict]                                               │
│  - purchase_history: List[Order]    ◄──── Verifies real users by history    │
│                                                                               │
│ Methods:                                                                     │
│  + add_saved_address(address: str)                                           │
│  + add_payment_method(payment: Dict)                                         │
│  + add_to_purchase_history(order: Order)                                     │
│  + is_real_user(): bool                                                      │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │ initiates
         │ (1 to *)
         ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│                                  ORDER (Transaction)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ Attributes:                                                                  │
│  - user: User                                                                │
│  - restaurant: Restaurant                                                    │
│  - driver: Driver                                                            │
│  - selected_items: List[MenuItem]   ◄──── Groups selected items             │
│  - status: str                      ◄──── Placed, Preparing, Delivering...  │
│  - total_cost: float                ◄──── Computed automatically             │
│  - created_at: datetime                                                      │
│  - completed_at: datetime                                                    │
│                                                                               │
│ Methods:                                                                     │
│  + add_item(item: MenuItem)                                                  │
│  + remove_item(item: MenuItem)                                               │
│  + _compute_total_cost()            ◄──── Auto-calculates total              │
│  + assign_driver(driver: Driver)                                             │
│  + update_status(status: str)                                                │
│  + get_order_summary(): Dict                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
         ↑                    ↑                    ↑
         │                    │                    │
   placed_by (1)         fulfilled_by (1)    delivers (1)
         │                    │                    │
         │ (1 to *)           │ (1 to *)           │ (1 to *)
         │                    │                    │
    USER ◄─────────────── ORDER ──────────────► DRIVER
                             RESTAURANT             DELIVERS
                               │
                               │ (1 to *)
                               ↓
                            MENUITEM
                     (name, price, category, rating)


┌─────────────────────────────────────────────────────────────────────────────┐
│                              RESTAURANT (Vendor)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Attributes:                                                                  │
│  - name: str                                                                 │
│  - address: str                                                              │
│  - operating_hours: Dict[str, str]                                           │
│  - menu_items: List[MenuItem]       ◄──── Manages item catalog               │
│                                                                               │
│ Methods:                                                                     │
│  + set_operating_hours(day: str, hours: str)                                 │
│  + add_menu_item(item: MenuItem)                                             │
│  + get_menu_items(): List[MenuItem]                                          │
│  + filter_by_category(category: str): List[MenuItem]  ◄──── Browse items    │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │ manages
         │ (1 to *)
         ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│                                 MENUITEM                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ Attributes:                                                                  │
│  - name: str               (e.g., "Spicy Burger", "Large Soda")             │
│  - price: float                                                              │
│  - category: str           (e.g., "Drinks", "Desserts", "Burgers")          │
│  - popularity_rating: float                                                  │
└─────────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────────┐
│                               DRIVER (Courier)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ Attributes:                                                                  │
│  - name: str                                                                 │
│  - vehicle_type: str               (Motorcycle, Car, Bicycle, etc.)         │
│  - current_location: str            ◄──── Tracks delivery location           │
│  - is_available: bool                                                        │
│  - active_deliveries: List[Order]   ◄──── Manages logistics                  │
│                                                                               │
│ Methods:                                                                     │
│  + set_location(location: str)                                               │
│  + set_availability(available: bool)                                         │
│  + accept_delivery(order: Order)                                             │
│  + complete_delivery(order: Order)                                           │
└─────────────────────────────────────────────────────────────────────────────┘


================================================================================
                              KEY RELATIONSHIPS
================================================================================

1. USER ──initiates──► ORDER
   - A User creates an Order
   - One User can have multiple Orders (1:N)
   - Used to verify real users via purchase_history

2. RESTAURANT ──fulfills──► ORDER
   - A Restaurant fulfills an Order
   - One Restaurant can fulfill multiple Orders (1:N)

3. DRIVER ──delivers──► ORDER
   - A Driver delivers an Order
   - One Driver can deliver multiple Orders (1:N)
   - Optional: An Order may not have a Driver assigned initially

4. ORDER ──contains──► MENUITEM
   - An Order contains selected Items
   - One Order can contain multiple MenuItems (N:N)

5. RESTAURANT ──manages──► MENUITEM
   - A Restaurant manages its Menu
   - One Restaurant can have multiple MenuItems (1:N)
   - Supports filtering by category (Drinks, Desserts, Burgers, etc.)


================================================================================
                            SPECIFICATION ALIGNMENT
================================================================================

✓ Customer Management      → User class tracks names and purchase history
✓ User Verification       → is_real_user() checks purchase history
✓ Item Browsing           → MenuItem with name, price, category, rating
✓ Menu Management         → Restaurant manages MenuItems with filtering
✓ Transaction Grouping    → Order groups items and computes total cost
✓ Order States            → Status tracks: Placed, Preparing, Delivering, Completed
✓ Driver Management       → Driver class with location and delivery logistics
✓ Cost Calculation        → Order._compute_total_cost() auto-calculates

================================================================================
