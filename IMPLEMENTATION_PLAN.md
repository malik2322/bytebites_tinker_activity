╔════════════════════════════════════════════════════════════════════════════════╗
║ BYTEBITES BACKEND - HIGH-LEVEL IMPLEMENTATION PLAN ║
║ Four Core Classes System Design ║
╚════════════════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════════════════
PROJECT OVERVIEW
═══════════════════════════════════════════════════════════════════════════════════

GOAL: Implement a Python backend system for the ByteBites food delivery app with:
• Customer management with purchase history verification
• Menu item catalog with category filtering
• Order transaction management with automatic cost calculation
• Driver/delivery logistics tracking

SCOPE: Four core classes with supporting data structures

1. MenuItem (Food items)
2. Restaurant (Menu management)
3. User (Customer management)
4. Order (Transaction management)
5. Driver (Delivery logistics)

DEPENDENCIES: Python 3.7+, datetime module, typing module, enum module

═══════════════════════════════════════════════════════════════════════════════════
IMPLEMENTATION PHASES
═══════════════════════════════════════════════════════════════════════════════════

PHASE 1: FOUNDATION (Data Models & Basic Structure)
────────────────────────────────────────────────────────────────────────────────────
Duration: 30-45 minutes
Deliverables: Core class definitions with attributes

Tasks:
☐ Create MenuItem class
├─ Attributes: name, price, category, popularity_rating
├─ **init**() method
└─ **repr**() for debugging

☐ Create User class
├─ Attributes: name, contact_info, saved_addresses, payment_methods, purchase_history
├─ **init**() method
└─ **repr**() method

☐ Create Restaurant class
├─ Attributes: name, address, operating_hours, menu_items
├─ **init**() method
└─ **repr**() method

☐ Create Driver class
├─ Attributes: name, vehicle_type, current_location, is_available, active_deliveries
├─ **init**() method
└─ **repr**() method

☐ Create Order class
├─ Attributes: user, restaurant, driver, selected_items, status, total_cost, timestamps
├─ **init**() method
└─ **repr**() method

☐ Create OrderStatus enum
├─ Values: PLACED, PREPARING, DELIVERING, COMPLETED

PHASE 2: CORE FUNCTIONALITY (Business Logic Methods)
────────────────────────────────────────────────────────────────────────────────────
Duration: 45-60 minutes
Deliverables: Functional methods for each class

Tasks:

☐ USER CLASS Methods
├─ add_saved_address(address: str) → Add delivery address
├─ add_payment_method(payment: Dict) → Add payment option
├─ add_to_purchase_history(order: Order) → Record completed order
├─ is_real_user() → bool; Verify user has purchase history
└─ Validation: Ensure data integrity in methods

☐ RESTAURANT CLASS Methods
├─ set_operating_hours(day: str, hours: str) → Set day/time
├─ add_menu_item(item: MenuItem) → Add to catalog
├─ remove_item(name: str) → Remove from catalog
├─ get_menu_items() → List[MenuItem]; Return all items
├─ filter_by_category(category: str) → List[MenuItem]; Category filter
└─ Error handling: Guard against duplicates/invalid items

☐ DRIVER CLASS Methods
├─ set_location(location: str) → Update current location
├─ set_availability(available: bool) → Toggle availability
├─ accept_delivery(order: Order) → Add to active deliveries
├─ complete_delivery(order: Order) → Remove from active deliveries
└─ Validation: Ensure only available drivers accept orders

☐ ORDER CLASS Methods
├─ add_item(item: MenuItem) → Add item & recalculate total
├─ remove_item(item: MenuItem) → Remove item & recalculate total
├─ \_compute_total_cost() → private; Sum all item prices
├─ assign_driver(driver: Driver) → Assign and update driver
├─ update_status(new_status: OrderStatus) → Update state
└─ get_order_summary() → Dict; Return order information

☐ FEATURE IMPLEMENTATION
├─ Automatic cost calculation on item changes
├─ Update purchase_history when order completes
├─ Timestamp tracking (created_at, completed_at)
└─ Status state management

PHASE 3: INTEGRATION & RELATIONSHIPS
────────────────────────────────────────────────────────────────────────────────────
Duration: 30-45 minutes
Deliverables: Proper class interactions and dependencies

Tasks:

☐ USER ↔ ORDER Integration
├─ Order stores reference to User
├─ User.purchase_history tracks completed Orders
└─ Test: Create order, complete it, verify in history

☐ RESTAURANT ↔ ORDER Integration
├─ Order stores reference to Restaurant
├─ Restaurant provides MenuItem objects to Order
└─ Test: Add items from restaurant menu to order

☐ RESTAURANT ↔ MENUITEM Integration
├─ Restaurant.menu_items manages MenuItem collection
├─ Filter by category functionality
└─ Test: Add items, filter by category

☐ DRIVER ↔ ORDER Integration
├─ Order optionally assigned to Driver
├─ Driver.active_deliveries tracks assigned Orders
├─ Completion removes from active_deliveries
└─ Test: Assign driver, complete delivery, verify removal

☐ CIRCULAR REFERENCE HANDLING
├─ Check for any issues with Order containing User/Restaurant/Driver
├─ User contains List[Order] (purchase_history)
└─ Ensure no infinite loops in **repr**() methods

PHASE 4: TESTING & VALIDATION
────────────────────────────────────────────────────────────────────────────────────
Duration: 30-45 minutes
Deliverables: Verified functionality and edge case handling

Tasks:

☐ UNIT TESTS (Basic functionality per class)
├─ MenuItem: Creation, attributes
├─ User: Address/payment addition, purchase history tracking
├─ Restaurant: Menu item management, category filtering
├─ Driver: Location/availability updates, delivery management
└─ Order: Item addition/removal, cost calculation, status updates

☐ INTEGRATION TESTS (Class interactions)
├─ Create complete order workflow
├─ Verify cost calculation accuracy
├─ Verify purchase history updates
├─ Verify driver assignment and delivery tracking
└─ Verify category filtering on actual menu

☐ EDGE CASE TESTING
├─ Empty orders (cost = 0)
├─ Duplicate item additions
├─ Order without driver assignment
├─ User with no purchase history (not real user)
├─ Restaurant with empty menu
└─ Status transitions validation

☐ EXAMPLE USAGE
├─ Create full end-to-end scenario
├─ Demonstrate all major features
├─ Verify output matches specification
└─ Document usage patterns

☐ CODE QUALITY
├─ Type hints on all methods
├─ Docstrings for all public methods
├─ Consistent naming conventions
├─ PEP 8 compliance
└─ Error handling for invalid inputs

═══════════════════════════════════════════════════════════════════════════════════
DETAILED IMPLEMENTATION SEQUENCE
═══════════════════════════════════════════════════════════════════════════════════

STEP 1: MenuItem Class
──────────────────────────────────────────────────────────────────────────────────
Purpose: Represent individual food items with metadata

Implementation:

1. Define attributes in **init**:
   - name: str (e.g., "Spicy Burger")
   - price: float (e.g., 12.99)
   - category: str (e.g., "Burgers")
   - popularity_rating: float (0-5 scale)

2. Add **repr**() for display

3. Optional: Add validation
   - Verify price >= 0
   - Verify rating 0-5

STEP 2: Restaurant Class
──────────────────────────────────────────────────────────────────────────────────
Purpose: Manage restaurant profile and menu

Implementation:

1. Define attributes in **init**:
   - name: str
   - address: str
   - operating_hours: Dict[str, str]
   - menu_items: List[MenuItem]

2. Implement menu_items management:
   - add_menu_item(item: MenuItem) → append to list
   - remove_item(name: str) → filter by name
   - get_menu_items() → return full list

3. Implement filtering:
   - filter_by_category(category: str)
   - Use list comprehension: [item for item in menu_items if item.category == category]

4. Implement operating hours:
   - set_operating_hours(day: str, hours: str) → store in dict

5. Add **repr**()

STEP 3: User Class
──────────────────────────────────────────────────────────────────────────────────
Purpose: Manage customer identity and verification

Implementation:

1. Define attributes in **init**:
   - name: str
   - contact_info: str
   - saved_addresses: List[str]
   - payment_methods: List[Dict]
   - purchase_history: List[Order]

2. Implement data management methods:
   - add_saved_address(address: str)
   - add_payment_method(payment: Dict)
   - add_to_purchase_history(order: Order)

3. Implement verification:
   - is_real_user() → return len(purchase_history) > 0

4. Add **repr**()

STEP 4: Driver Class
──────────────────────────────────────────────────────────────────────────────────
Purpose: Track delivery logistics and driver status

Implementation:

1. Define attributes in **init**:
   - name: str
   - vehicle_type: str
   - current_location: Optional[str]
   - is_available: bool
   - active_deliveries: List[Order]

2. Implement location tracking:
   - set_location(location: str) → update current_location

3. Implement availability management:
   - set_availability(available: bool)

4. Implement delivery management:
   - accept_delivery(order: Order) → append to active_deliveries
   - complete_delivery(order: Order) → remove from active_deliveries

5. Add **repr**()

STEP 5: Order Class (Core Transaction Logic)
──────────────────────────────────────────────────────────────────────────────────
Purpose: Link user, restaurant, driver and manage the transaction

Implementation:

1. Define attributes in **init**:
   - user: User
   - restaurant: Restaurant
   - driver: Optional[Driver]
   - selected_items: List[MenuItem]
   - status: OrderStatus (start with PLACED)
   - total_cost: float (initialize to 0.0)
   - created_at: datetime (current time)
   - completed_at: Optional[datetime]

2. Implement item management:
   - add_item(item: MenuItem):
     a. Append to selected_items
     b. Call \_compute_total_cost()
   - remove_item(item: MenuItem):
     a. Remove from selected_items if present
     b. Call \_compute_total_cost()

3. Implement cost calculation:
   - \_compute_total_cost():
     a. Sum all item prices: sum(item.price for item in selected_items)
     b. Update self.total_cost

4. Implement driver assignment:
   - assign_driver(driver: Driver):
     a. Set self.driver = driver
     b. Call driver.accept_delivery(self)

5. Implement status management:
   - update_status(new_status: OrderStatus):
     a. Set self.status = new_status
     b. If status == COMPLETED:
     - Set completed_at = datetime.now()
     - Call user.add_to_purchase_history(self)
     - Call driver.complete_delivery(self)

6. Implement summary generation:
   - get_order_summary() → Dict:
     Return dict with customer, restaurant, items, total, status, driver

7. Add **repr**()

STEP 6: OrderStatus Enum
──────────────────────────────────────────────────────────────────────────────────
Purpose: Define valid order states

Implementation:

1. Create Enum with four values:
   - PLACED = "Placed"
   - PREPARING = "Preparing"
   - DELIVERING = "Delivering"
   - COMPLETED = "Completed"

═══════════════════════════════════════════════════════════════════════════════════
DEPENDENCY GRAPH
═══════════════════════════════════════════════════════════════════════════════════

Without Dependencies:
MenuItem (no internal dependencies)
OrderStatus (no internal dependencies)

Depends on MenuItem:
Restaurant (manages MenuItem objects)
Order (contains MenuItem objects)

Depends on User + Restaurant + MenuItem + Driver:
Order (links all together)

Depends on Order:
User (stores List[Order] for purchase_history)
Driver (stores List[Order] for active_deliveries)

Implementation Order (respects dependencies):

1. MenuItem ✓ Can implement first
2. OrderStatus ✓ Can implement first
3. User ✓ Can implement early (contains Order type hints)
4. Restaurant ✓ Can implement (uses MenuItem)
5. Driver ✓ Can implement (contains Order type hints)
6. Order ✓ Must implement last (depends on all others)

═══════════════════════════════════════════════════════════════════════════════════
KEY IMPLEMENTATION NOTES
═══════════════════════════════════════════════════════════════════════════════════

TYPE HINTS:
• Use typing.List, Dict, Optional for Python 3.7+
• Type hint all method parameters and return values
• Example: def add_item(self, item: MenuItem) -> None:

DATETIME IMPORT:
• Import datetime at top: from datetime import datetime
• Use datetime.now() for timestamps

ENUM USAGE:
• Import Enum: from enum import Enum
• Define OrderStatus(Enum) with string values
• Access as: OrderStatus.PLACED

LIST OPERATIONS:
• Use list comprehension for filtering:
items = [item for item in items if item.category == category]
• Use list.append() and list.remove()

CIRCULAR REFERENCES:
• User contains List[Order]
• Order contains User
• This is acceptable in Python; use forward references if needed:
from **future** import annotations (Python 3.7+)

DOCSTRINGS:
• Add docstrings to all public classes and methods
• Format:
def method(self, param: str) -> bool:
"""
Brief description

        Args:
            param: Parameter description

        Returns:
            Return value description
        """

═══════════════════════════════════════════════════════════════════════════════════
EXPECTED OUTCOMES
═══════════════════════════════════════════════════════════════════════════════════

After Phase 1 (Foundation):
✓ All five classes defined with attributes
✓ All **init**() methods working
✓ All **repr**() methods for debugging

After Phase 2 (Core Functionality):
✓ All business logic methods implemented
✓ Cost calculations working automatically
✓ Status transitions functioning
✓ Data validation in place

After Phase 3 (Integration):
✓ Classes properly linked together
✓ No circular reference issues
✓ Bidirectional relationships working (e.g., User ↔ Order)

After Phase 4 (Testing):
✓ All functionality verified
✓ Edge cases handled
✓ Example usage demonstrates complete workflow
✓ Production-ready code

═══════════════════════════════════════════════════════════════════════════════════
TOTAL EFFORT
═══════════════════════════════════════════════════════════════════════════════════

Estimated Timeline:
Phase 1 (Foundation) : 30-45 minutes
Phase 2 (Functionality) : 45-60 minutes
Phase 3 (Integration) : 30-45 minutes
Phase 4 (Testing) : 30-45 minutes
─────────────────────────────────────────
TOTAL : 2.5-4 hours

Code Size:
Expected lines of code: 400-600 (including docstrings and comments)
5 classes + 1 enum + main/example section

Quality Metrics:
✓ Type coverage: 100%
✓ Docstring coverage: 100%
✓ Method test coverage: All major functionality
✓ PEP 8 compliance: Full

═══════════════════════════════════════════════════════════════════════════════════
