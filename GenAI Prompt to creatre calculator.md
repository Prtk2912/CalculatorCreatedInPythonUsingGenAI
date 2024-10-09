# Prompt: Create a Python Calculator Using Tkinter

Create a functional calculator application using Python and the tkinter library. The calculator should have the following features and specifications:

1. Use the tkinter library for the graphical user interface.
2. Implement a main `Calculator` class that inherits from `tk.Tk`.
3. Create a display area using a tkinter `Entry` widget with the following properties:
   - Right-justified text
   - Large font size (e.g., Arial 24)
   - Sunken relief
   - Span across the top of the calculator window

4. Create buttons for the following:
   - Digits 0-9
   - Decimal point (.)
   - Basic operations: addition (+), subtraction (-), multiplication (*), division (/)
   - Parentheses: ( and )
   - Clear (C)
   - Equals (=)
   - Sign change (±)
   - Advanced operations: square root (√), square (x²), sine (sin), cosine (cos)

5. Arrange the buttons in a grid layout with 4 columns.

6. Use different background colors for different types of buttons:
   - White for digit buttons
   - Light blue for the equals button
   - Light red for the clear button
   - Light orange for basic operation buttons
   - Light purple for advanced operation buttons
   - Light gray for other buttons (parentheses, sign change)

7. Implement the following methods in the `Calculator` class:
   - `__init__`: Set up the window and create all widgets
   - `create_button`: A helper method to create and grid a button
   - `click`: Handle digit and basic operation button clicks
   - `calculate`: Perform the calculation when equals is clicked
   - `clear`: Clear the display
   - `toggle_sign`: Change the sign of the current number
   - `advanced_operation`: Handle advanced operations (sqrt, square, sin, cos)

8. Use a `StringVar` to manage the content of the display Entry widget.

9. For basic calculations, use Python's `eval()` function, but wrap it in a try-except block to handle errors.

10. For advanced operations, use the `math` module and handle potential errors.

11. Ensure the window is resizable and that widgets expand appropriately when the window is resized.

12. Add appropriate padding around widgets for a polished look.

13. Use lambda functions to pass arguments to button command callbacks.

14. Include a `__main__` check to run the application.

Follow these guidelines to create a functional, user-friendly calculator application. Remember to test each feature thoroughly to ensure proper functionality.

